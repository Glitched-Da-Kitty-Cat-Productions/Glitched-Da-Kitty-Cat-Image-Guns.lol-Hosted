from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import logging
from datetime import datetime
import os
import requests
import re

load_dotenv()

UPLOAD_KEY = os.getenv("GUNSLOLUPLOADKEY")
if not UPLOAD_KEY:
    raise ValueError("GUNSLOLUPLOADKEY is not set in the environment variables.")

AUTH_KEY = os.getenv("AUTHKEY")
if not AUTH_KEY:
    raise ValueError("AUTHKEY is not set in the environment variables.")
if AUTH_KEY == "SET_ME_TO_SOMETHING_SECURE":
    print("AUTHKEY is empty. Please set a valid AUTHKEY in the environment variables.")

APIURL = os.getenv("APIURL")
if not APIURL:
    raise ValueError("APIURL is not set in the environment variables.")
if not APIURL.endswith('/'):
    print("APIURL should end with a slash. Adding it automatically.")
    APIURL += '/'
if not APIURL.startswith('http://') and not APIURL.startswith('https://'):
    raise ValueError("APIURL must start with 'http://' or 'https://'.")

AuthorName = os.getenv("AuthorName")
if not AuthorName:
    raise ValueError("AuthorName is not set in the environment variables.")

WebsiteName = os.getenv("WebsiteName")
if not WebsiteName:
    raise ValueError("WebsiteName is not set in the environment variables.")


DESCRIPTION = os.getenv("DESCRIPTION")
if not DESCRIPTION:
    raise ValueError("DESCRIPTION is not set in the environment variables.")

THEME_COLOR = os.getenv("THEMECOLOR")
if not THEME_COLOR:
    raise ValueError("THEMECOLOR is not set in the environment variables.")

CUSTOM_EMBED_URL = os.getenv("CUSTOM_EMBED_URL")
if not CUSTOM_EMBED_URL:
    raise ValueError("CUSTOM_EMBED_URL is not set in the environment variables.")
if not CUSTOM_EMBED_URL.startswith('http://') and not CUSTOM_EMBED_URL.startswith('https://'):
    raise ValueError("CUSTOM_EMBED_URL must start with 'http://' or 'https://'.")
if CUSTOM_EMBED_URL == "WHAT_EVER_YOU_WANT":
    raise ValueError("Please set a valid CUSTOM_EMBED_URL in the environment variables.")

app = Flask(__name__, static_folder='static', template_folder='templates')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_image_id(url):
    if not url:
        return None
    match = re.search(r'https?://i\.guns\.lol/([a-zA-Z0-9]+)', url)
    if match:
        return match.group(1)
    return None

@app.route('/u', methods=['POST'])
def upload():
    try:
        provided_key = request.form.get('key') or request.headers.get('X-API-Key')
        if  provided_key != AUTH_KEY:
            return jsonify({"proxy_link": "", "deletion_url": "", "error": "Invalid API key"}), 401
        if 'file' not in request.files:
            return jsonify({"proxy_link": "", "deletion_url": "", "error": "No file part in the request"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"proxy_link": "", "deletion_url": "", "error": "No file selected"}), 400
        client_ip = request.remote_addr
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"[{timestamp}] Upload request from {client_ip} - File: {file.filename}")
        files = {'file': (file.filename, file.stream, file.content_type)}
        data = {'key': UPLOAD_KEY}
        response = requests.post('https://guns.lol/api/upload', files=files, data=data)
        if response.status_code == 200:
            result = response.json()
            if 'link' in result:
                imageid = extract_image_id(result['link'])
                if imageid:
                    result['imageid'] = imageid
                    result['proxy_link'] = f"{APIURL}i?id={imageid}"
                    logger.info(f"[{timestamp}] Upload successful - URL: {result['link']}")
            return jsonify(result), 200
        else:
            logger.error(f"[{timestamp}] Upload failed - Status Code: {response.status_code}, Response: {response.text}")
            return jsonify({"proxy_link": "", "deletion_url": "", "error": "Upload failed"}), response.status_code
    except Exception as e:
        logger.error(f"An error occurred during upload: {e}")
        return jsonify({"proxy_link": "", "deletion_url": "", "error": "Internal server error"}), 500
def get_image_info(image_url):
    try:
        response = requests.head(image_url, timeout=10)
        if response.status_code == 200:
            content_length = response.headers.get('content-length')
            if content_length:
                size_bytes = int(content_length)
                if size_bytes < 1024:
                    size_str = f"{size_bytes}B"
                elif size_bytes < 1024 * 1024:
                    size_str = f"{size_bytes // 1024}KB"
                else:
                    size_str = f"{size_bytes // (1024 * 1024)}MB"
                return size_str
        return "Size unknown"
    except:
        return "Size unknown"

@app.route('/i', methods=['GET'])
def image():
    try:
        imageid = request.args.get('id')
        if not imageid:
            return "Missing image ID parameter", 400
        if not re.match(r'^[a-zA-Z0-9]+$', imageid):
            return "Invalid image ID format", 400
            
        guns_lol_url = f"https://i.guns.lol/{imageid}"
        image_direct_url = f"https://images.guns.lol/{imageid}.png"
        proxy_url = f"{APIURL}/i?id={imageid}"
        
        file_size = get_image_info(image_direct_url)
        current_time = datetime.now().strftime("%b %d, %Y, %H:%M:%S")
        
        return render_template('image.html',
                        guns_lol_url=guns_lol_url,
                        image_direct_url=image_direct_url,
                        proxy_url=proxy_url,
                        image_id=imageid,
                        author_name=AuthorName,
                        website_name=WebsiteName,
                        description=DESCRIPTION,
                        theme_color=THEME_COLOR,
                        file_size=file_size,
                        upload_date=current_time,
                        custom_embed_url=CUSTOM_EMBED_URL)
    except Exception as e:
        logger.error(f"An error occurred while processing the image: {e}")
        return "Internal server error", 500
    
import json

def create_sharex_config():
    config = {
        "Version": "13.1.0",
        "Name": WebsiteName,
        "DestinationType": "ImageUploader, FileUploader",
        "RequestMethod": "POST",
        "RequestURL": f"{APIURL}u",
        "Body": "MultipartFormData",
        "Arguments": {
            "key": AUTH_KEY,
        },
        "FileFormName": "file",
        "URL": "$json:proxy_link$",
        "DeletionURL": "$json:deletion_url$",
        "ErrorMessage": "$json:error$"
    }
    try:
        with open('sharex_upload.sxcu', 'w') as f:
            json.dump(config, f, indent=2)
        print("ShareX config file created successfully.")
    except Exception as e:
        print(f"Failed to create ShareX config file: {e}")

if __name__ == '__main__':
    create_sharex_config()
    app.run(debug=True)
