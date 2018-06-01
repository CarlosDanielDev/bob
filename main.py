#!/usr/bin/python3
#-*- coding: utf-8 -*-
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as s:
	r.adjust_for_ambient_noise(s)

	try:
		while True:
			audio = r.listen(s)
			speech = r.recognizer_google(audio, language='pt')
			print('Você Disse: ', speech)
	except:
		print('ERROR!')
