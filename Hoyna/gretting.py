import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)





def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()

def get_random_greeting():
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
    return random.choice(greetings)

def how_are_you():
    how = [
        "I'm fine, thanks. What about you, sir?",
        "Everything is great, sir. How are you?",
        "Fine, sir! What are you doing?",
        "Not bad. How are you?",
        "I'm doing well, and you?",
    ]
    return random.choice(how)

def thanks_to():
    thanks = [
    "I'm really happy to hear from you, sir.",
    "It was my pleasure.",
    "I'm so glad you liked it!",
    "I'm so glad it was helpful!",
    "Anytime, sir!",
    "You're most welcome, sir!"
    ]
    return random.choice(thanks)

def introduce_self():
    introduce = [
    '''I'm Jarvis. Who is an advanced artificial intelligence designed and developed by Hakim,
    A genius inventor and the alter ego of Hakim.
    Created to serve as Hakim's personal assistant,Jarvis became an integral part of Hakim's life,
    assisting him with various tasks and projects.'''
    ]
    return random.choice(introduce)
    

# if __name__ == "__main__":
#     while True:
#         query = input("You: ").lower()
#         if "hi" in query or "hello jarvis" in query or 'hello' in query:
#             Speak(get_random_greeting())
            
#         elif 'how are you' in query or "what about you" in query or "how are you doing" in query:
#             Speak(how_are_you())
#         elif "thanks" in query or "thank you" in query or "thanks jarvis" in query:
#             Speak(thanks_to())
#         elif 'who are you' in query or "introduce your self" in query or "tell me about you" in query:
#             Speak(introduce_self())


            
            
