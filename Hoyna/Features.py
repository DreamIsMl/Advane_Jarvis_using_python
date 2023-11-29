from pytube import YouTube
from pyautogui import click
from pyautogui import hotkey
import pyperclip
from time import sleep
# import pywhatkit
import webbrowser
import speech_recognition as sr

import webbrowser as web
# from Customevoice.voice import Speak
import os
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def TakeCommand():
    

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source,0,20)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')  #en-in

        print(f": Your Command : {query}\n")

    except Exception as e:
        Speak(None)
        return ""

    return query.lower()





def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    
def jarvis():
    Speak("What should I search on YouTube?")
    search_query = TakeCommand().lower()
    if search_query:
        url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
        webbrowser.open(url)
        Speak(f"Searching YouTube for {search_query}")
           
    


def DateConverter(Query):
    try:
        Date = Query.replace(" and ", "-")
        Date = Date.replace(" and ", "-")
        Date = Date.replace("and", "-")
        Date = Date.replace("and", "-")
        Date = Date.replace(" ", "")

        return str(Date)
    except Exception as e:
        print("Sorry! Plz tell me the date correctly")
        print(e)
        return None

def DownloadYouTube():
    
    
    
    
    

    sleep(2)
    click(x=725, y=87)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('F:\\Hoyna\\Youtubevideos\\')


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('F:\\Hoyna\\Youtubevideos\\')
    
from time import sleep
from pyautogui import click, write

def camera():
      # Assuming you have defined the Speak function somewhere else.
    click(x=35, y=26)
    sleep(2)
    click(x=126, y=22)
    
    write('camera')
    sleep(2)
    click(x=164, y=155)
      # Assuming you have defined the Speak function somewhere else.

# Assuming you want to call the camera function with a name as an argument.



