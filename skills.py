import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("Hello World!")
engine.runAndWait()
engine.stop()