import random
import json
import pickle
import numpy as np 
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import pyttsx3 as spk
import os

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = pickle.load(open("H:\\Vision-windows\\Vision\\models\\words.pkl", 'rb'))
classes = pickle.load(open("H:\\Vision-windows\\Vision\\models\\classes.pkl", 'rb'))
model = load_model("H:\\Vision-windows\\Vision\\models\\chatbot_model.h5")

def clean_up(sentence):
	sen_words = nltk.word_tokenize(sentence)
	sen_words = [lemmatizer.lemmatize(word) for word in sen_words]
	return sen_words

# def sop_tag(sentence):
# 	pos_list = []
# 	tokens = clean_up(sentence)
# 	print(tokens)
# 	for w in tokens:
# 		pos_list.extend(nltk.pos_tag([w]))
# 	return pos_list

def bag_of_words(sentence):
	sen_words = clean_up(sentence)
	bag = [0] * len(words)
	for w in sen_words:
		for i, word in enumerate(words):
			if word == w:
				bag[i] = 1
	return np.array(bag)

def predict_class(sentence):
	bow = bag_of_words(sentence)
	res = model.predict(np.array([bow]))[0]
	ERROR_THRESHOLD = 0.25
	result = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
	result.sort(key=lambda x: x[1], reverse=True)
	return_list = []
	for r in result:
		return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
	return return_list

def get_responses(intents_list, intents_json):
	tag = intents_list[0]['intent']
	list_of_intents = intents_json['intents']
	for i in list_of_intents:
		if i['tag'] == tag:
			result = random.choice(i['responses'])
			break
	return result

def run(msg):
	ints = predict_class(msg)
	if ints[0]['intent'] == "launchapp":
		res = get_responses(ints, intents)
		cmd = list(map(str,msg.split(" ")))
		spk.speak(cmd[0] + "ing" + cmd[-1])
		os.system(res + " " + cmd[-1])
		return 0

	elif ints[0]['intent'] == "goodbye":
		res = get_responses(ints, intents)
		spk.speak(res)
		return 1

	else:
		res = get_responses(ints, intents)
		spk.speak(res)
		return 0