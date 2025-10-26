# 🎙️ Slide Audio Generator

Generate audio files from slide content using Google's Gemini AI with text-to-speech capabilities.

## 🚀 Quick Start (Running from Source)

### Prerequisites
- Python 3.8 or higher
- A Google AI API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python GUI.py
   ```

4. **Enter your Google AI API key** in the application and start generating audio!

## 📦 Distribution Options

### Option 1: Share Python Scripts (Easiest)

Share the entire project folder with users and provide them these instructions:

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Open terminal/command prompt in the project folder
3. Run: `pip install -r requirements.txt`
4. Run: `python GUI.py`

**Pros:** Works on Windows, Mac, and Linux  
**Cons:** Users need Python installed

### Option 2: Build Executables (No Python Required)

Create standalone executables for specific platforms:

#### For Windows (on Windows):
```powershell
python build_exe.py
```
Share `dist/SlideAudioGenerator.exe` with Windows users.

#### For macOS (on a Mac):
```bash
python build_mac.py
```
Share `dist/SlideAudioGenerator.app` with Mac users.

#### Cross-Platform Build:
```bash
python build_cross_platform.py
```
Automatically detects your OS and builds accordingly.

**Important:** Executables must be built on the target OS (build .exe on Windows, .app on Mac, etc.)

**Pros:** Users don't need Python  
**Cons:** Large file size (~50-100 MB), platform-specific builds

## 🔧 Usage

1. **Enter your Google AI API Key** (required)
2. **Set a folder name** for saving audio files (default: `SlideAudioFiles`)
3. **Add slides** using the interface
4. **Customize voice and settings** (optional)
5. **Generate audio** - the app will create WAV files for each slide

## 📁 Project Structure

```
CLT/
├── GUI.py                      # Main application interface
├── gemini.py                   # Audio generation logic
├── requirements.txt            # Python dependencies
├── build_exe.py               # Windows build script
├── build_mac.py               # macOS build script
├── build_cross_platform.py    # Auto-detect OS build script
├── BUILD_INSTRUCTIONS.md      # Detailed build guide
└── README.md                  # This file
```

## 🎨 Features

- **Multiple voice options** (Aoede, Charon, Fenrir, Kore, Puck, Schedar)
- **Customizable content specification** for audio generation
- **Batch processing** of multiple slides
- **Progress tracking** with detailed logs
- **Audio speed control**
- **Easy-to-use GUI**

## 🔑 Getting a Google AI API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and paste it in the application

## 🐛 Troubleshooting

### "Module not found" errors
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### API errors
- Check that your API key is correct
- Ensure you have internet connection
- Verify your Google AI API quota hasn't been exceeded

### Audio not generating
- Check the console/log output for error messages
- Verify the folder has write permissions
- Ensure the slide content is not empty

## 📄 License

This project is provided as-is for educational and personal use.

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📚 Additional Resources

- [Google Generative AI Documentation](https://ai.google.dev/docs)
- [PyInstaller Documentation](https://pyinstaller.org/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
