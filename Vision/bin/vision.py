import os
import pyttsx3 as spk
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import keyboard
import multiprocessing

def greet():
	hour = int(datetime.datetime.now().hour)

	if hour>=0 and hour<12:
	   spk.speak("Good morning Sir...")
	elif hour>=12 and hour<17:
	   spk.speak("Good Afternoon sir...")
	else :
	   spk.speak("Good Evening Sir ")
    

def launchApp(app):	
	spk.speak("Launching " + app)
	exit_stat = os.system(app)
	if not exit_stat :
		spk.speak(app + " launched successfully....")
	else: 
		spk.speak("Sorry sir , Something is wrong! Try again")
		print("Something is wrong! Try again")

def vision_body():
	while 'True':
		try:
			greet()
			spk.speak("Vision at your service...What can i do for you sir ?")
			r = sr.Recognizer()
			mic = sr.Microphone()
			with mic as source:
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
			inst = r.recognize_google(audio)
			if inst == "exit":
				spk.speak("Good bye sir..have a nice day...")
				exit()
			launchApp(inst)
		except:
			spk.speak("Sorry sir, i can not understand what you are saying.")

def sayonara():
	y = multiprocessing.Process(target=vision_body, args=())
	y.start()
	while True:
	    if keyboard.read_key() == "q":
	        ans = input("Do you really want to quit ? (yes/no) ")
	        if 'yes' in ans:
	        	spk.speak("Good bye sir..have a nice day...")
	        	y.terminate()
	        	exit()

#vision_body()

	
		