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
import turtle
import playsound
import pyttsx3
import subprocess
import sys , bs4
from urllib.parse import urlparse
import urllib.request
import urllib3
import selenium
from selenium import webdriver
import fbchat
from fbchat.models import *
from fbchat import Client
import tkinter as tk
import _thread
from turtle import *
import random
#Asistentul Snarky
   #by Zaharie Andrei
#==========================================================


'''Toate Drepturile de autor se rezerva lui ZAHA TECH INDUSTIES.
'''

#================================================================
iesire =0
   
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
        speak("Before we get started I will open my commands list for you.")
        subprocess.Popen(["notepad.exe", "Help.txt"])
        speak("Here are all my commands I hope you will find this note usefull ")
        
    f.close()
   

#Interfata grafica==============
N = 80
myList = [3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9]
t=random.choice(myList)
#Subprograme ce determina graficele unor functii matematice pt partea de loading
def f(x):
    global t
    return t*x*(1-x)

def g(x):
    global t
    return t*x-t*x*x

def h(x):
    return 3.9*(x-x**2)

def jumpto(x, y):
    penup(); goto(x,y)

def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)

def coosys():
    line(-1, 0, N+1, 0)
    line(0, -0.1, 0, 1.1)

def plot(fun, start, color):
    pencolor(color)
    x = start
    jumpto(0, x)
    pendown()
    dot(5)
    for i in range(N):
        x=fun(x)
        goto(i+1,x)
        dot(5)




#=====================
def interfata():
    colors = [ "red","purple","blue","green","orange","yellow"]
    pen = turtle.Pen()
   
    turtle.bgcolor("white")
    pen.penup()
    pen.backward(200)
    pen.pendown()
    turtle.hideturtle()
    pen.penup()
    turtle.write("Bot Assistant",
                 True,align="center",
                 font=("Courier",30,"bold"))
    pen.pendown()
    pen.pencolor("blue")
    pen.width(10)
    pen.forward(400)
    time.sleep(1)
    turtle.clearscreen()
    pen.pencolor("blue")
    pen.width(10)
    turtle.hideturtle()
    pen.penup()
    turtle.write("By Zaha Tech Industries",True,align="center",font=("Cornerstone",20))
    pen.pendown()
    pen.goto(-200,0)
    pen.goto(200,0)
    time.sleep(2)
    turtle.clearscreen()
    turtle.hideturtle()
    pen.penup()
     
    setworldcoordinates(-1.0,-0.1, N+1, 1.1)
    speed(0)
    turtle.write("Loading...",True,align="left",font=("Courier",30,"bold"))
    hideturtle()
    coosys()
    plot(f, 0.35, "blue")
    plot(f, 0.35, "green")
    #plot(h, 0.35, "red")
    turtle.clearscreen()
    turtle.write("Done",True,align="left",font=("Courier",30,"bold"))
    turtle.bye()

 #PREZENTARE ==============================
def inceput():
   f= open('recunoastere.txt','r')
   nume=f.readline()
   f.close()
   timp=datetime.datetime.now()
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

    driver = webdriver.Chrome('/Users/Dell/source/repos/Snarky2.0/chromedriver')
    driver.get("https://www.facebook.com/")
    driver.find_element_by_id('email').send_keys(user)
    driver.find_element_by_id('pass').send_keys(parola)
    time.sleep(1)
    driver.find_element_by_id('loginbutton').click()
    #driver.get("https://www.facebook.com/messages/t/10000717453743")
    

