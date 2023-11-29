from datetime import datetime
import pyttsx3
# from Customevoice.voice import Speak

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

FiveTo6 = '''
In This Time , 
You Have To Get Up & Listen Somethintg Positive .
5:00 Am To 6:00 Am 
Thanks.
'''

SixTo9 = '''
In This Time , 
You Have To Study .
6:00 Am To 9:00 Am .
Thanks .
'''

NineTo12 = '''
In This Time ,
You Have To Learn Sql Database for learning Machine Learnong .
9:00 Am To 12:00 Pm .
Thanks .
'''

TwelveTo13 = '''
In This Time ,
You Have To You Have To Take Launch And Prepare For Your Campus .
12:00 Pm To 1:00 Pm .
Thanks .
'''

ThirteenTo19 = '''
In This Time ,
You Have To Stay Focus In Your Class .
3:00 Pm To 7:00 Pm .
Thanks .
'''

NineteenTo23 = '''
In This Time ,
You Have To coading .
7:00 Pm To 11:00 Pm .
Thanks .
'''

def Time():

    hour = int(datetime.now().strftime("%H"))

    if hour>=5 and hour<6:
        Speak(FiveTo6)
        return FiveTo6
        
    elif hour>=6 and hour<9:
        Speak
        (SixTo9)
        return SixTo9

    elif hour>=9 and hour<12:
        Speak(NineTo12)
        return NineTo12

    elif hour>=12 and hour<13:
        Speak(TwelveTo13)
        return TwelveTo13

    elif hour>=13 and hour<19:
        Speak(ThirteenTo19)
        return ThirteenTo19

    elif hour>=19 and hour<23:
        Speak(NineteenTo23)
        return NineteenTo23
        
    else:
        Speak("In This Time , You Have To Sleep ")

        return '''In This Time , You Have To Sleep .'''
