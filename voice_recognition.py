# Imports
import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox

# Defining a function "recognize_speech"
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            # Adjusting for ambient noise and record audio
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            
            # Recognizing speech using Google Web API
            text = recognizer.recognize_google(audio)
            result_text.set(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I could not understand the audio.")
        except sr.RequestError:
            messagebox.showerror("Error", "Sorry, there was an issue with the request.")

# Initializing the main window
root = tk.Tk()
root.title("Voice Recognition")

# Creating a StringVar to update recognized text
result_text = tk.StringVar()
result_text.set("Press 'Start' and speak...")

# Creating GUI elements
label = tk.Label(root, textvariable=result_text, wraplength=400)
label.pack(pady=20)

start_button = tk.Button(root, text="Start", command=recognize_speech)
start_button.pack(pady=20)

# Starting the GUI event loop
root.mainloop()
