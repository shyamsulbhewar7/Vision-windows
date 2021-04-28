from google_trans_new import google_translator 

def change_lang(lang):
	if lang=='English':
		d={'en_voice_id': "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
		'name': 'Vision','lang':'en'}
		return d
	elif lang=='Hindi':
		d={'en_voice_id': "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM",
		'name': 'Vision','lang':'hi'}
		return d

def translate_text(txt,dest_lang):
	translator = google_translator()  
	translate_textt = translator.translate(txt, lang_src='en', lang_tgt=dest_lang)  
	return translate_textt