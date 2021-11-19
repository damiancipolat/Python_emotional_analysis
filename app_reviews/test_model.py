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
	'es lindo',
	'me sirve',
	'5 estrellas',
	'el mejor',
	'Maaaala',
	'una mierda',
	'Me sirve aveces',
	'No funciona'
	'una lastima me era muy util'
]

#Constantes
emotions=['Positivo','Negativo']

#Recorro haciendo predicciones.
for testphrase in testphrases:
	#Usando el clasificador bayesiano.	
	result = model.predict([testphrase])
	#Muestro el resultado.
	print(testphrase+' --> '+emotions[int(result)])
