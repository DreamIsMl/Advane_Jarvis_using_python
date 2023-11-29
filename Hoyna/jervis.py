import pyttsx3
# from Brain.AIBrain import ReplyBrain

from Automation.Automations import Notepad
# from gretting import get_random_greeting
from gretting import how_are_you
from gretting import thanks_to
# from sound import change_volume

from gretting import introduce_self 
# from pyautogui import hotkey
from password import securepassword

import os
import random
from Automation.Automations import MessangerMsg
# from Customevoice.voice import Speak
# from googletrans import Translator 
# import speech_recognition as sr
import datetime
import cv2
from pyautogui import click
from keyboard import write
from time import sleep
import random
import wikipedia
from requests import get
import smtplib
from PIL import Image
import webbrowser
# import pywhatkit as kit
from keyboard import press
from keyboard import press_and_release
# import webbrowser as web
import sys
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)





def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    
#  
    
def TakeCommand():
    f = input("Your Command")
    

    # r = sr.Recognizer()

    # with sr.Microphone() as source:

    #     print(": Listening....")

    #     r.pause_threshold = 1

    #     audio = r.listen(source,0,20)


    # try:

    #     print(": Recognizing...")

    #     query = r.recognize_google(audio,language='en-in')  #en-in

    #     print(f": Your Command : {query}\n")

    # except Exception as e:
    #     Speak(None)
    #     return ""

    # return query.lower()

# def TranslationBnToEng(Text):
#     try:
        
    
#         line = str(Text)
#         translate = Translator()
#         result = translate.translate(line)
#         data = result.text
#         line = str(Text)
#         print(f"You : {data}.")
#         return data
#     except Exception as e:
#         print(e)
#         return ""

# def TakeCommand():
#     query = takeCommand()
#     data = TranslationBnToEng(query)
#     return data

Api_Key = "KrsOGOZLgYGcxYVBLZld2U65PevfTyOfbdqy7ggK"


def NasaNews(Date):
    try:
        Speak("Extracting Data From Nasa . ")
        Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
        Params = {'date': str(Date)}
        r = requests.get(Url, params=Params)
        r.raise_for_status()  # Raise an exception if there's an error with the request
        Data = r.json()
        Info = Data['explanation']
        Title = Data['title']
        Image_Url = Data['url']
        Image_r = requests.get(Image_Url)
        Image_r.raise_for_status()  # Raise an exception if there's an error with the image request
        FileName = str(Date) + '.jpg'
        with open(FileName, 'wb') as f:
            f.write(Image_r.content)
        Path_1 = "F:\\Hoyna\\" + str(FileName)
        Path_2 = "F:\\Hoyna\\Nasadata\\" + str(FileName)
        os.rename(Path_1, Path_2)
        img = Image.open(Path_2)
        img.show()
        Speak(f"Title : {Title}")
        Speak(f"According To Nasa : {Info}")
    except requests.exceptions.HTTPError as e:
        Speak("Sorry! please tell me the correct date and time")
    except requests.exceptions.RequestException as e:
        Speak("Sorry! please tell me the correct date and time")
    except KeyError as e:
        Speak("Sorry! please tell me the correct date and time")
    except Exception as e:
        Speak("Sorry! please tell me the correct date and time")
        print(e)






def respond_to_greeting():
    greetings = [
        "Hello there!",
        "Hi, how can I assist you?",
        "Hey, what's up?",
        "Greetings, my friend!",
        "Hey there! How's it going?",
        "Hi! What can I do for you?",
        "I can hear you, sir!",
        "Aye! How can I assist you?",
        "Hello! How may I help you?",
        "Hey! What's on your mind?",
    ]
    
    Speak(random.choice(greetings))
    




