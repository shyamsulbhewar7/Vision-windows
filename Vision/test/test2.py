import pyttsx3
engine = pyttsx3.init()

# Voice IDs pulled from engine.getProperty('voices')
# These will be system specific
hi_voice_id_f = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM"
hi_voice_id_m = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM"

# Use female English voice
engine.setProperty('voice', hi_voice_id_m)
engine.say('नमस्ते...')
engine.say('हैलो ... मैं vision हूं')

# Use female Russian voice
engine.setProperty('voice', hi_voice_id_f)
engine.say('नमस्ते...')
engine.say('हाय ... मैं wanda हूं')

engine.runAndWait()
