import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

data = pd.read_csv('training_data.csv')

X = data['input']
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

model_pipeline.fit(X_train, y_train)

with open('trained_model.pkl', 'wb') as f:
    pickle.dump(model_pipeline, f)

print("Model trained and saved as 'trained_model.pkl'.")
