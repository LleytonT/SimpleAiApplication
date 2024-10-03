import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import pickle
import os

# Load the dataset
data = pd.read_csv('hsc_tutor_training_data.csv')

# Features (questions) and labels (subjects)
X = data['input']  # The question or input from the user
y = data['label']  # The subject (Mathematics, English, etc.)

# Train-test split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with a CountVectorizer and Naive Bayes classifier
model_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),  # Convert text to a matrix of token counts
    ('classifier', MultinomialNB())  # Naive Bayes classifier
])

# Train the model
model_pipeline.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model_pipeline.predict(X_test)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save the trained model to a file (pickle format)
model_path = os.path.join(os.path.dirname(__file__), 'trained_hsc_tutor_model.pkl')
with open(model_path, 'wb') as model_file:
    pickle.dump(model_pipeline, model_file)

print(f"Model trained and saved as {model_path}")
