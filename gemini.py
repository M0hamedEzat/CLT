from google import genai
from google.genai import types
import wave
import os

# Slide content organized by slide number
slides = {
    2: "Listen to the following and repeat.",
}

# Set up the wave file to save the output


def save_wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    """Save audio data as a WAV file."""
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)
    print(f"✅ Audio saved: {filename}")


def generate_slide_audio(slide_num, text, client, voice_name='Schedar', folder_name='SlideAudioFiles', content_specification="Read aloud clearly and naturally"):
    """Generate audio for a single slide."""
    print(f"\n🎙️ Generating audio for Slide #{slide_num}...")

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"📁 Created folder: {folder_name}")

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=f"{content_specification}: {text}",
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=voice_name,
                    )
                )
            ),
        )
    )

    data = response.candidates[0].content.parts[0].inline_data.data
    file_name = os.path.join(folder_name, f'slide_{slide_num}.wav')
    save_wave_file(file_name, data)
    return file_name


# Main execution
if __name__ == "__main__":
    api_key = input("Enter your Google Gemini API Key: ")
    client = genai.Client(api_key=api_key)

    print("🚀 Starting audio generation for all slides...")

    # Generate audio for each slide
    for slide_num, text in slides.items():
        generate_slide_audio(slide_num, text, client, voice_name='Schedar')

    print("\n✨ All audio files generated successfully!")
