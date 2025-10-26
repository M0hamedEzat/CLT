import tkinter as tk
from tkinter import ttk, messagebox
from gemini import generate_slide_audio, slides
from google import genai
import threading


class AudioGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Slide Audio Generator")
        self.root.geometry("700x650")

        # API Key
        tk.Label(root, text="API Key:").pack(pady=5)
        self.api_key_entry = tk.Entry(root, width=50, show="*")
        self.api_key_entry.insert(0, "")
        self.api_key_entry.pack(pady=5)

        # Folder name for saving the audio files
        tk.Label(root, text="Folder name:").pack(pady=5)
        self.folder_name_entry = tk.Entry(root, width=50)
        self.folder_name_entry.pack(pady=5)
        self.folder_name_entry.insert(0, "SlideAudioFiles")

        # Advanced options - Collapsible section
        self.advanced_visible = False
        self.advanced_frame = tk.Frame(root)

        # Toggle button for advanced options
        self.toggle_btn = tk.Button(
            root,
            text="▶ Advanced: Custom Content Specification",
            command=self.toggle_advanced,
            bg='#f0f0f0',
            font=('Arial', 9),
            anchor='w',
            relief='flat',
            cursor='hand2'
        )
        self.toggle_btn.pack(pady=5, padx=20, fill='x')

        # Advanced options content (initially hidden)
        tk.Label(self.advanced_frame, text="Content Specification (how AI should read):",
                 font=('Arial', 9)).pack(anchor='w', padx=5, pady=2)

        self.content_spec_entry = tk.Entry(
            self.advanced_frame, width=50, font=('Arial', 9))
        self.content_spec_entry.pack(pady=5, padx=5)
        self.content_spec_entry.insert(0, "Read aloud clearly and naturally")

        tk.Label(self.advanced_frame,
                 text="💡 Examples: 'Speak slowly', 'Read enthusiastically', 'Pronounce carefully'",
                 font=('Arial', 7), fg='#666').pack(anchor='w', padx=5)

        # Slide content input
        tk.Label(root, text="Insert The Content of The slides. Use '#' to separate each slide:",
                 font=('Arial', 10, 'bold')).pack(pady=10)

        # Create a Text widget (multi-line input)
        text_frame = tk.Frame(root)
        text_frame.pack(pady=5, padx=20, fill='both', expand=True)

        # Scrollbar for the text box
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')

        # Text widget
        self.text_entry = tk.Text(
            text_frame,
            height=10,
            width=60,
            font=('Arial', 9),
            wrap='word',  # Wrap text by word
            yscrollcommand=scrollbar.set
        )
        self.text_entry.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.text_entry.yview)

        # Pre-fill with example
        example_text = """# Listen to the following and repeat.
# Business - Business - Business. Some foreign people travel to Egypt for business."""

        self.text_entry.insert('1.0', example_text)

        # Info label
        tk.Label(root, text="Each line starting with '#' will become a separate audio file",
                 font=('Arial', 8), fg='#666').pack(pady=2)

        # Voice selection
        tk.Label(root, text="Voice:").pack(pady=5)
        self.voice_combo = ttk.Combobox(root, values=[
            'Zephyr', 'Puck', 'Charon', 'Kore', 'Fenrir', 'Leda', 'Orus', 'Aoede',
            'Callirrhoe', 'Autonoe', 'Enceladus', 'lapetus', 'Umbriel', 'Algieba',
            'Despina', 'Erinome', 'Algenib', 'Rasalgthi', 'Laomedia', 'Achernar',
            'Alnilam', 'Schedar', 'Gacrux', 'Plucherrima', 'Achird', 'Zubenelgenubi',
            'Vindemiatrix', 'Sadachbia', 'Sadaltager', 'Sulafat'
        ])
        self.voice_combo.set('Schedar')
        self.voice_combo.pack(pady=5)

        # Generate button
        self.generate_btn = tk.Button(root, text="🎙️ Generate Audio", command=self.generate_audio,
                                      bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'))
        self.generate_btn.pack(pady=20)

        # Progress
        self.progress_label = tk.Label(root, text="")
        self.progress_label.pack(pady=5)

        self.progress_bar = ttk.Progressbar(
            root, length=400, mode='determinate')
        self.progress_bar.pack(pady=5)

    def toggle_advanced(self):
        """Toggle the visibility of advanced options."""
        if self.advanced_visible:
            # Hide advanced options
            self.advanced_frame.pack_forget()
            self.toggle_btn.config(
                text="▶ Advanced: Custom Content Specification")
            self.advanced_visible = False
        else:
            # Show advanced options (right after the toggle button)
            self.advanced_frame.pack(
                after=self.toggle_btn, pady=5, padx=20, fill='x')
            self.toggle_btn.config(
                text="▼ Advanced: Custom Content Specification")
            self.advanced_visible = True

    def generate_audio(self):
        api_key = self.api_key_entry.get()
        if not api_key:
            messagebox.showerror("Error", "Please enter API key")
            return

        # Get folder name
        folder_name = self.folder_name_entry.get().strip()
        if not folder_name:
            messagebox.showerror("Error", "Please enter a folder name")
            return

        # Get text content and parse slides
        text_content = self.text_entry.get(
            '1.0', 'end-1c')  # Get all text from Text widget

        if not text_content.strip():
            messagebox.showerror("Error", "Please enter slide content")
            return

        # Parse text: split by '#' and create slide dictionary
        lines = text_content.split('\n')
        parsed_slides = {}
        slide_num = 1

        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                # Remove '#' and get the text
                slide_text = line[1:].strip()
                if slide_text:  # Only add non-empty slides
                    parsed_slides[slide_num] = slide_text
                    slide_num += 1

        if not parsed_slides:
            messagebox.showerror(
                "Error", "No slides found! Make sure each slide starts with '#'")
            return

        # Show confirmation
        confirm = messagebox.askyesno(
            "Confirm Generation",
            f"Found {len(parsed_slides)} slides.\n\nGenerate audio in folder '{folder_name}'?"
        )

        if not confirm:
            return

        # Get content specification from advanced options
        content_spec = self.content_spec_entry.get().strip()
        if not content_spec:
            content_spec = "Read aloud clearly and naturally"  # Default fallback

        # Run in separate thread to avoid freezing GUI
        thread = threading.Thread(target=self._generate_thread,
                                  args=(api_key, parsed_slides, self.voice_combo.get(), folder_name, content_spec))
        thread.start()

    def _generate_thread(self, api_key, parsed_slides, voice, folder_name, content_spec):
        self.generate_btn.config(state='disabled', text='Generating...')
        self.progress_bar['maximum'] = len(parsed_slides)

        try:
            client = genai.Client(api_key=api_key)

            for i, (slide_num, slide_text) in enumerate(parsed_slides.items(), 1):
                self.progress_label.config(
                    text=f"Generating Slide {slide_num}...")
                generate_slide_audio(slide_num, slide_text,
                                     client, voice_name=voice, folder_name=folder_name,
                                     content_specification=content_spec)
                self.progress_bar['value'] = i
                self.root.update()

            messagebox.showinfo(
                "Success", f"✨ Generated {len(parsed_slides)} audio files!\n\nFiles saved in '{folder_name}' folder.")

        except Exception as e:
            messagebox.showerror("Error", f"Generation failed: {str(e)}")

        finally:
            self.generate_btn.config(state='normal', text='🎙️ Generate Audio')
            self.progress_label.config(text="")
            self.progress_bar['value'] = 0


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioGeneratorGUI(root)
    root.mainloop()


""" Zephyr
Puck
Charon
Kore
Fenrir
Leda
Orus
Aoede
Callirrhoe
Autonoe
Enceladus
lapetus
Umbriel
Algieba
Despina
Erinome
Algenib
Rasalgthi
Laomedia
Achernar
Alnilam
Schedar
Gacrux
Plucherrima
Achird
Zubenelgenubi
Vindemiatrix
Sadachbia
Sadaltager
Sulafat """


