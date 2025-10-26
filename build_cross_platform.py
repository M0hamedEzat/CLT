"""
Cross-platform build script for SlideAudioGenerator
Automatically detects OS and builds the appropriate executable
Run this with: python build_cross_platform.py
"""

import PyInstaller.__main__
import os
import sys
import platform

# Detect the operating system
os_name = sys.platform
is_windows = os_name == 'win32'
is_mac = os_name == 'darwin'
is_linux = os_name.startswith('linux')

print("="*50)
print(f"🖥️  Detected OS: {platform.system()} ({os_name})")
print("="*50)

# Base PyInstaller arguments
base_args = [
    'GUI.py',                          # Your main script
    '--name=SlideAudioGenerator',      # Name of the executable
    '--onefile',                       # Create a single file
    '--windowed',                      # No console window (GUI only)
    '--clean',                         # Clean cache before building
    '--noconfirm',                     # Replace output directory without asking
]

# Platform-specific arguments
if is_mac:
    print("📦 Building for macOS (.app bundle)...")
    base_args.extend([
        '--osx-bundle-identifier=com.slideaudiogenerator.app',
        # '--icon=icon.icns',          # Uncomment and add .icns icon if available
    ])
    output_name = 'SlideAudioGenerator.app'
    
elif is_windows:
    print("📦 Building for Windows (.exe)...")
    # base_args.extend([
    #     '--icon=icon.ico',           # Uncomment and add .ico icon if available
    # ])
    output_name = 'SlideAudioGenerator.exe'
    
elif is_linux:
    print("📦 Building for Linux (executable)...")
    # base_args.extend([
    #     '--icon=icon.png',           # Uncomment and add .png icon if available
    # ])
    output_name = 'SlideAudioGenerator'
    
else:
    print(f"⚠️  Unknown platform: {os_name}")
    print("Proceeding with default settings...")
    output_name = 'SlideAudioGenerator'

# Run PyInstaller
try:
    PyInstaller.__main__.run(base_args)
    
    print("\n" + "="*50)
    print("✅ BUILD COMPLETE!")
    print("="*50)
    print(f"\n📁 Your application is located at:")
    print(f"   {os.path.abspath(f'dist/{output_name}')}")
    print("\n📦 Distribution notes:")
    
    if is_mac:
        print("   • Share the .app bundle with Mac users")
        print("   • Users may need to right-click → Open (first time)")
        print("   • For wider distribution, consider code signing")
        print("   • See: https://developer.apple.com/support/code-signing/")
    elif is_windows:
        print("   • Share the .exe file with Windows users")
        print("   • Windows may show a security warning (normal for unsigned apps)")
        print("   • For wider distribution, consider code signing")
    elif is_linux:
        print("   • Share the executable with Linux users")
        print("   • Users may need to make it executable: chmod +x SlideAudioGenerator")
    
    print("\n⚠️  Note: The file will be large (~50-100 MB)")
    print("   because it includes Python and all dependencies.")
    print("\n" + "="*50)
    
except Exception as e:
    print(f"\n❌ BUILD FAILED: {e}")
    sys.exit(1)
