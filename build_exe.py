"""
Build script for creating SlideAudioGenerator.exe
Run this with: python build_exe.py
"""

import PyInstaller.__main__
import os

# PyInstaller configuration
PyInstaller.__main__.run([
    'GUI.py',                          # Your main script
    '--name=SlideAudioGenerator',      # Name of the .exe file
    '--onefile',                       # Create a single .exe file
    '--windowed',                      # No console window (GUI only)
    '--clean',                         # Clean cache before building
    '--noconfirm',                     # Replace output directory without asking
    # Add any additional files or data here if needed
    # '--add-data=icon.ico;.',         # Example: add an icon file
])

print("\n" + "="*50)
print("BUILD COMPLETE!")
print("="*50)
print(f"\nYour executable is located at:")
print(f"   {os.path.abspath('dist/SlideAudioGenerator.exe')}")
print("\nYou can share this .exe file with anyone!")
print("\nNote: The .exe file will be large (~50-100 MB)")
print("   because it includes Python and all dependencies.")
print("\n" + "="*50)
