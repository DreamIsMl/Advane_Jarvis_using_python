# from TimeTable import Time
# import pyttsx3
# import random
# # from Customevoice.voice import Speak

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voices',voices[1].id)
# def Speak(audio):
#     print(" ")
#     print(f": {audio}")
#     engine.say(audio)
#     engine.runAndWait()
# def TimeTable():

#     Speak("Checking....")

    

#     value = Time()

   

#     Speak("AnyThing Else Sir ??")
query = input().lower()

if "remember that" in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("jarvis","")
            print("You tell me to remaind you that: " + rememberMsg)
            remeber = open("F:\\Hoyna\\Remember\\data.txt", 'w')
            remeber.write(rememberMsg)
            remeber.close()
        
elif "what do you remember" in query:
            remeber = open("F:\\Hoyna\\Remember\\data.txt",'r') 
            print("You tell me that" + remeber.read())








         