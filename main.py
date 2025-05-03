import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import newsapi
recognizer = sr.Recognizer()
engine = pyttsx3.init()
nwsapi= newsapi.key

def speak(text):
    engine.say(text)
    engine.runAndWait()



    


if __name__ == "__main__":
    speak("Initializing Steve........")
    while True:

        #listen for the wake word jarvis

        r=sr.Recognizer()
        
        
        print("Recognizing........")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "steve"):
                speak("Yeah")
                #listen for command
                with sr.Microphone() as source:
                    print("steve active.....")
                    audio=r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))