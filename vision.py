import os
import pyttsx3 as spk
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr

hour = int(datetime.datetime.now().hour)

if hour>=0 and hour<12:
   spk.speak("Good morning Sir...")
elif hour>=12 and hour<18:
   spk.speak("Good Afternoon sir...")
else :
   spk.speak("Good Evening Sir ")

spk.speak("Vision at your service...What can i do for you ?")
    

def launchApp(app):
	if app == 'exit' :
		spk.speak("Good bye sir..have a nice day...")
		exit()
	spk.speak("Launching " + app)
	exit_stat = os.system(app)
	if not exit_stat :
		spk.speak(app + " launched successfully....")
	else: 
		spk.speak("Sorry sir , Something is wrong! Try again")
		print("Something is wrong! Try again")


while True:
	spk.speak("What can i do for you sir..?")
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	inst = r.recognize_google(audio)
	launchApp(inst)
		