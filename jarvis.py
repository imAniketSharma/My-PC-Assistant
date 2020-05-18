import pyttsx3      #pyttsx3 is a text-to-speech conversion library in Python
import speech_recognition as sr
import datetime
import random
import wikipedia  
import requests     #news api package
import webbrowser   #simply calling the open() function from this module will do the right thing
import os           #The OS module provides a way of using operating system dependent functionality.
import smtplib      #The smtplib module defines an SMTP client session object that can be 
                    #used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import pyaudio
# PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. 
# With PyAudio, you can easily use Python to play and record audio on a variety of platforms

import json
# json = The json module provides an API similar to pickle for converting in-memory Python objects to a serialized representation 
# known as JavaScript Object Notation (JSON)
# is probably most widely used for communicating between the web server and client in an AJAX application, 
# but is not limited to that problem domain.


engine = pyttsx3.init('sapi5')  #Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    '''This is a function used by the jarvis to speak '''
    engine.say(audio)
    engine.setProperty('rate', 150) #makes the voice slower, default value is 200 words per minutes
    engine.runAndWait()


def wishMe():
    '''This function wish me according to the time  '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    '''This function takes microphone input from the user and returns string as output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:     #with block to open python files
        print("Listening...")
        r.energy_threshold = 300        #minimum audio energy to consider for recording
        r.pause_threshold = 1        #seconds of non-speaking audio before a phrase is considered completed
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e: 
        print("I'm sorry, please say again...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'E:\\My Music'
            songs = os.listdir(music_dir)
            # print(songs)    
            current = os.startfile(os.path.join(music_dir, songs[random.randint(0,251)]))
            
        elif 'play videos' in query:
            videos = 'E:\\Videos'
            songs = os.listdir(videos)
            # print(songs)
            os.startfile(os.path.join(
                videos, songs[random.randint(0, 26)]))
            
        if 'play news' in query:
            speak('searching news for today...')
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=yourapi "
            news = requests.get(url).text
            news_json = json.loads(news)
            print(news_json["articles"])
            article = news_json["articles"]
            speak("Breaking News")
            for articles in article:
            # in enumerate(news_json):
                speak(articles['title'])
                speak("Moving on to the next...")
            speak("thanks for listening times of india")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to aniket' in query:
            try:
                
                speak("What should I say?")
                content = takeCommand()
                # speak("Whom this email is to send?")
                # to = takeCommand()
                to = "email@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry aniket bhai. I am not able to send this email")   
        
        elif 'open notepad' in query:
            os.system('notepad.exe')

        elif 'open calculator' in query:
            os.system('calculator.exe')

        elif 'open amazon music' in query:
            os.system('C:\\Users\\abc\\AppData\\Local\\Amazon Music')
