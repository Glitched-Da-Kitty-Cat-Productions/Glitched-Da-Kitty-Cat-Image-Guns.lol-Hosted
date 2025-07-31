# Glitched Da Kitty Cat Image Hosting Service

A Flask-based image hosting proxy service that interfaces with the guns.lol image hosting API, providing a custom web interface for viewing uploaded images with enhanced metadata display and a sleek dark theme.

## ⚠️ Important Notice

Uses guns.lol image hosting so it isn't free but feel free to edit the code to fit to your own image host.

## ✨ Features

- 🌙 **Dark Theme Interface** - Modern, eye-friendly dark theme design
- 📁 **Image Upload Proxy** - Seamless integration with guns.lol API
- 📊 **Enhanced Metadata Display** - File size detection and display
- 📋 **Copy to Clipboard** - Easy sharing functionality
- 📱 **Responsive Design** - Works great on all devices
- 🔗 **Direct Image Links** - Access original images directly
- ❌ **Error Handling** - Graceful handling of missing images
- ⚡ **Fast Loading** - Optimized for quick image viewing

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Flask
- guns.lol API access

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Glitched-Da-Kitty-Cat-Image-Guns.lol-Hosted.git
   cd Glitched-Da-Kitty-Cat-Image-Guns.lol-Hosted
   ```

2. **Install dependencies**
   ```bash
   pip install flask requests
   ```

3. **⚙️ Configure Environment Variables**
   
   **You MUST fill out the environment file before running the application!**
   
   Create a `.env` file in the root directory with the following variables:
   ```env
   GUNSLOLUPLOADKEY=your_guns_lol_upload_key_here
   AUTHKEY=your_authentication_key_here
   APIURL=http://localhost:5000/
   NAME=Your Display Name
   DESCRIPTION=Your Site Description
   THEMECOLOR=#ff00c8
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

The service will be available at `http://localhost:5000`

## 📝 Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GUNSLOLUPLOADKEY` | API key for guns.lol upload service | ✅ Yes | - |
| `AUTHKEY` | Authentication key for upload endpoint | ✅ Yes | - |
| `APIURL` | Base URL for your service | ✅ Yes | - |
| `NAME` | Display name for uploader | ✅ Yes | - |
| `DESCRIPTION` | Site description for meta tags | ✅ Yes | - |
| `THEMECOLOR` | Theme color for meta tags | ❌ No | `#ff00c8` |

## 🔌 API Endpoints

### Upload Image
- **Endpoint:** `POST /u`
- **Description:** Upload images via guns.lol proxy
- **Authentication:** Requires `AUTHKEY`

### View Image
- **Endpoint:** `GET /i?id=<image_id>`
- **Description:** View uploaded image with enhanced UI
- **Features:** Metadata display, copy functionality, responsive design

## 🏗️ Project Structure

```
├── main.py              # Flask application backend
├── templates/
│   ├── image.html       # Image viewer page
│   └── index.html       # Main page
├── static/
│   ├── styles.css       # Dark theme styling
│   └── scripting.js     # JavaScript utilities
├── .env                 # Environment configuration (create this!)
└── README.md           # This file
```

## 🛠️ Technology Stack

- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **API Integration:** guns.lol hosting service
- **Styling:** Custom dark theme CSS
- **Deployment:** Any Python-compatible hosting platform

## 🎨 Customization

The application is designed to be easily customizable:

- **Themes:** Modify `static/styles.css` for different color schemes
- **Image Host:** Replace guns.lol integration in `main.py` with your preferred service
- **UI Components:** Update templates in the `templates/` directory
- **Functionality:** Extend features in `static/scripting.js`

## 📦 Dependencies

- `flask` - Web framework
- `requests` - HTTP library for API calls
- `os` - Environment variable handling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source. Feel free to modify it to work with your preferred image hosting service.

## ⚡ Quick Tips

- Make sure to keep your API keys secure and never commit them to version control
- Test your environment variables before deploying
- The dark theme is optimized for image viewing - perfect for showcasing photos
- Consider adding rate limiting for production deployments

---

**Need help?** Ask questions or report issues [here](https://discord.gg/rNNpGDcCeZ).
# THIS AD WAS AI GENERATED BECAUSE I AM LAZY AND DIDN'T WANT TO MAKE A REAL ONE :)