#LOGIN INCERCARE==========================
def login2(use,parola):
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
     }

    login_data = {
    'name': 'zaharie_andrei66@yahoo.com',
    'pass': '',
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
    
    
    speak('That is everything I found for'+ audio)


   
      #MAKE A NOTE ===========================================
def note(audio):
    
    date = 'note'
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(audio)

    subprocess.Popen(["notepad.exe", file_name])

     
#MODUL DE FACEBOOK=============================================================
def defemail():

    
       email=comandaA()
       speak("Is this the right email?")
       print('zaharie_andrei66'+'@yahoo.com');
       #x=comandaA()
       #return x



def facebok(url):

    speak('Are you logged in?')
    raspuns=comandaA()
    if 'no' in raspuns:
        
        speak("Do you want me log in for you?")
        ras=comandaA()
        if'yes' in ras:
               #webbrowser.close(url)
               speak("Can you tell me your email without the @yahoo.com part?")
               x=defemail()
               user= 'zaharie_andrei66'+'@yahoo.com'
               speak("now can you tell me your password?")
               parola=comandaR()
               login(user,parola)
               '''if 'yes' in x:
                      user= 'zaharie_andrei66'+'@yahoo.com'
                      speak("now can you tell me your password?")
                      parola=comandaR()
                      login(user,parola)


               elif'no' in x:
                      speak("Can you repeat if please")
                      email=comandaR()
                      speak("Is this the right email?")
                      print(email+'@yahoo.com');
                      x=comandaA()
                      if 'yes' in x:
                                 user= email+'@yahoo.com'
                                 speak("now can you tell me your password?")
                                 parola=comandaA()
                                 login(user,parola)
                      elif'no' in x:
        
                                 speak("I can't understand can you write it for me,please?")'''
        else:
            webbrowser.open(url)
            
    else:
        webbrowser.open(url)
        print('Done!')


#Final MODUL FACEBOOK==========================================================

#==========================MESAGERIE AUTOMATA FACEBOOK=========================

def mesagerie():

    
     #login('zaharie_andrei66@yahoo.com','')
     client1= Client('zaharie_andrei66@yahoo.com','Andreius2007')



     speak("Would you like to write to someone?")
     raspuns=comandaA()
     ''' if 'yes' in raspuns:
          speak('Tell me the name!')
          raspuns = comandaR()

     raspunsok=raspuns[0].upper()
     raspuns=raspuns[:0]+raspuns[1:]
     raspunsok=raspunsok+raspuns+ " "
     #raspuns = comandaR()

     raspunsok=raspunsok+raspuns[0].upper()
     raspuns=raspuns[:0]+raspuns[1:]
     h=""
     for i in range(0,len(raspuns)):
        if (raspuns[i] !=" "):
           h=h+raspuns[i]

     raspunsok=raspunsok+h
 
     x=client1.searchForUsers(raspunsok,2)
     print('\n')
     print(raspunsok)
     speak("I will search for this user")'''
     x=client1.searchForUsers("Marozsan Alex",2)
     print(x[0].uid)
     userid=x[0]
     speak('What massage do you want to send?')
     l=1
     while l!=0:
         mesaj = comandaR()
         if 'stop'!= mesaj:
            client1.send(fbchat.models.Message(mesaj),userid.uid)
         else: 
            l=0
           
   #client1.send(Message(text='mesaj'), thread_id=userid.uid, thread_type=ThreadType.USER)

     
     
   #=========================== Comanda vocala pentru asistent (Limba ENGLEZA) ===============================

def comandaA():
    
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
 
        comanda = r.recognize_google(audio).lower()
        print('You said: ' + comanda + '\n')

   #revenirea in loop in cazul in care comanda nu a fost recunoscută
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        comanda = comandaA()
    return comanda
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


   #+========================= Comanda vocala pentru asistent (Limba ROMANA) ======================================
def comandaR():
    "listens for commands"
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
 
        comanda = r.recognize_google(audio, language='ro-RO').lower()
        print('You said: ' + comanda + '\n')

    #revenirea in loop in cazul in care comanda nu a fost recunoscută
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        comanda = comandaA();

    return comanda

#================================ Interpretarea Comenzilor ========================================


def assistant(comanda):
    NOTE = ["make a note", "write this down", "remember this", "type this"]
  
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
    elif comanda in  NOTE:
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
                facebok(url)

            else:
               webbrowser.open(url)
               print('Done!')
        else:
            pass

    elif 'how are you' in comanda:
        speak("I am good how are you?")
    elif'how was your day'in comanda:
        timp=datetime.datetime.now()
        if timp.hour < 10:
                audio='Well i did nothing so far. I am not a morning person'
                speak(audio)
        elif timp.hour>=10 and timp.hour<18:
            audio='I woke up at 9 am and I helped some people, opened some browsers, basic stuffs'
            speak(audio)
            time.sleep(0.5)
            speak ("What about you? How was your day so far?")
        elif timp.hour>=19:
             audio='My day was really good and I did a lot of good things'
             speak(audio)
    elif 'i love you' in comanda:
        speak("Awww.I was not programmed to have feelings but I think I love you too!")
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
    elif 'message' in comanda:
         mesagerie()
    elif 'help page' in comanda:
        subprocess.Popen(["notepad.exe", "Help.txt"])
        speak("Here are all my commands I hope you will find this note usefull ")
#loop to continue executing multiple commands

    return 1

#faza de cunoastere si impretenire=====



#=========== Modul de Recunoastere pesoana (in caz ca aceasta este la prima folosire a programului)=======================
interfata()

cunoastere()
nume=inceput()

  
#SFARSIT faza=========

#============ Int main()=============
while iesire==0:
    
    assistant(comandaA())
   
if iesire ==1:
    speak('Before I exit, would you like me to remove your name form my database?')
    x=input('Write yes/ no: ')
    if x=='yes':
        uitare(nume)
    speak('I will close myself. Goodbye sir!')
    print('Program closed...')


