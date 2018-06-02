#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from pocketsphinx import pocketsphinx, Jsgf, FsgModel
import speech_recognition as sr
import os
import pyttsx3
import traceback

#CRIANDO UM DECODIFICADOR DE OBJETO

config = pocketsphinx.Decoder.default_config()
config.set_string("-hmm", 'model')
config.set_string("-lm", 'model.lm.bin')
config.set_string("-dict", 'model.dic')
config.set_string("-logfn", os.devnull)
decoder = pocketsphinx.Decoder(config)
#print('Tudo Certo até aqui :)')

def recognize_pt(audio):
    raw_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
    decoder.start_utt()
    decoder.process_raw(raw_data, False, True)
    decoder.end_utt()
    hypothesis = decoder.hyp()
    if hypothesis is not None:
        return hypothesis.hypstr
    return None


v = pyttsx3.init()
#print('pyttsx3 Iniciado :)')

bot = ChatBot('Bob', read_only=True)

def voz(text):
    v.say(text)
    v.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    print('Diga Alguma Coisa!')
    try:
        while True:
            audio = r.listen(s)
            speech = recognize_pt(audio)
            response = bot.get_response(speech)
            print('Você Disse: ', speech)
            print('Bob: ', response)
            voz(response)
    except:
        trace = traceback.format_exc()
        voz('Erro.')
    finally:
        print(trace)

# bot.set_trainer(ListTrainer)

# for _file in os.listdir('chats'):
#    lines = open('chats/' + _file, 'r').readlines()
#    bot.train(lines)
