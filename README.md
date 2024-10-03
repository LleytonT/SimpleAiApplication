# NSW HSC Tutor

This project is an AI-powered tutoring application designed to assist students preparing for the Australian NSW Higher School Certificate (HSC) exams. It leverages machine learning to classify questions into subjects and uses OpenAI's GPT-4 to provide detailed answers.
See it live https://simple-ai-application.vercel.app/ .

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Machine Learning Model](#machine-learning-model)

## Project Overview

### Purpose
This is a simple HSC tutor powered by gpt-4o designed to help students for the HSC.

### Functionality
- **Subject Classification**: The application classifies user questions into three categories: **Mathematics**, **English**, and **Physics**.
- **AI-Powered Responses**: It uses OpenAI's GPT-4 to generate detailed responses based on the categorized questions.
- **Natural Language Processing (NLP)**: User input is preprocessed to improve classification accuracy and ensure that the model understands the context of the questions.
- **User Interface**: The frontend is built with React and Tailwind CSS for a clean and responsive design.

## Technologies Used

- **Frontend**: React, Tailwind CSS
- **Backend**: Django, Django REST Framework
- **Machine Learning**: Scikit-learn (Naive Bayes Classifier)
- **APIs**: OpenAI GPT-4
- **Data**: CSV files for training data

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/LleytonT/SimpleAiApplication.git
   cd SimpleAiApplication
   ```
2. **Navigate to the backend directory and set up the Python environment**:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ``` 
4. **Set up your environment variables**:
   - In the terminal export your OpenAi API key:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```
5. **Start the Django server**:
   ```bash
   python manage.py runserver
   ```
6. **Navigate to the frontend directory**:
   ```bash
   cd ../ui
   ```
7. **Install frontend dependencies**:
   ```bash
   npm install
   ```
8. **Start the React app**:
   ```bash
   npm start
   ```

## Usage
1. Open your web browser and go to http://localhost:3000.
2. Select the chat mode and start typing your questions related to Mathematics, English, or Physics.
3. Receive AI-generated responses to help with your studies.

## Machine Learning Model
### Overview
The machine learning model is designed to classify student queries into predefined subjects (Mathematics, English, Physics) using a Naive Bayes classifier.

### Data Preparation
- Training Data: A CSV file named hsc_tutor_training_data.csv is created, containing various questions and their associated subjects.
- Vectorization: The model uses CountVectorizer to convert text data into a numerical format suitable for training.

### Model Training
1. The training script (train_model.py) uses the sklearn library to implement the model.
2. The model is trained on 80% of the data and evaluated on the remaining 20%.

Key Code Snippets
```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pandas as pd

# Load dataset
data = pd.read_csv('hsc_tutor_training_data.csv')
X = data['input']
y = data['label']

# Create and train the model pipeline
model_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])
model_pipeline.fit(X_train, y_train)
```
## Natural Language Processing (NLP)
### Purpose
NLP techniques are employed to preprocess user input, improving the model's ability to classify questions accurately.

### Techniques Used
- Tokenization: Breaking down user input into individual words or tokens.
- Lemmatization: Reducing words to their base or root form.
- Preprocessing Function: The `preprocess_input` function handles input cleaning and preparation before classification.

Example Preprocessing Code
```python
import nltk
from nltk.stem import WordNetLemmatizer

def preprocess_input(text):
    # Tokenization and lemmatization
    tokens = nltk.word_tokenize(text.lower())
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized)

```




