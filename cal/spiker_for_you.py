import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') # print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

intro="Enter the document you want me to read for you."
#speak(intro)
document=input(str("Enter:"))
speak(document)
