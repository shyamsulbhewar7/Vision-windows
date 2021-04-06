import os
import pyttsx3 as spk
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import keyboard
import multiprocessing
import sys

d = {'name':"Vision",
'en_voice_id':"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"}

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
    
def launchApp(app):	
	spk.speak("Launching " + app)
	exit_stat = os.system(app)
	if not exit_stat :
		spk.speak(app + " launched successfully....")
	else: 
		spk.speak("Sorry sir , Something is wrong! Try again")
		print("Something is wrong! Try again")

def vision_body(name,voice):
	global engine
	engine = spk.init()
	engine.setProperty('voice', voice)
	while 'True':
		try:
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
				sys.exit()
			else:
				launchApp(inst)
		except:
			spk.speak("Sorry sir, i can not understand what you are saying.")

def Key_Controls():
	greet()
	global y
	y = multiprocessing.Process(target=vision_body, args=(d['name'],d['en_voice_id'],))
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
	    	if d['name'] == 'Vision':
	    		d['en_voice_id'] = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
	    		d['name'] = "Wanda"
	    	else:
	    		d['en_voice_id'] = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
	    		d['name'] = "Vision"
	    	y = multiprocessing.Process(target=vision_body, args=(d['name'],d['en_voice_id'],))
	    	y.start()