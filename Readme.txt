Smart Speech & Translator – Python Speech & Language Tool

Smart Speech & Translator is a modern Python application that combines real-time Speech-to-Text, Text-to-Speech, and automatic language translation in a simple Tkinter interface. Users can speak to generate text, translate typed text into another language, and instantly hear the translated output using Google TTS.

FEATURES
- Text → Translate → Speech
  * Enter text, choose a language code (en, hi, gu, kn, etc.)
  * Text is translated using GoogleTranslator
  * Speech is generated using gTTS
  * Audio plays automatically and deletes after playback

- Speech → Text
  * Converts voice to text using SpeechRecognition
  * Handles background noise
  * Inserts recognized text into the GUI

- Language List
  * Displays all gTTS-supported languages

- Modern Tkinter UI
  * Dark theme interface
  * Clean layout and labeled sections

TECHNOLOGIES USED
- Tkinter (GUI)
- gTTS (Text-to-Speech)
- SpeechRecognition (Speech-to-Text)
- deep-translator (GoogleTranslator)
- playsound (audio playback)
- PyAudio (microphone input)

INSTALLATION
pip install gTTS playsound SpeechRecognition deep-translator pyaudio

RUNNING THE APP
python main.py

USAGE
1. Speech → Text:
   - Click “Speech → Text”
   - Stay silent for 2 seconds
   - Speak clearly
   - Text appears automatically

2. Text → Translate → Speech:
   - Type text
   - Enter language code
   - Click “Translate & Speak”
   - Translated speech is played instantly

3. List Languages:
   - Click “List Languages” to see all available language codes.

DEVELOPERS
- Shubham Singh
- Yajnik Sharma
