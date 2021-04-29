# importing installed library
import pyjokes
import pyttsx3 as spk

# using get_joke() to generate a single joke
#language is english
#category is neutral
My_joke = pyjokes.get_joke(language="en", category="all")
print(My_joke)
spk.speak(My_joke)
