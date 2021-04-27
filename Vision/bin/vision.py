import os
import pyttsx3 as spk
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import keyboard
import multiprocessing
import sys
from translate_change_lang import *
voicess=["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM"]
d = {'name':"Vision",
'en_voice_id':voicess[0],
'lang':'en'}

def greet():
	global sayonara
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
	   spk.speak("Good morning Sir...")
	   sayonara = "Good bye sir..have a nice day..."
	elif hour>=12 and hour<17:
	   spk.speak("Good Afternoon sir...")
	   sayonara = "Good bye sir...see you again later.."
	else :
	   spk.speak("Good Evening Sir ")
	   sayonara = "Good night sir..have sweet dreams..!"
def vision_body(name,voice,lang):
	global engine
	engine = spk.init()
	engine.setProperty('voice', voice)
	while 'True':
		try:
			if lang!='en':
				spk.speak(translate_text(name + "at your service...What can i do for you sir ?",lang))
			else:
				spk.speak(name + "at your service...What can i do for you sir ?")
			r = sr.Recognizer()
			mic = sr.Microphone()
			with mic as source:
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
			inst = r.recognize_google(audio)
			if inst == "exit":
				spk.speak(sayonara)
				break
			else:
				if lang!='en':
					spk.speak(translate_text("Launching " + inst,lang))
				else:
					spk.speak("Launching " + inst)
				os.system("python C:\\Users\\POOJA\\Desktop\\Vision\\Vision-windows\\Vision\\bin\\set_path.py" + " " + inst)
		except:
			if lang!='en':
				spk.speak(translate_text("Sorry sir, i can not understand what you are saying.",lang))
			else:
				spk.speak("Sorry sir, i can not understand what you are saying.")
def Key_Controls():
	greet()
	global y
	global d
	y = multiprocessing.Process(target=vision_body, args=(d['name'],d['en_voice_id'],d['lang']))
	y.start()
	while True:
	    if keyboard.read_key() == "q":
	        ans = input("Do you really want to quit ? (yes/no) ")
	        if 'yes' in ans:
	        	spk.speak(sayonara)
	        	y.terminate()
	        	sys.exit()
	    if keyboard.read_key() == "v":
	    	y.terminate()
	    	if d['name'] == 'Vision' and 'EN-US' in d['en_voice_id']:
	    		d['en_voice_id'] = voicess[1]
	    		d['name'] = "Wanda"
	    	elif d['name'] == 'Wanda' and 'EN-US' in d['en_voice_id']:
	    		d['en_voice_id'] = voicess[0]
	    		d['name'] = "Vision"
	    	elif d['name'] == 'Wanda' and 'hiIN' in d['en_voice_id']:
	    		d['en_voice_id'] = voicess[2]
	    		d['name'] = "Vision"
	    	elif d['name'] == 'Vision' and 'hiIN' in d['en_voice_id']:
	    		d['en_voice_id'] = voicess[3]
	    		d['name'] = "Wanda"
	    	y = multiprocessing.Process(target=vision_body, args=(d['name'],d['en_voice_id'],d['lang']))
	    	y.start()
	    if keyboard.read_key() == "l":
	    	y.terminate()
	    	if d['lang']=='en':
	    		d=change_lang('Hindi')
	    	else:
	    		d=change_lang('English')
	    	y = multiprocessing.Process(target=vision_body, args=(d['name'],d['en_voice_id'],d['lang']))
	    	y.start()