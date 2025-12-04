from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
from tkinter import *
from tkinter import messagebox
from gtts.lang import tts_langs
from deep_translator import GoogleTranslator


# -------------------- TEXT → TRANSLATE → SPEECH --------------------
def text_to_speech():
    text = text_entry.get("1.0", END).strip()
    language = accent_entry.get().strip()

    if len(text) == 0 or len(language) == 0:
        messagebox.showerror("Error", "Enter both text and language code")
        return

    try:
        # ✅ TRANSLATE TEXT FIRST
        translated_text = GoogleTranslator(source="auto", target=language).translate(text)

        # ✅ CONVERT TO SPEECH
        speech = gTTS(text=translated_text, lang=language)
        speech.save("text.mp3")
        playsound("text.mp3")
        os.remove("text.mp3")

    except Exception as e:
        messagebox.showerror("Error", f"Text-to-Speech failed\n{e}")


# -------------------- SPEECH → TEXT --------------------
def speech_to_text():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True
    r.pause_threshold = 1.2

    with sr.Microphone() as source:
        messagebox.showinfo("Info", "Stay silent for 2 seconds...")
        r.adjust_for_ambient_noise(source, duration=2)

        messagebox.showinfo("Info", "Now speak clearly...")
        audio = r.listen(source, timeout=15)

    try:
        text = r.recognize_google(audio)
        text_entry.delete("1.0", END)
        text_entry.insert(END, text)

    except:
        messagebox.showerror("Error", "Could not understand voice")


# -------------------- LIST LANGUAGES --------------------
def list_languages():
    langs = tts_langs()
    formatted = "\n".join([f"{k} : {v}" for k, v in langs.items()])
    messagebox.showinfo("Available Languages", formatted)


# -------------------- MODERN GUI --------------------
root = Tk()
root.title("Smart Speech & Translator")
root.geometry("600x460")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

Label(
    root,
    text="Speech & Language Translator",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#1e1e2e"
).pack(pady=15)

frame = Frame(root, bg="#282a36")
frame.pack(padx=20, pady=10)

Label(frame, text="Enter Text:", fg="white", bg="#282a36").grid(row=0, column=0, sticky="w", padx=10, pady=5)

text_entry = Text(frame, height=6, width=55, font=("Arial", 11))
text_entry.grid(row=1, column=0, columnspan=2, padx=10)

Label(frame, text="Language Code (en / hi / gu / kn):", fg="white", bg="#282a36").grid(row=2, column=0, sticky="w", padx=10, pady=10)

accent_entry = Entry(frame, width=20, font=("Arial", 12))
accent_entry.grid(row=3, column=0, padx=10, sticky="w")
accent_entry.insert(0, "gu")  # Default Gujarati

btn_frame = Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=20)

Button(
    btn_frame,
    text="🎤 Speech → Text",
    width=20,
    height=2,
    bg="#ff79c6",
    fg="black",
    font=("Arial", 11, "bold"),
    command=speech_to_text
).grid(row=0, column=0, padx=10)

Button(
    btn_frame,
    text="🔊 Translate & Speak",
    width=20,
    height=2,
    bg="#50fa7b",
    fg="black",
    font=("Arial", 11, "bold"),
    command=text_to_speech
).grid(row=0, column=1, padx=10)

Button(
    root,
    text="📜 List Languages",
    width=25,
    bg="#8be9fd",
    font=("Arial", 10, "bold"),
    command=list_languages
).pack()

root.mainloop()