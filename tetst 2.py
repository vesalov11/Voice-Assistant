import random
from gtts import gTTS
import speech_recognition as sr


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
    if "шаро" in message:
        if "чао" in message:
            exit()
        elif"youtube" in message:
            print('стартитаме you tube')


if __name__ == '__main__':
    print('test')
    while True:
        command = listen()
        hangle_message(command)
