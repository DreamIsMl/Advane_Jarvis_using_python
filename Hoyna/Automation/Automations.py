from os import startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pyttsx3
import speech_recognition as sr
# from TimeTable import Time
import os
# import pygame

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
# speak

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    
def TakeCommand():
        
    

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source,0,5)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')  #en-in

        print(f": Your Command : {query}\n")

    except Exception as e:
        Speak(None)
        return ""

    return query.lower()

# voice2 = 'en-GB-SoniaNeural'
# def Speak(data):
#     voice = 'en-US-SteffanNeural'
#     command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
#     os.system(command)

#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load("data.mp3")

#     try:
#         pygame.mixer.music.play()

#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)

#     except Exception as e:
#         print(None)
#     finally:
#         pygame.mixer.music.stop()
#         pygame.mixer.quit()

def MessangerMsg(name,message):
     
    startfile("C:\\Users\\Ghost Codm\\AppData\\Local\\Programs\\Messenger\\Messenger.exe")

    sleep(8)

    click(x=441, y=148)

    sleep(1)

    write(name)

    sleep(4)

    click(x=399, y=208)

    sleep(1)

    click(x=762, y=741)

    sleep(1)

    write(message)

    press('enter')
    Speak("Message Has Been Sent!")
    

import os
import os
from datetime import datetime
from time import sleep

# Assuming you have defined the Speak and TakeCommand functions somewhere else.

def Notepad():
    Speak("Please tell me what name should I set for this note?")
    m =TakeCommand().lower()

    Speak("Tell me the note.")
    Speak("I am ready to write, sir!")

    writes = TakeCommand().lower()

    time = datetime.now().strftime("%H-%M-%S")
    filename = str(m).replace(" ", "_") + f"_{time}-note.txt"

    try:
        with open(filename, "w") as file:
            file.write(writes)
    except Exception as e:
        Speak("I'm sorry, there was an error while saving the note.")
        print(f"Error: {e}")
        return

    path_1 = "F:\\Hoyna\\" + str(filename)
    path_2 = "F:\\Hoyna\\Note\\" + str(filename)

    try:
        os.rename(path_1, path_2)
    except Exception as e:
        Speak("Please wait a minute, sir. I can't write a note at the same time.")
        # print(f"Error: {e}")
        return

    try:
        os.startfile(path_2)
        sleep(2)
        Speak("It's done, sir!")
    except Exception as e:
        Speak("I'm sorry, there was an error while opening the file.")
        print(f"Error: {e}")
        return

# Assuming you have defined the Speak function and the TakeCommand function properly.



    

    
