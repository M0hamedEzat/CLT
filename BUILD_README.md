# How to Build SlideAudioGenerator.exe

## Method 1: Using the Batch File (Easiest)

1. Double-click `build_exe.bat`
2. Wait for the build to complete
3. Find your .exe in the `dist` folder

## Method 2: Using Python Script

1. Open terminal/command prompt
2. Run: `python build_exe.py`
3. Find your .exe in the `dist` folder

## Method 3: Manual PyInstaller Command

Open terminal and run:

```bash
pyinstaller --onefile --windowed --name SlideAudioGenerator GUI.py
```

## Build Options Explained:

- `--onefile`: Creates a single .exe file (easier to share)
- `--windowed`: No console window appears (GUI only)
- `--name SlideAudioGenerator`: Name of the output .exe
- `--clean`: Clean PyInstaller cache before building
- `--icon=myicon.ico`: Add a custom icon (optional)

## After Building:

1. **Output Location**: `dist\SlideAudioGenerator.exe`
2. **File Size**: ~50-100 MB (includes Python + all dependencies)
3. **Sharing**: Just share the .exe file - no Python installation needed!

## Important Notes:

⚠️ **API Key Security**: The API key is hardcoded in the .exe

- Consider removing the default API key before building
- Or let users enter their own API key

⚠️ **Dependencies**: Make sure `gemini.py` is in the same folder when building

⚠️ **First Run**: The .exe may take a few seconds to start (unpacking)

## Troubleshooting:

**Error: "gemini module not found"**

- Make sure `gemini.py` is in the same directory as `GUI.py`

**Error: "google-genai not found"**

- The package will be bundled automatically
- If issues occur, try: `pip install google-genai`

**Large File Size:**

- This is normal! The .exe includes Python + all libraries
- Use `--onedir` instead of `--onefile` for smaller size (but multiple files)

## Advanced: Reduce File Size

If you want a smaller .exe (but multiple files):

```bash
pyinstaller --windowed --name SlideAudioGenerator GUI.py
```

This creates a folder in `dist\` instead of a single file.
