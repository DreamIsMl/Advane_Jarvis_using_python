import os
import pygame
voice7 ='ar-KW-NouraNeural'
voice6 = 'ar-EG-ShakirNeural'
voice5 = 'ar-EG-SalmaNeural'
voice4 = 'am-ET-MekdesNeural'
voice3 = 'sq-AL-AnilaNeural'
voice2 = 'af-ZA-WillemNeural'
voice1='en-GB-SoniaNeural'
def Speak(data, voice='en-US-SteffanNeural'):
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()

# Example usage:
Speak("Hello, this is a test message.")

        


    
