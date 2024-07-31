import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import pyttsx3
from config import apikey

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"User: {query}\nJarvis: "
    try:
        response = openai.Completion.create(
            model="gpt-4o-mini",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text = response["choices"][0]["text"]
        say(response_text)
        chatStr += f"{response_text}\n"
        return response_text
    except Exception as e:
        say("Sorry, I couldn't get a response from the AI.")
        print(f"Error: {e}")
        return ""

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response on the prompt: {prompt} \n***********************************\n"
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text = response["choices"][0]["text"]
        print(response_text)
        text += response_text
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    except Exception as e:
        say("Sorry, there was an error generating the AI response.")
        print(f"Error: {e}")

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "I didn't understand. Some error occurred, apologies from Jarvis!"

if __name__ == '__main__':
    print("Abeer ka JARVIS")
    say("I am Jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand()
        if "quit" in query.lower() or "exit" in query.lower():
            say("Goodbye!")
            break
        
        sites = [["YouTube", "https://www.youtube.com"], ["Wikipedia", "https://www.wikipedia.com"], ["Google", "https://www.google.com"], ["Instagram", "https://www.instagram.com"]]

        for site in sites:
            if f"open {site[0].lower()}" in query.lower():
                say(f"Opening {site[0]} ...")
                webbrowser.open(site[1])
                break

        if "open music" in query.lower():
            musicpath = "C:/Users/Abeer Fatima/OneDrive/Desktop/Let s Ask AI ding di.mp3"
            os.startfile(musicpath)

        elif "open my chatbot" in query.lower():
            chatbotpath = "https://mediafiles.botpress.cloud/da29c6d6-9585-4bdb-b2e5-56333df5837c/webchat/bot.html"
            webbrowser.open(chatbotpath)

        elif "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"The time is {hour} baj ke {min} minutes")
        
        elif "open da vinci" in query.lower():
            os.startfile("C:/Users/Abeer Fatima/OneDrive/Desktop/DaVinci Resolve.lnk")

        elif "using artificial intelligence" in query.lower():
            ai(prompt=query)

        elif "reset chat" in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)


'''import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import pyttsx3
from config import apikey


chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"User: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response on the prompt: {prompt} \n *********************************** \n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt= prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
# todo: Wrap this in a try catch, there may not be any choice sometimes
    print(response[choices][0]["text"])
    text += response[choices][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    #with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

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

        elif "Open My ChatBot".lower() in query.lower():
            chatbotpath = "https://mediafiles.botpress.cloud/da29c6d6-9585-4bdb-b2e5-56333df5837c/webchat/bot.html"
            os.startfile(chatbotpath)

        elif "the time" in query:
            #strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"The Time is {hour} baj ke {min} minutes ")
            break

        elif "open da vinci".lower() in query.lower(): #as we did with sites, we can give multiple location for apps and with the for loop we can do the similar thing here as well
            os.startfile(f"C:/Users/Abeer Fatima/OneDrive/Desktop/DaVinci Resolve.lnk")

        elif "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""


        #say(query)

        else:
            print("Chatting...")
            chat(query)'''






