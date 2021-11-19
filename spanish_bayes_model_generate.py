import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
import joblib
import json

#Vuelco los archivos a una estructura que alimentara el modelo.
def loadDataFrame(list,emotion):
	listResult=[]
	for item in list:
		listResult.append({"text":item,"sentiment":emotion})
	return pd.DataFrame(listResult,columns=['text','sentiment']);	

#Cargo archivos de datos.
print("Cargando archivos...")
positives_list=json.load(open('./data/spanish/spanish_positives.json'))

print("Terminos positivos:",len(positives_list))
negatives_list=json.load(open('./data/spanish/spanish_negatives.json'))

print("Terminos positivos:",len(negatives_list))
print("Resultado de carga:",len(positives_list)+len(negatives_list),"oraciones")

#Transformo a frames.
print("Convirtiendo a frames...")
postivesFrames= loadDataFrame(positives_list,'1')
negativesFrames= loadDataFrame(negatives_list,'0')

#Concateno frames.
train_df=pd.concat([postivesFrames,negativesFrames])

#Armo el pipe que alimentara el modelo.
print("Generando modelo..")
pipeline_bayes = Pipeline([('count', CountVectorizer()),('tfidf', TfidfTransformer()),('gnb', MultinomialNB())])
model_bayes = pipeline_bayes.fit(train_df['text'], train_df['sentiment'])

#Grabo el modelo.
print("Descargando modelo...")
ouput=joblib.dump(model_bayes, './models/bayes_spanish_model.pkl')

print("Modelo generado",ouput)