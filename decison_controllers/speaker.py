import pyttsx3
import speech_recognition as sr
import datetime
from multiprocessing import Process
import keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    if isinstance(audio, list):
        for a in audio:
            engine.say(a)
            engine.runAndWait()
    else:
        engine.say(audio)
        engine.runAndWait()


def take_speech():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=0) as source:
            print("Listening....")
            r.pause_threshold = 1
            r.energy_threshold = 100
            audio = r.listen(source)
            print("Recognizing....")
            query = r.recognize_google(audio, language='en')
            print(f"User said : {query}\n")
            return query
    except Exception as e:
        print("Please Say that again.")
        return "None"


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        return speak("Good Morning !! Please tell me  , what can i do for you")
    elif 12 < hour < 17:
        return speak("Good After noon!! Please tell me  , what can i do for you")
    else:
        return speak("Good Evening!! Please tell me  , what can i do for you")


def speech_control(content):
    try:
        p = Process(target=speak, args=(content,))
        p.start()
        while p.is_alive():
            if keyboard.is_pressed('q'):
                p.terminate()
            else:
                continue
    except Exception as err:
        print(f"{err}")
        raise