import random
from gtts import gTTS
import speech_recognition as sr
import webbrowser

import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



engine.say("Hello im your voices assistant Zara")
engine.runAndWait()
engine.stop()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Кажете команда")
        audio = r.listen(sourse)
        try:
            speech = r.recognize_google(audio, language='bg')
            print(speech)
            return (speech)
        except sr.UnknownValueError:
            return "error"
        except sr.RequestError:
            return "error"

def hangle_message(message):
    message = message.lower()
    if "зара" in message:
        if "чао" in message:
            exit()
        elif"youtube" in message:
            print('стартитаме you tube')
            webbrowser.open_new_tab('https://www.youtube.com')
        elif"netflix" in message:
            print('Стартираме Netflix')
            webbrowser.open_new_tab('https://www.netflix.com')


if __name__ == '__main__':
    print('test')
    while True:
        command = listen()
        hangle_message(command)