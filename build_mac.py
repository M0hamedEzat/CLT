"""
Build script for creating SlideAudioGenerator.app for macOS
Run this with: python build_mac.py (on a Mac)
"""

import PyInstaller.__main__
import os
import sys

# Check if running on macOS
if sys.platform != 'darwin':
    print("WARNING: This script should be run on macOS!")
    print("   You are currently on:", sys.platform)
    response = input("\nDo you want to continue anyway? (y/n): ")
    if response.lower() != 'y':
        sys.exit(1)

# PyInstaller configuration for macOS
PyInstaller.__main__.run([
    'GUI.py',                          # Your main script
    '--name=SlideAudioGenerator',      # Name of the .app bundle
    '--onefile',                       # Create a single executable
    '--windowed',                      # No console window (GUI only)
    '--clean',                         # Clean cache before building
    '--noconfirm',                     # Replace output directory without asking
    '--osx-bundle-identifier=com.slideaudiogenerator.app',  # Bundle identifier for macOS
    # Add any additional files or data here if needed
    # '--icon=icon.icns',              # Example: add a macOS icon file (.icns format)
])

print("\n" + "="*50)
print("BUILD COMPLETE!")
print("="*50)
print(f"\nYour application is located at:")
print(f"   {os.path.abspath('dist/SlideAudioGenerator.app')}")
print("\nYou can share this .app bundle with Mac users!")
print("\nNote: The .app will be large (~50-100 MB)")
print("   because it includes Python and all dependencies.")
print("\nTo distribute, you may need to code sign it:")
print("   See: https://developer.apple.com/support/code-signing/")
print("\n" + "="*50)
