import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import time
import datetime
import requests
import mpg123
import winsound
import win32com.client as wincl
import playsound
import pyttsx3
import subprocess
from weather import Weather
import sys , bs4
from urllib.parse import urlparse
import urllib.request
import urllib3
import selenium
from selenium import webdriver
#Asistentul Snarky
   #by Zaharie Andrei
#==========================================================




# MODUL SPEAK ============================================
vocea=0
def speak(audio):
    "speaks audio passed as argument"
    global vocea
 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[vocea].id)
    print(audio)
    engine.say(audio)
    engine.runAndWait()
   
#Cunoastere persoana=============

def cunoastere():
    
    f= open('recunoastere.txt','r+')
    if os.path.getsize('recunoastere.txt')==0:
        speak('Hey are you new? How would you like me to call you?')
        x=input('Name: ')
        f.write(x)
    f.close()

       

 #PREZENTARE ==============================
def inceput():
   f= open('recunoastere.txt','r')
   nume=f.readline()
   f.close()
   timp=datetime.datetime.utcnow()
   if timp.hour < 10:
      audio='Good morning ' +nume+'! My name is Snarky and i will be your bot assistant.'
      speak(audio)
   elif timp.hour>=10 and timp.hour<19:
      audio='Hello '+nume +'! My name is Snarky and i will be your bot assistant.'
      speak(audio)
      time.sleep(0.5)
      speak('How was your day so far?')
   elif timp.hour>=19:
      audio='Good evening '+nume+'! My name is Snarky and i will be your bot assistant.'
      speak(audio)
   return nume
#RETINERE SAU UITARE PERSOANA=======

def uitare(nume):
    f= open('recunoastere.txt','r+')
    lines=f.readlines()
    f.seek(0)
    for line in lines:
        if line.strip("\n")!= nume:
          f.write(line)
    f.truncate()
    f.close()

# LOGARE AUTOMATA==========================

def login(user , parola):
    driver = webdriver.Chrome('Users/Dell/source/repos/Snarky2.1/Snarky2.1/chromedriver')
    driver.get("https://www.facebook.com/")
    driver.find_element_by_id('email').send_keys(user)
    driver.find_element_by_id('pass').send_keys(parola)
    time.sleep(1)
    driver.find_element_by_id('loginbutton').click()
    driver.find_element_by_class('_55lr').click()
    driver.find_element_by_data-id('100007174537439').send_keys('Sluut')

#LOGIN INCERCARE==========================
def login2(use,parola):
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
     }

    login_data = {
    'name': 'zaharie_andrei66@yahoo.com',
    'pass': 'Andreius2001',
    'form_id': 'new_login_form',
    'op': 'Login'
     }

    with requests.Session() as s:
         url = 'https://www.facebook.com/'
         r = s.get(url, headers=headers)
         soup = BeautifulSoup(r.content, 'html5lib')
         login_data['form_build_id'] = soup.find('input', attrs={'name': 'form_build_id'})['value']
         r = s.post(url, data=login_data, headers=headers)


#========================================================================================================

#CAUTARE AVANSATA ===================
def cautare_avansata(audio):
    
    res=requests.get('https://google.com/search?q='+ ''.join(audio))
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    linkElements = soup.select(' a')
    linkOpen=min(9, len(linkElements))
    for i in range(linkOpen):
       if i !=0 and i!=1 and i!=6:
         webbrowser.open('https://www.google.com'+linkElements[i].get('href'))
    
    
    speak('That is everithing I found for'+ audio)


   
      #MAKE A NOTE ===========================================
def note(audio):
    date = 'note'
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(audio)

    subprocess.Popen(["notepad.exe", file_name])

     
   #Comanda vocala pentru asistent===============================


def comandaA():
    "listens for commands"
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
 
        comanda = r.recognize_google(audio).lower()
        print('You said: ' + comanda + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        comanda = comandaA();

    return comanda


#comenzile ce le interpreteaza ========================================
iesire =0
NOTE = ["make a note", "write this down", "remember this", "type this"]
def assistant(comanda):
    "if statements for executing commands"
    
    if 'change your voice' in comanda:
           global vocea
           if vocea==1:
            vocea=0
            speak('I have changed my voice back, sir!')
           else:
            vocea=1
            speak('I have changed my voice for you')
           
    elif 'close' in comanda:
        global iesire
        iesire = 1
    elif 'make a note' in comanda:
          speak("What would you like me to write down? ")
          scrie = comandaA()
          note(scrie)
          speak("I've made a note of that.")
        
    elif 'open ' in comanda:
        reg_ex = re.search('open (.+)', comanda)

        if reg_ex:
         
            domain =reg_ex.group(1)
            url = 'https://www.'+domain +'.com'
            if 'facebook' in domain:
                speak('Are you logged in?')
                raspuns=comandaA()
                if 'no' in raspuns:
                    webbrowser.open(url)
                    speak("Do you want me log in for you?")
                    ras=comandaA()
                    if'yes' in ras:
                        webbrowser.close(url)
                        speak("Can you tell me your email without the @yahoo.com part?")
                        email=comandaA()
                        speak("Is this the right email?")
                        print('zaharie_andrei66'+'@yahoo.com');
                        x=comandaA()
                        if 'yes' in x:
                            user= 'zaharie_andrei66'+'@yahoo.com'
                            speak("now can you tell me your password?")
                            parola=comandaA()
                            login(user,parola)


                        else:
                            speak("Can you repeat if please")
                            email=comandaA()
                            speak("Is this the right email?")
                            print(email+'@yahoo.com');
                            x=comandaA()
                            if 'yes' in x:
                                 user= email+'@yahoo.com'
                                 speak("now can you tell me your password?")
                                 parola=comandaA()
                                 login(user,parola)
                            else:
                              speak("I can't understand can you write it for me,please?")

            else:
               webbrowser.open(url)
               print('Done!')
        else:
            pass

    elif 'how are you' in comanda:
        speak("I am good how are you?")
    elif 'joke' in comanda:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            speak(str(res.json()['joke']))
        else:
            speak('Hmmm Sorry sir I think I ran out of jokes.')

    elif 'search' in comanda:
         com = re.search('search (.+)', comanda)
         cautare= com.group(1)
         cautare_avansata(cautare)

#loop to continue executing multiple commands



#faza de cunoastere si impretenire=====

cunoastere()
nume=inceput()


#SFARSIT faza=========

login('zaharie_andrei66@yahoo.com','Andreius2001')
while iesire==0:
    assistant(comandaA())
if iesire ==1:
    speak('Before I exit woul you like me to remove your name form my database?')
    x=input('Write yes/ no: ')
    if x=='yes':
        uitare(nume)
    speak('I will close myself. Goodbye sir!')
    print('Program closed...')

