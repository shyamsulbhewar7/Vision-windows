import os
import pyttsx3 as spk
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr

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


while True:
	try:
		spk.speak("Vision at your service...What can i do for you sir ?")
		r = sr.Recognizer()
		mic = sr.Microphone()
		with mic as source:
			r.adjust_for_ambient_noise(source, duration=0.8)
			audio = r.listen(source)
		inst = r.recognize_google(audio)
		if inst == "exit":
			spk.speak("Good bye sir..have a nice day...")
			break
			exit()
		launchApp(inst)
	except:
		spk.speak("Sorry sir, i can not understand what you are saying.")

	
		