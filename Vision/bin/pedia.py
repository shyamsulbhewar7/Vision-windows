import wikipedia
import webbrowser
import pyttsx3 as spk
import speech_recognition as sr

def get_response():
	while True:
		try:
			r = sr.Recognizer()
			mic = sr.Microphone()
			with mic as source:
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
			inst = r.recognize_google(audio)
			break
		except:
			spk.speak("Sorry sir, i can not understand what you are saying..")
	return inst

def search_wiki():
	inst = get_response()
	print("Searching " + inst + ".....")
	try:
		results = wikipedia.summary(inst, sentences = 4)
		link = wikipedia.page(inst)
		link = link.url
		webbrowser.open(link)
		spk.speak("According to wikipedia ")
		spk.speak(results)
	except:
		spk.speak("Sorry sir i could not find information about {inst} on wikipedia".format(inst=inst))
		print(wikipedia.search(inst))


spk.speak("What would you like to know ?")
search_wiki()

