import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

print('Cargando archivo csv...')
data = pd.read_csv('./data/google_play_store_apps_reviews_training.csv')
data.head()

def preprocess_data(data):
    # Remove package name as it's not relevant
    data = data.drop('package_name', axis=1)    
    # Convert text to lowercase
    data['review'] = data['review'].str.strip().str.lower()
    return data

print('Procesando datos...')
data = preprocess_data(data)

# Split into training and testing data
x = data['review']
y = data['polarity']
x, x_test, y, y_test = train_test_split(x,y, stratify=y, test_size=0.25, random_state=42)

# Vectorize text reviews to numbers
vec = CountVectorizer(stop_words='english')
x = vec.fit_transform(x).toarray()
x_test = vec.transform(x_test).toarray()

print('Genero el modelo...')

#Generate model
model = MultinomialNB()
model.fit(x, y)

# Save model
output=joblib.dump(model, 'bayes_model.pkl')
print('Modelo descargado',output)