from youtubesearchpython import VideosSearch
import sys
import pyttsx3 as spk
import speech_recognition as sr
from word2number import w2n 
import vlc
import pafy

def get_results(show,lim):
	results = []
	videosSearch = VideosSearch(show, limit = int(lim))
	result = videosSearch.result()['result']
	i = 1
	for x in result:
		video = {}
		video["ind"] = i
		video["title"] = x["title"]
		video["duration"] = x["duration"]
		video["link"] = x["link"]
		video["channel_name"] = x["channel"]["name"]
		video["channel_link"] = x["channel"]["link"]
		results.append(video)
		i += 1
		del video
	return results

def show_results(show,lim):
	results = get_results(show,lim)
	for x in results:
		print(x["ind"],end=". ")
		print("Title: ",x["title"])
		print("Duration: ",x["duration"])
		print("Video Link: ", x["link"])
		print("Channel Name: ",x["channel_name"])
		print("Channel Link: ", x["channel_link"])
		print("-"*100)

def get_response(show,lim):
	spk.speak("Which video shall i play sir ?")
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
			spk.speak("Sorry sir, I can not understand what you are saying..")
	return inst

def clean_response(show, lim):
	response = list(map(str, get_response(show, lim).split(" ")))
	punctuation = ["?",",",".","/","|",":",";"]
	result = [word for word in response if word not in punctuation]
	final = " ".join(result)
	return final

def check_response(show,lim):
	results = get_results(show,lim)
	response = clean_response(show,lim)
	print(response)
	for x in results:
		title = x["title"].lower()
		if response.lower()[:15] in title:
			spk.speak("playing " + x["title"])
			play_video(x)
			return 0
		elif "playlist" in response.lower():
			visit_playlist(x)
			return 0
		else:
			try:
				num = w2n.word_to_num(response)
				if x["ind"] == num:
					spk.speak("playing " + x["title"])
					play_video(x)
					return 0
			except:
				return 1
	return 1

def play_video(x):
	url = x["link"]
	video = pafy.new(url)
	best = video.getbest()
	media = vlc.MediaPlayer(best.url)
	media.play()
	while True:
		pass

def visit_playlist(x):
	spk.speak("Use browser to visit playlist")
	spk.speak("Work to be done by shyam")


show = sys.argv[1]
lim = sys.argv[2]

spk.speak("Here are the Top {lim} results for {show}".format(lim=lim,show=show))
show_results(show,lim)
if check_response(show,lim):
	spk.speak("Sorry sir, i could not find the match in the list")