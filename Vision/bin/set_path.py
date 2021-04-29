import os
import sys
import pyttsx3 as spk
def serach(app):# Function for the seraching app in C drive & adding path in pth file
	try:
		pth=os.popen("dir C:\\{ap}.exe /b/s".format(ap=app)).read()
	except Exception as e:
		print(e)
	if pth != "File Not Found":
		f=open("c:\\pth.txt", 'a')
		f.write('{pth}'.format(pth=pth))
		f.close()


def launch(app):#Launching app using path in the pth file
	f=open("c:\\pth.txt","r")
	l=f.readlines()
	pth=None
	for i in l:
		if app in i:
			pth=i[:-1]
			break
			f.close()
	os.popen("start /wait {pth}".format(pth=pth))

app= sys.argv[1] #App to open
try:# cheking for the environment variable if found launching directly
	os.popen("start /wait {pth}".format(pth=app))
	spk.speak(app + " launched successfully....")
except:#if not found environment variable then
	try:# launching app by using path in pth file
		launch(app)
		spk.speak(app + " launched successfully....")
	except:# is path not found in the file then serching for app in c drive if path found then adding in the pth file
		spk.speak("seraching for app...")
		serach(app)
		try:# launching app by using path in pth file
			launch(app)
			spk.speak(app + " launched successfully....")
		except:# if app not found in c drive 
			spk.speak("App may not be installed yet")
