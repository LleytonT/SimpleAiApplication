import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import pickle
import os

# Load your dataset
data = pd.read_csv('training_data.csv')

# Check class balance
print(data['label'].value_counts())

# Feature (input) and labels
X = data['input']
y = data['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with vectorizer and classifier, using n-grams
model_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range=(1, 2))),  # Use unigrams and bigrams
    ('classifier', MultinomialNB(alpha=0.5))  # Adjust alpha for Naive Bayes smoothing
])

# Train the model
model_pipeline.fit(X_train, y_train)

# Evaluate the model
y_pred = model_pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

# Define the path to save the model
model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')

# Save the model as a pickle file
with open(model_path, 'wb') as f:
    pickle.dump(model_pipeline, f)

print(f"Model trained and saved as {model_path}")
