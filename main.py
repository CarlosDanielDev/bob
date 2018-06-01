#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr
import os
import pyttsx3

v = pyttsx3.init()

bot = ChatBot('Bob', read_only=True)

def voz(text):
    v.say(text)
    v.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    print('Bob: Diga Alguma Coisa!')
    try:
        while True:
            audio = r.listen(s)
            speech = r.recognize_google(audio, language='pt')
            response = bot.get_response(speech)
            print('Você Disse: ', speech)
            print('Bob: ', response)
            voz(response)
    except:
        voz('ERROR! Demorou Demais kkkkk Até a Próxima.')

#bot.set_trainer(ListTrainer)

#for _file in os.listdir('chats'):
#    lines = open('chats/' + _file, 'r').readlines()
#    bot.train(lines)

