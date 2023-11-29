from Customevoice.voice import Speak
import pyttsx3
from time import sleep
import speech_recognition as sr
# from Customevoice.voice import Speak




engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty("voices", voice[1].id)


def Speak(audio):
    print("")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source,0,15)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')  #en-in

        print(f": Your Command : {query}\n")

    except Exception as e:
        Speak(None)
        return ""

    return query.lower()



secure = (('s', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('1', '1'), ('.', ':'), ('z', '2'), ('u', 'n'), ('l', '7'), ('h', 'H'), ('k', 'K'), ('m', 'M'))
def securepassword(password):
    for a,b in secure:
        password = password.replace(a, b)
        
    return password


# if __name__ == '__main__':
#     while True:
#         Speak("Hello sir! How may i help you?")
#         query =TakeCommand().lower()
#         if "generate a password"  in query:
            
#             password = TakeCommand().lower()
#             password = securepassword(password)
#             Speak("Generating password...")
#             sleep(2)
#             Speak(f"Your Secure Password Is: {password}")
#             Speak("I hope this will help you sir!")

        
    
           