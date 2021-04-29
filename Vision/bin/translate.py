from google_trans_new import google_translator 
def translate_text(txt,dest_lang,src_lang='en'):
	translator = google_translator()  
	try:
		translate_textt = translator.translate(txt, lang_src=src_lang, lang_tgt=dest_lang)
		return translate_textt  
	except:
		return txt