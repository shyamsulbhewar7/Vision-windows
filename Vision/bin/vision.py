import os
import pyttsx3 as spk
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import keyboard
import multiprocessing
import sys
import chatbot as cb

class Chat_Bot(object):
	def greet(self):
		hour = int(datetime.datetime.now().hour)
		if hour>=0 and hour<12:
		   spk.speak("Good morning Sir...")
		elif hour>=12 and hour<17:
		   spk.speak("Good Afternoon sir...")
		else :
		   spk.speak("Good Evening Sir ")
	    		
	def vision_body(self,name,voice):
		global engine
		engine = spk.init()
		engine.setProperty('voice', voice)
		self.greet()
		while 'True':
			try:
				spk.speak(name + "at your service...What can i do for you sir ?")
				r = sr.Recognizer()
				mic = sr.Microphone()
				with mic as source:
					r.adjust_for_ambient_noise(source)
					audio = r.listen(source)
				inst = r.recognize_google(audio)
				exit_stat = cb.run(inst)
				if exit_stat:
					cnt.stop_vision()
					
			except:
				spk.speak("Sorry sir, i can not understand what you are saying.")

class Controls(Chat_Bot):

	voices = [
	"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
	"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
	"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM",
	"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM"
	]


	d = {
	'name':"Vision",
	'en_voice_id':voices[0],
	'lang':'en'
	}

	bot = Chat_Bot()

	y = multiprocessing.Process(target=bot.vision_body, args=(d['name'],d['en_voice_id'],))
	
	def stop_vision(self):
		spk.speak("Terminating....")
		self.y.terminate()
		sys.exit()

	def Key_Controls(self):
		self.y.start()
		while True:
		    if keyboard.read_key() == "q":
		        ans = input("Do you really want to quit ? (yes/no) ")
		        if 'yes' in ans:
		        	self.stop_vision()

		    if keyboard.read_key() == "v":
		    	self.y.terminate()
		    	if self.d['name'] == 'Vision':
		    		self.d['en_voice_id'] = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
		    		self.d['name'] = "Wanda"
		    	else:
		    		self.d['en_voice_id'] = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
		    		self.d['name'] = "Vision"
		    	self.y = multiprocessing.Process(target=self.bot.vision_body, args=(self.d['name'],self.d['en_voice_id'],))
		    	self.y.start()