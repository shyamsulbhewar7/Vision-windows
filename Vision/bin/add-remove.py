import os
import sys
import pyttsx3 as spk
def install(app):
	if not os.system("choco install " + app):
		spk.speak(app + "installed successfully...")
	else:
		spk.speak("Failed to install " + app)
def uninstall(app):
	if not os.system("choco uninstall " + app):
		spk.speak(app + "uninstalled successfully...")
	else:
		spk.speak("Failed to uninstall " + app)
def upgrade(app):
	if not os.system("choco upgrade " + app):
		spk.speak(app + "updated successfully...")
	else:
		spk.speak("Failed to update " + app)
process = sys.argv[1]
app = sys.argv[2]
if process == 'install':
	install(app)
elif process == 'uninstall':
	uninstall(app)
elif process == 'upgrade' or process == 'update':
	upgrade(app)
elif process == 'info':
	spk.speak("Information on " + app)
	os.system("choco info " + app)
else:
	spk.speak("Sorry sir ... " + process + " operation can not be performed...")
