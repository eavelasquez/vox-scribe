#!/usr/bin/env python3
"""
A simple script to transcribe audio using Whisper.
"""
import sys
import os
import ssl
import argparse
import whisper

def main():
    parser = argparse.ArgumentParser(description="Transcribe audio files using OpenAI's Whisper")
    parser.add_argument("audio_file", help="Path to the audio file to transcribe")
    parser.add_argument(
        "--model", 
        default="base", 
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model to use (default: base)"
    )
    parser.add_argument(
        "--language", 
        default=None,
        help="Language code (optional, auto-detected if not specified)"
    )
    parser.add_argument(
        "--task",
        default="transcribe",
        choices=["transcribe", "translate"],
        help="Task to perform (transcribe or translate to English, default: transcribe)"
    )
    parser.add_argument(
        "--output", 
        default=None,
        help="Output file path (default: [audio_filename].txt)"
    )
    parser.add_argument(
        "--verbose", 
        action="store_true",
        help="Show verbose output"
    )
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.isfile(args.audio_file):
        print(f"Error: File '{args.audio_file}' does not exist")
        return
    
    # Handle SSL certificate issues on macOS
    if sys.platform == 'darwin':
        print("Detected macOS, setting SSL context for certificate verification...")
        ssl._create_default_https_context = ssl._create_unverified_context
    
    # Set default output file if not specified
    if args.output is None:
        args.output = os.path.splitext(args.audio_file)[0] + ".txt"
    
    # Load model
    print(f"Loading Whisper model: {args.model}")
    try:
        model = whisper.load_model(args.model)
        
        # Transcribe
        print(f"Transcribing {args.audio_file}...")
        if args.verbose:
            print(f"  Language: {args.language if args.language else 'auto-detect'}")
            print(f"  Task: {args.task}")
        
        result = model.transcribe(
            args.audio_file,
            language=args.language,
            task=args.task,
            verbose=args.verbose
        )
        
        # Print result
        print("\nTranscription:")
        print(result["text"])
        
        # Save to file
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        print(f"\nTranscription saved to {args.output}")
        
        # If verbose, print additional information
        if args.verbose and "language" in result:
            print(f"\nDetected language: {result['language']}")
            if "segments" in result:
                print(f"Number of segments: {len(result['segments'])}")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
