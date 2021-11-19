import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
import joblib
import json

#Cargo el modelo.
model = joblib.load('./bayes_model.pkl')

#Lista de palabras.
testphrases = [
	'The product is a shit',
	'I love amazon',
	'I dont like this',
	'Terrible service',
	'stupid people',
	'nice thing'
]

#Constantes
emotions={1: 'Negative', 2: 'Neutral', 3: 'Positive'}

#Recorro haciendo predicciones.
for testphrase in testphrases:
	#Usando el clasificador bayesiano.	
	result = model.predict([testphrase])
	#Muestro el resultado.
	print(testphrase + '-> ' + emotions[result[0]])
