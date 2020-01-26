import spacy
import en_core_web_sm
import numpy as np
import json
import requests
from bs4 import BeautifulSoup
nlp = en_core_web_sm.load()

candisatesList = []
with open('candidates.json','r') as candidates:
	candidateData = json.load(candidates)
for candidate in candidateData['Names']:
	candisatesList.append(candidate)

relatedWordsList = []
with open('relatedWords.json','r') as relatedWords:
	relatedWordsData = json.load(relatedWords)
for relatedWords in relatedWordsData['relatedWords']:
	relatedWordsList.append(relatedWords)

scoresList = []
with open('scoresList.json','r') as scores:
	scoresData = json.load(scores)
for i in range(len(scoresData)):
	scoresList.append(scoresData[i]['Score'])

r1 = requests.get(http://feeds.bbci.co.uk/news/politics)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage,'html5lib')
coverPageNews = soup1.find_all('item',class='paddeditembox')


# print(candisatesList,scoresList,relatedWordsList)
with open('inputText.txt',"r") as fullText:
	text = nlp(fullText.readline())
	for word in text:
		print(word.text,word.pos_)
		if(word.pos_=="PROPN"):
			for i in range(len(relatedWordsList)):
				if word.text in relatedWordsList[i]:
					scoresList[0][i]+=(text.sentiment-5)*0.001
					print(scoresList)

