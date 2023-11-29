import requests
import pyttsx3
from PIL import Image
import os
from Customevoice.voice import Speak

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[1].id)


# def Speak(audio):
#     print(" ")
#     print(f": {audio}")
#     engine.say(audio)
#     engine.runAndWait()


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



if __name__ == '__main__':
    while True:
        query = input("Enter: ")
        if 'space news' in query or "NASA news" in query or "news of nasa" in query:
            Speak("Tell Me The Date For News Extracting Process .")
            Date = input().strip()  # Changed from input.lower() to input().strip()
            from Features import DateConverter
            Value = DateConverter(Date)
            # from Nasanews import NasaNews
            NasaNews(Value)