def wish():
    
    
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<=6:
         Speak("it's Midnight sir! you have to sleep!")
         Speak("Have you any important work?")
         l = TakeCommand().lower()
         if "yes" in l or "yeah" in l or "i have" in l:
             Speak("Ok sir! finish your work as soon as possible. You need to sleep properly for stay health")
         elif 'no' in l:
             Speak("Then Why you are here sir? It's my duty to take care your self. I'm going out of here. see you next time!")
             sys.exit()
         else:
             Speak("You Might Have Not Any Work. I'm Going To Sleep!")
             sys.exit()
                        
    
    elif hour>=6 and hour<12:
        Speak("Good Morning sir!")
    elif hour>12 and hour<18:
         Speak("Good Afternoon")
    else:
         Speak("Good Evening")
    k = (
        "Welcome back sir! how i assit you?",
        "Hello! Nice To Meet You Again",
        "I'm Jarvis Sir! How May I Assits You?",
    )
        
    
    Speak(random.choices(k))

    
    
def Pass(pass_inp):

       password = "Nooneknows"

       passss  = str(password)

       if passss==str(pass_inp):

              Speak("Access Granted .")

              

       else:
              Speak("Access Not Granted .")
    
              sys.exit()





           



if __name__ =='__main__':
    # Speak("Hello")
    Speak("This Particular File Is Password Protected .")

    Speak("Kindly Provide The Password To Access .")

    passssssss = input("Enter The Password: ")

    Pass(passssssss)
    Speak("Intializing The System...")
    
    sleep(5)

    # Pass()
    wish()
    while True:
        query = TakeCommand()
        
        #Logic building
        if 'space news' in query or "NASA news" in query or "news of nasa" in query:
            Speak("Tell Me The Date For News Extracting Process .")
            Date = TakeCommand().strip()  # Changed from input.lower() to input().strip()
            from Features import DateConverter
            Value = DateConverter(Date)
            # from Nasanews import NasaNews
            NasaNews(Value)
        
        
        
        
        
        
        elif "open notepad" in query:
            npath = 'C:\\WINDOWS\\system32\\notepad.exe'
            Speak("Intializing Notepad...")
            sleep(1)
            Speak("Notepad Has Been Open Sir!")
        
            
        elif 'write a note' in query:

            Speak("Preparing Notepad For Write A Note Sir!")
            sleep(2)

            Notepad()
       
            
        elif "generate password" in query or "generate me a password" in query:
            Speak('Tell me the password which you want')
            
            password = TakeCommand().lower()
            Speak("Generating your password...")
            password = securepassword(password) 
            Speak(f"Your password is: {password}")
            Speak("I hope this password will help you sir!")       
            
        elif "close notepad" in query:
            
            click(x=828, y=384)   
        
        elif 'in this time' in query:

            from test import TimeTable

            TimeTable()
        elif 'download' in query:
            from Features import DownloadYouTube
            Speak("As Your Wish sir!")
            DownloadYouTube()
            
            
        elif 'send message' in query:

            name = query.replace("messanger message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            
            Speak(f"Whats The Message For")
            Name = TakeCommand().lower()
            Speak(f"And Whats the message")
            
            MSG = TakeCommand().lower()
            
            MessangerMsg(Name,MSG)
            
            
            
        elif "open cmd" in query:
            cpath = 'C:\\WINDOWS\\system32\\cmd.exe'
            Speak("Checking")
            os.startfile(cpath)
            Speak("Command Promt is Runinng sir!")
            
        elif "open chorme" in query or "open browser" in query or 'open webbrowser' in query:
            Speak("launching browser sir")
            os.startfile('"C:\\Users\\Ghost Codm\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"')   
            
        
            
        elif "make it full screen" in query: #youtube
            Speak("ok")
            click(x=1276, y=60)
            
        elif "play music" in query or "i feel boring" in query:
            Speak("Preparing system for music")
            music_dir = "F:\\class\\Artwork"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            
            Speak('enjoy sir!')
            
        elif 'play a movie' in query:
            Speak("preparing sir!")
            video_dir = "E:\\NCS\\New folder"    
            videos = os.listdir(video_dir)
            rd = random.choice(videos)
            os.startfile(os.path.join(video_dir,rd))
            sleep(2)
            Speak('Enjoy sir')
            
        
            
        elif "i don't like this music" in query or 'change this music' in query or 'next music' in query or 'Change music' in query:
            Speak("As Your Wish Sir!")
            click(x=918, y=371)
        elif "previous music" in query or "play previous music" in query or "last music" in query:
            Speak('I am really happy that you have enjoied the last music')
            click(x=847, y=380)
      
        
       
        
        
        elif 'ip address' in query:
            Speak("Checking ip adress sir!")
            ip = get("https://api.ipify.org").text
            Speak(f"Your ip address is {ip}")
            
        elif 'wikipedia' in query:
            Speak('Searching Wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 2) 
            Speak("according to wikipedia")
            Speak(results)
            print(results)
        
        elif "open youtube" in query:
            Speak("preparing...")
            webbrowser.open('www.youtube.com')
            Speak("youtube is open now!")
            
        elif "open facebook" in query:
            Speak("preparing...")
            webbrowser.open('www.facebook.com')
            Speak("facebook is open now!")
        elif "open whatsapp" in query:
            Speak("preparing...")
            webbrowser.open('https://web.whatsapp.com/')
            Speak("whatsapp is open now!")
            
        elif "open youtube" in query:
            Speak("preparing...")
            webbrowser.open('www.youtube.com')
            Speak("youtube is open now!")
        
        elif "open google" in query:
            Speak("sir! what should i search on google?")
            cm= TakeCommand().lower()
            webbrowser.open(f"{cm}")
            
        
            
            
        elif "search in youtube" in query or "youtube search" in query:
            from Features import jarvis
            jarvis()
            
            
            
        
            
        
        elif 'new tab' in query:

            press_and_release('ctrl + t')

        elif 'close tab' in query or " closed tab":

            press_and_release('ctrl + w')

        

        elif 'open history' in query:

            press_and_release('ctrl + h')

        elif 'open download' in query:

            press_and_release('ctrl + j')
            

        elif 'bookmark' in query:

            press_and_release('ctrl + d')

            press('enter')

        elif 'incognito' in query:

            press_and_release('Ctrl + Shift + n')

        elif 'switch tab' in query:

            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to","")
        
            num = Tab

            bb = f'ctrl + {num}'

            press_and_release(bb)


        # 
        elif 'pause' in query:

            press('space bar')

        elif 'resume' in query:

            press('space bar')
            
        elif "what's the time" in query or "tell me time":
            now = datetime.datetime.now()
            Speak ("Current date and time : ")
                
            Speak (now.strftime("%Y-%m-%d %H:%M:%S"))

        elif 'full screen' in query:

            press('f')

        elif 'film screen' in query:

            press('t')

        elif 'skip' in query:

            press('l')

        elif 'back' in query:

            press('j')

        elif 'increase' in query:

            press_and_release('SHIFT + .')

        elif 'decrease' in query:

            press_and_release('SHIFT + .')

        elif 'previous' in query:

            press_and_release('SHIFT + p')

        elif 'next' in query:

            press_and_release('SHIFT + n')
    
        elif 'search' in query:

            click(x=668, y=166)

            Speak("What To Search Sir ?")

            search = TakeCommand()

            write(search)

            sleep(4)

            press('enter')
            Speak("I have Found This result form your command sir!")
        elif "play one" in query:
            Speak("As Your Wish Sir!")
            click(x=512, y=346)
            
        elif "play second" in query:
            Speak("Sure Sir!")
            click(x=496, y=502)
            
            
                
        elif "Play third" in query:
            click(x=489, y=646)
            
            
                
            

        elif 'mute' in query:

            press('m')

        elif 'unmute' in query:
            press('m')
            
       
        elif "shutdown the system" in query or "shut down the system" in query or " shutdown system" in query:
            Speak("Ok sir! Shuting Down The System!") 
            sys.exit()
        
        
        elif 'how are you' in query or "what about you" in query or "how are you doing" in query:
            Speak(how_are_you())
        elif "thanks" in query or "thank you" in query or "thanks jarvis" in query:
            Speak(thanks_to())
        elif 'who are you' in query or "introduce yourself" in query or "tell me about you" in query:
            Speak(introduce_self())
            
            
        elif "hi" in query or "hello jarvis" in query or "hello" in query:
            respond_to_greeting(query)
            
        
        
            
                
     
            
        else:
            Speak("that's avobe me")     
        
                