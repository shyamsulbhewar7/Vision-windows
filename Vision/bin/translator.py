import translate as tl 
import pyttsx3 as spk
import sys

text = sys.argv[1]

dl = sys.argv[1]

newtext = tl.translate_text(text,dl)

print(newtext)
spk.speak(newtext)