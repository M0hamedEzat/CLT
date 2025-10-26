# Build Instructions for SlideAudioGenerator

This guide explains how to build executables for different operating systems.

## 🎯 Quick Summary

**Important:** PyInstaller creates platform-specific executables. You must build on the same OS where you want to run the app:
- Build on **Windows** → creates `.exe` for Windows
- Build on **macOS** → creates `.app` for Mac
- Build on **Linux** → creates executable for Linux

## 📦 Building for Windows

1. Open terminal/PowerShell on Windows
2. Install PyInstaller (if not already installed):
   ```powershell
   pip install pyinstaller
   ```
3. Run the build script:
   ```powershell
   python build_exe.py
   ```
   Or use the cross-platform script:
   ```powershell
   python build_cross_platform.py
   ```
4. Find your executable at: `dist/SlideAudioGenerator.exe`

## 🍎 Building for macOS

1. Get access to a Mac computer
2. Transfer your project files to the Mac
3. Open Terminal on Mac
4. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
5. Run the macOS build script:
   ```bash
   python build_mac.py
   ```
   Or use the cross-platform script:
   ```bash
   python build_cross_platform.py
   ```
6. Find your app at: `dist/SlideAudioGenerator.app`

### macOS Security Note
When users first open the app, macOS may block it. To open:
- Right-click the app → Select "Open"
- Or: Go to System Preferences → Security & Privacy → Click "Open Anyway"

## 🐧 Building for Linux

1. On a Linux machine, install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Run the cross-platform build script:
   ```bash
   python build_cross_platform.py
   ```
3. Find your executable at: `dist/SlideAudioGenerator`
4. Make it executable (if needed):
   ```bash
   chmod +x dist/SlideAudioGenerator
   ```

## 🌐 Cross-Platform Script

The `build_cross_platform.py` script automatically detects your OS and builds accordingly. Use this script on any platform:

```bash
python build_cross_platform.py
```

## 🚀 Alternative: Don't Build at All

Instead of creating executables, you can distribute your Python scripts directly:

### Option 1: Python Script Distribution
Share the `.py` files with users and provide instructions:
```bash
# Install dependencies
pip install tkinter google-generativeai

# Run the app
python GUI.py
```

### Option 2: Use Cloud Services
Consider building a web version using:
- **Streamlit** - Easy Python web apps
- **Flask/Django** - More control
- **Electron** with Python backend - True cross-platform

### Option 3: GitHub Actions for Automated Builds
Set up GitHub Actions to automatically build for all platforms when you push code. This way you don't need access to a Mac or Linux machine.

## 🔧 Troubleshooting

### "Module not found" errors
Add missing modules to the build script:
```python
'--hidden-import=module_name',
```

### Large file size
The executable includes Python and all dependencies (~50-100 MB). This is normal for PyInstaller.

### Antivirus warnings
Unsigned executables may trigger warnings. Consider code signing for distribution.

### macOS "damaged" message
This happens with unsigned apps. Users can:
1. Right-click → Open (bypass Gatekeeper)
2. Or use: `xattr -cr SlideAudioGenerator.app` in Terminal

## 📚 Additional Resources

- [PyInstaller Documentation](https://pyinstaller.org/)
- [macOS Code Signing](https://developer.apple.com/support/code-signing/)
- [Windows Code Signing](https://docs.microsoft.com/en-us/windows/win32/seccrypto/cryptography-tools)

## 💡 Need Help?

If you need to build for macOS but don't have a Mac:
1. Use a virtual machine (macOS on Mac hardware only, per Apple's license)
2. Use a cloud Mac service (MacStadium, AWS Mac instances)
3. Ask a friend with a Mac to run the build script
4. Use GitHub Actions with macOS runners (free for public repos)
