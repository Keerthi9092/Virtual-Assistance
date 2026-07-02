#Virtual Assistance
#Google Text to Speech

#pip install gtts
#pip install speechrecognition
#pip install playsound==1.2.2
#pip install pyaudio

from gtts import gTTS
import speech_recognition as sr
import playsound
from time import ctime
import os
import uuid
import smtplib
import webbrowser

#to make sure it listens
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking")
        audio = r.listen(source,pharse_time_limit=5)
    data = ""
    #Exception Handling
    try:
        data = r.recognize_google(audio, language= 'en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot heat you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
listen()

#To respond back with audio
def respond(String):
    print(String)
    tts = gTTS(text = String, lang='en-US')
    tts.save("speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
#respond('Hey codegnan how are you')
#start giving action
#Virtual Assistance actions
def virtual_assistant(data):
    """give your actions"""
    if "how are you" in data:
        listening = True
        respond("Good and doing well")
    if "time" in data:
        listening = True
        respond(ctime())

    if "open google" in data.casefold():
        listening = True
        url = "https://www.google.com/"
        webbrowser.open(url)
        respond("Success")
    if "locate" in data:
        webbrowser.open('https://www.google.com/maps/search/'+data.replace("locate",""))
        result = "Locate"
        respond("Located {}".format(data.replace("locate","")))
    if "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen().lower()
        edict = {'user_name':'usergmail@gmail.com'}#give mail id's
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("Waht should i tell that person?")
        message = listen()
        content = 'Subject :{}\n\n{}'.format(subject,message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)
        #identify the server
        mail.ehlo()
        mail.starttls()
        #login
        mail.login('user@gmail.com','ensb ilkt ewtz lput')#App Password
        mail.sendmail('user@gmail.com',toaddr,content)#ent
        mail.close()
        respond('Email Sent')
    if 'stop' in data:
        listening = False
        print("Listening Stopped")
        respond("Okay done take care...")
    try:
        return listening
    except UnboundLocalError:
        print("Timedout")
respond = ("Hey user how are you")
listening = True
while listening == True:
    data = listen()
    listening = virtual_assistant(data)

