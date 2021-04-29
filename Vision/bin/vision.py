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
import translate


def greet(lang):
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		spk.speak(translate.translate_text("Good morning Sir...",lang))
	elif hour>=12 and hour<17:
		spk.speak(translate.translate_text("Good Afternoon sir...",lang))
	else :
		spk.speak(translate.translate_text("Good Evening Sir ",lang))
	    		
def vision_body(name,voice,lang):
	engine = spk.init()
	engine.setProperty('voice', voice)
	engine.setProperty("language",lang)
	greet(lang)
	while 'True':
		try:
			spk.speak(translate.translate_text("{name}at your service...What can i do for you sir ?".format(name=name),lang))
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
			spk.speak(translate.translate_text("Sorry sir, i can not understand what you are saying.",lang))

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


def Key_Controls():
	global d
	global voices
	y = multiprocessing.Process(target=vision_body, args=(d['name'],d['en_voice_id'],d['lang'],))
	y.start()
	while True:
	    if keyboard.read_key() == "q":
	        ans = input("Do you really want to quit ? (yes/no) ")
	        if 'yes' in ans:
	        	spk.speak("Terminating....")
	        	y.terminate()
	        	sys.exit()

	    if keyboard.read_key() == "v":
	    	y.terminate()
	    	if d['name'] == 'Vision' and 'EN-US' in d['en_voice_id']:
	    		d['en_voice_id'] = voices[1]
	    		d['name'] = "Wanda"
	    	elif d['name'] == 'Wanda' and 'EN-US' in d['en_voice_id']:
	    		d['en_voice_id'] = voices[0]
	    		d['name'] = "Vision"
	    	elif d['name'] == 'Wanda' and 'hiIN' in d['en_voice_id']:
	    		d['en_voice_id'] = voices[2]
	    		d['name'] = "Vision"
	    	elif d['name'] == 'Vision' and 'hiIN' in d['en_voice_id']:
	    		d['en_voice_id'] = voices[3]
	    		d['name'] = "Wanda"
	    	y = multiprocessing.Process(target=vision_body, args=(d['name'],d['en_voice_id'],d['lang'],))
	    	y.start()
	    if keyboard.read_key() == "l":
	    	y.terminate()
	    	if d['lang']=='en':
	    		d['lang']='hi'
	    		if d['name'] == 'Wanda':
	    			# d['name'] = 'Nila'
	    			d['en_voice_id']=voices[3]
	    		else:
	    			d['en_voice_id']=voices[2]
	    		lang='hi'
	    	else:
	    		if d['name'] == 'Vision':
	    			# d['name']='Chitti'
	    			d['en_voice_id']=voices[0]
	    		else:
	    			d['en_voice_id']=voices[1]
	    		d['lang']='en'
	    	y = multiprocessing.Process(target=vision_body, args=(d['name'],d['en_voice_id'],d['lang'],))
	    	y.start()