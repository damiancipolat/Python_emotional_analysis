import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

# Load the train data
path = './data/'
train_base_df = pd.read_csv(path + "train.csv") 
test_base_df = pd.read_csv(path + "test.csv") 

# Define Class Integer Values
cleanup_nums = {"sentiment": {"negative": 1, "neutral": 2, "positive": 3}}

# Replace the Classes with Integer Values
train_df = train_base_df.copy()
train_df.replace(cleanup_nums, inplace=True)

# Clean the Test Data
test_df = test_base_df.copy()
test_df.replace(cleanup_nums, inplace=True)

# Create a Feature based on Text Length
train_df['text_length'] = train_df['text'].str.len() # Store string length of each sample
train_df = train_df.sort_values(['text_length'], ascending=True)
train_df = train_df.dropna()

# Create a Bayes Classifier
pipeline_bayes = Pipeline([
                	('count', CountVectorizer()),
                	('tfidf', TfidfTransformer()),
                	('gnb', MultinomialNB()),
                ])

# Train model using the created sklearn pipeline
model_bayes = pipeline_bayes.fit(train_df['text'], train_df['sentiment'])

#TEST
testphrases = ['The product is a shit', 'I love amazon', 'I dont like this', 'Terrible service','stupid people', 'nice thing']

for testphrase in testphrases:
	#Usando el clasificador bayesiano.
	resultBayes = model_bayes.predict([testphrase])
	# use model_bayes for predictions with the other model
	dict = {1: 'Negative', 2: 'Neutral', 3: 'Positive'}
	print(testphrase + '-> ' + dict[resultBayes[0]])