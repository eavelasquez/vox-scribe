#!/usr/bin/env python3
"""
A utility script to create test audio files using Google Text-to-Speech.
This is useful for testing the Whisper transcription tool with custom audio content.
"""
import argparse
import os
from gtts import gTTS
from gtts.lang import tts_langs

def list_available_languages():
    """List all available languages supported by gTTS."""
    langs = tts_langs()
    print("\nAvailable languages:")
    print("--------------------")
    for code, name in sorted(langs.items()):
        print(f"{code}: {name}")

def main():
    parser = argparse.ArgumentParser(description="Create a test audio file using Google Text-to-Speech")
    parser.add_argument(
        "--text", 
        default="This is a test audio file for the Whisper transcription tool.",
        help="Text to convert to speech"
    )
    parser.add_argument(
        "--output", 
        default="test_audio.mp3",
        help="Output audio file name (default: test_audio.mp3)"
    )
    parser.add_argument(
        "--language", 
        default="en",
        help="Language code (default: en)"
    )
    parser.add_argument(
        "--slow", 
        action="store_true",
        help="Generate slower speech"
    )
    parser.add_argument(
        "--list-languages", 
        action="store_true",
        help="List all available language codes and exit"
    )
    args = parser.parse_args()
    
    # List languages if requested
    if args.list_languages:
        list_available_languages()
        return
    
    print(f"Converting text to speech...")
    print(f"Text: {args.text}")
    print(f"Language: {args.language}")
    print(f"Slow speech: {'Yes' if args.slow else 'No'}")
    
    try:
        # Convert text to speech
        tts = gTTS(text=args.text, lang=args.language, slow=args.slow)
        
        # Save the audio file
        tts.save(args.output)
        
        file_size = os.path.getsize(args.output) / 1024  # Size in KB
        print(f"\nAudio file saved to {args.output} ({file_size:.1f} KB)")
        print(f"\nYou can now transcribe it with:")
        print(f"python3 simple_transcribe.py {args.output}")
    except Exception as e:
        print(f"\nError: {str(e)}")
        if "Language" in str(e):
            print("\nTry using --list-languages to see all available language codes.")

if __name__ == "__main__":
    main() 
