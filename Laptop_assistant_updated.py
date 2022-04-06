import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from requests import get
import smtplib



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id) #id=1 for girl and id= 0 for boys voices
engine.setProperty('voice', voices[1].id)

#text to speach
def speak(audio):
    '''This method works for speak what you want to speak'''
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#voice to text
def takecommand():
    '''It take microphone input and return string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining.......")
        r.pause_threshold=1 # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source,timeout=9,phrase_time_limit=9)
    try:
        print("Recogning......")
        quary=r.recognize_google(audio,language='en-in')
        print(f"User Said: {quary}\n")
    except Exception as e:
        print("Say again please...")
        return "None"
    return quary
#to wish
def wishMe():
    '''This method wish to the user good moring and wishes'''
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("Hello sir I am your ratan Please tell me how may i help you......")
#to send email
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rajn14964@gmail.com','9661376960')
    server.sendmail('rajn14964@gmail.com',to,content)
    server.close()



if __name__=='__main__':
    wishMe()
    while True:
    #if 1:
        quary = takecommand().lower()
        # performing task by using quary;
        if 'open code' in quary:
            srccode="C:\\Users\\NIRAJ\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(srccode)
            speak("opening opening code")
        elif 'open notepad' in quary:
            srccode="C:\\Windows\\system32\\notepad.exe"
            os.startfile(srccode)
            speak("opening notepad")
        elif 'open command prompt' in quary:
            os.system("start cmd")
            speak("opening cmd")
        elif 'play music' in quary:
            my_songs='E:\\python projects\\my song'
            songs=os.listdir(my_songs)
            #rd=random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(my_songs,song))

        elif 'IP Address' in quary:
            IP=get('https://api.ipify.org').text
            speak(f"your IP address is{IP}")

        elif 'wikipedia' in quary:
            speak("Searching wikipedia......")
            quary=quary.replace('wikipedia',"")
            results=wikipedia.summary(quary,sentences=10)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in quary:
            speak("sir what should i search on youtube")
            sear = takecommand().lower()
            webbrowser.open("{sear}")

        elif 'open google' in quary:
            speak("sir what should i search on google")
            sear=takecommand().lower()
            webbrowser.open("{sear}")

        elif 'open facebook' in quary:
            webbrowser.open("facebook.com")
            speak("opening facebook")
        elif 'open stack overflow' in quary:
            webbrowser.open("stackoverflow.com")

        elif 'time' in quary:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")

        elif 'send Email' in quary:
            try:
                speak('what should i say?')
                content=takecommand().lower()
                to='rajn14964@gmail.com'
                sendEmail(to,content)
                speak('email has been send to niraj')
            except Exception as e:
                print(e)
                speak('sorry sir can not send the email')

        elif 'stop' in quary:
            speak("thanks for your time have a good day sir!")
            exit()
        elif 'myself' in quary:
            speak("your full name is niraj raj from rothas bihar persuming master from iiita Allahabd")
