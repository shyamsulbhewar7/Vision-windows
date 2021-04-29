import os
import sys
import pyttsx3 as spk
import speech_recognition as sr
from word2number import w2n

def get_index(inst):
	return w2n.word_to_num(inst)

def open_file(inpt):
	os.popen('start /wait "{pth}"'.format(pth=y[inpt]))

def get_response():
	spk.speak("Which file shall i open for you sir ?")
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	inst = r.recognize_google(audio)
	if "exit" in inst or "quit" in inst or inst == "bye" or inst == "good bye":
		spk.speak("Good bye sir...")
		exit()
	else:
		num = get_index(inst)
		spk.speak("Opening file number " + str(num))
		open_file(num)

def search_any_file(filename):
	pths=''
	print(filename)
	print('Searching File....')
	pth=os.popen("wmic logicaldisk get caption").read()
	disks = pth.split("\n\n")
	for y in range(1,len(disks)):
		disks[y]=disks[y].strip()
		pths+=os.popen("dir "+disks[y]+"\\"+filename+".* /b/s").read()
	paths = pths.split("\n")
	return paths

file ='"'+sys.argv[1]+'"'

y=search_any_file(file)

spk.speak("I found the following files for you...")
print("List of files")
print("---" * 35)
for z in range(len(y[:-1])):
	print(z+1," | ",y[z])
print("---" * 35)

while True:
	try:
		get_response()
	except:
		spk.speak("I can not understand what you are saying...")