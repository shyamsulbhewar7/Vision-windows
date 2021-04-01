import os
def serach(app):# Function for the seraching app in C drive & adding path in pth file
	try:
		pth=os.popen("dir C:\\{ap}.exe /b/s".format(ap=app)).read()
	except Exception as e:
		print(e)
	if pth != "File Not Found":
		f=open("c:\\Users\\SHRI\\Desktop\\pth.txt", 'a')
		f.write('{pth}'.format(pth=pth))
		f.close()


def launch(app):#Launching app using path in the pth file
	f=open("c:\\Users\\SHRI\\Desktop\\pth.txt","r")
	l=f.readlines()
	pth=None
	for i in l:
		if app in i:
			pth=i[:-1]
			break
			f.close()
	os.startfile("{pth}".format(pth=pth))

app="chrome" #App to open

try:# cheking for the environment variable if found launching directly
	os.startfile("{pth}".format(pth=app))
except:#if not found environment variable then
	try:# launching app by using path in pth file
		launch(app)
	except:# is path not found in the file then serching for app in c drive if path found then adding in the pth file
		print("seraching for app")
		serach(app)
		try:# launching app by using path in pth file
			launch(app)
		except:# if app not found in c drive 
			print("App not installed yet")
		else:
			print("App Found & launching the app")
	else:
		print("App launch Succesfully")
else:
	print("App launch Succesfully")