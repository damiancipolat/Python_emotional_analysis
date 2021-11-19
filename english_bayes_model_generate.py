from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import joblib

# Load the train data
print("Cargando archivo...")
train_base_df = pd.read_csv("./data/english/english_words.csv")

# Define Class Integer Values
cleanup_nums = {"sentiment": {"negative": 1, "neutral": 2, "positive": 3}}

# Replace the Classes with Integer Values
print("Normalizo datos...")
train_df = train_base_df.copy()
train_df.replace(cleanup_nums, inplace=True)

# Create a Feature based on Text Length
train_df['text_length'] = train_df['text'].str.len() # Store string length of each sample
train_df = train_df.sort_values(['text_length'], ascending=True)
train_df = train_df.dropna()

# Create a Bayes Classifier
print("Armo pipeline...")
pipeline_bayes = Pipeline([
	('count', CountVectorizer()),
	('tfidf', TfidfTransformer()),
	('gnb', MultinomialNB())
])

# Train model using the created sklearn pipeline
print("Genero el modelo...")
model_bayes = pipeline_bayes.fit(train_df['text'], train_df['sentiment'])

#Grabo el modelo.
print("Descargando modelo...")
ouput=joblib.dump(model_bayes, './models/bayes_english_model.pkl')