import speech_recognition as sr
import os
import webbrowser
import openai
import datetime

import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.5 Here you can change the time till which it listens to you, by deafult it is 0.8 so we are commenting this line out for now
        audio = r.listen(source)
        try:
            print ("Recognizing...")
            query = r.recognize_google(audio, language= 'en-in')
            print (f"User said: {query}")
            return query
        except Exception as e:
            return "I didn't understand, Some Error Occured, Apologies from Jarvis!"

if __name__ == '__main__':
    print("Abeer ka JARVIS")
    say("Assalamualaikum, I am Jarvis A I")
    while True:
        print ("Listening...")
        query = takeCommand()
        sites = [["YouTube", "https://www.youtube.com"], ["Wikipedia", "https://www.wikipedia.com"],["Google", "https://www.google.com"], ["Instagram", "https://www.instagram.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} ...")
                webbrowser.open(site[1])

        if "Open Music".lower() in query.lower():
            musicpath = "C:/Users/Abeer Fatima/OneDrive/Desktop/Let s Ask AI ding di.mp3"
            os.startfile(musicpath)
            #os.system(f"open {musicpath}") (This line of code works for macOS)

        if "the time" in query:
            #strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"The Time is {hour} baj ke {min} minutes ")
            break

        if "open da vinci".lower() in query.lower(): #as we did with sites, we can give multiple location for apps and with the for loop we can do the similar thing here as well
            os.startfile(f"C:/Users/Abeer Fatima/OneDrive/Desktop/DaVinci Resolve.lnk")