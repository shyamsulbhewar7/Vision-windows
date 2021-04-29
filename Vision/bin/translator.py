import translate as tl 
import pyttsx3 as spk
import sys

text = sys.argv[1]

dl = sys.argv[1]

sl = sys.argv[2]

newtext = tl.translate_text(text,dl,sl)

print(newtext)
spk.speak(newtext)