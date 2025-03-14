# Whisper Transcription Tool

A simple command-line tool for transcribing audio files using OpenAI's Whisper speech recognition model.

## Overview

This tool provides an easy way to transcribe speech from audio files into text using OpenAI's Whisper, a state-of-the-art multilingual speech recognition model. It can handle various audio formats and supports multiple languages.

Whisper is trained on a large dataset of diverse audio and is a multitasking model that can perform:
- Multilingual speech recognition
- Speech translation
- Language identification

## Installation

### Prerequisites

- Python 3.8 or newer
- FFmpeg (required for audio processing)

### Install FFmpeg

FFmpeg is required for processing audio files.

**On macOS:**
```bash
brew install ffmpeg
```

**On Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install ffmpeg
```

**On Windows:**
Using Chocolatey:
```bash
choco install ffmpeg
```

### Install Whisper and Dependencies

1. Clone this repository or download the script files:
```bash
git clone <repository-url>
cd vox-scribe
```

2. Install the required Python packages:

```bash
# Install Whisper directly from GitHub (recommended for latest version)
pip install git+https://github.com/openai/whisper.git

# Install gTTS for test audio generation (optional)
pip install gTTS
```

## Usage

### Basic Usage

Transcribe an audio file with default settings (using the 'base' model):

```bash
python3 transcribe.py your-audio-file.mp3
```

The transcription will be:
1. Displayed in the console
2. Saved as a text file with the same name as the input file (e.g., `your-audio-file.txt`)

### Command-line Options

```
usage: transcribe.py [-h] [--model {tiny,base,small,medium,large}] [--language LANGUAGE]
                            [--task {transcribe,translate}] [--output OUTPUT] [--verbose]
                            audio_file

Transcribe audio files using OpenAI's Whisper

positional arguments:
  audio_file            Path to the audio file to transcribe

optional arguments:
  -h, --help            show this help message and exit
  --model {tiny,base,small,medium,large}
                        Whisper model to use (default: base)
  --language LANGUAGE   Language code (optional, auto-detected if not specified)
  --task {transcribe,translate}
                        Task to perform (transcribe or translate to English, default: transcribe)
  --output OUTPUT       Output file path (default: [audio_filename].txt)
  --verbose             Show verbose output
```

### Examples

1. Basic transcription with default settings:
```bash
python3 transcribe.py recording.mp3
```

2. Use a different model size:
```bash
python3 transcribe.py recording.mp3 --model medium
```

3. Specify a language (improves accuracy):
```bash
python3 transcribe.py recording.mp3 --language Spanish
```

4. Translate to English:
```bash
python3 transcribe.py recording.mp3 --task translate
```

5. Specify custom output file:
```bash
python3 transcribe.py recording.mp3 --output my_transcript.txt
```

6. Show verbose output:
```bash
python3 transcribe.py recording.mp3 --verbose
```

### Models

Whisper offers several model sizes with different accuracy levels and processing speeds:

- `tiny`: Fastest, lowest accuracy (approx. 1GB of memory)
- `base`: Good balance between speed and accuracy (approx. 1GB)
- `small`: Better accuracy than base, slightly slower (approx. 2GB)
- `medium`: High accuracy, slower processing (approx. 5GB)
- `large`: Highest accuracy, slowest processing (approx. 10GB)

The model will be automatically downloaded the first time you use it.

## Creating Test Audio Files

The included `create_test_audio.py` script allows you to generate test audio files using Google's Text-to-Speech (gTTS) service. This is useful for testing the Whisper transcription capabilities with controlled content.

### Creating Test Audio Options

```
usage: create_test_audio.py [-h] [--text TEXT] [--output OUTPUT] [--language LANGUAGE]
                            [--slow] [--list-languages]

Create a test audio file using Google Text-to-Speech

optional arguments:
  -h, --help           show this help message and exit
  --text TEXT          Text to convert to speech
  --output OUTPUT      Output audio file name (default: test_audio.mp3)
  --language LANGUAGE  Language code (default: en)
  --slow               Generate slower speech
  --list-languages     List all available language codes and exit
```

### Test Audio Examples

1. Create a basic test audio file in English:
```bash
python3 create_test_audio.py
```

2. Create audio with custom text:
```bash
python3 create_test_audio.py --text "This is a custom message to test the Whisper transcription accuracy."
```

3. Create audio in a different language:
```bash
python3 create_test_audio.py --language es --text "Esto es una prueba de transcripción en español."
```

4. List all available language codes:
```bash
python3 create_test_audio.py --list-languages
```

## Supported Audio Formats

Whisper supports various audio formats including:
- MP3
- WAV
- FLAC
- OGG
- M4A
- and others supported by FFmpeg

## Troubleshooting

### SSL Certificate Issues on macOS

If you encounter SSL certificate verification issues on macOS, our script automatically handles this by setting:

```python
ssl._create_default_https_context = ssl._create_unverified_context
```

### Model Download Issues

When running the script for the first time, it will download the selected model. This requires an internet connection and may take some time depending on the model size and your connection speed.

### FFmpeg Not Found

If you see an error about FFmpeg not being found, make sure it's installed and available in your system's PATH.

## Example Results

When you run the script on an audio file, you'll see output similar to this:

```
Detected macOS, setting SSL context for certificate verification...
Loading Whisper model: base
Transcribing audio.mp3...

Transcription:
[Transcription text appears here]

Transcription saved to audio.txt
```

With verbose output:
```
Detected macOS, setting SSL context for certificate verification...
Loading Whisper model: base
Transcribing audio.mp3...
  Language: auto-detect
  Task: transcribe

Transcription:
[Transcription text appears here]

Transcription saved to audio.txt

Detected language: en
Number of segments: 12
```

## License

This tool uses OpenAI's Whisper, which is released under the MIT License.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) - The speech recognition model powering this tool
