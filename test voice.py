import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sir')
    elif hour>=12 and hour<18:
        speak('Good Afternoon sir')
    else:
        speak('Good Evening sir')

    speak('I am your voice assistent vesalov')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print('Listening...')

        r.pause_threshold = 1

        audio = r.listen(source)

    print(takeCommand())
    try:
        print("You said " + r.recognize(audio))  # recognize speech using Google Speech Recognition

        print('Recognizing...')
        query = r.recognize_google(audio, language='bg')
        print(f"User said: {query}\n")

    except Exception as e:

        print('say that again pls sir')
        return "None"
    return query


if __name__ == "__main__":
   wishMe()
