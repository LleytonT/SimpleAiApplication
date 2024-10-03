# NSW HSC Tutor

This project is an AI-powered tutoring application designed to assist students preparing for the Australian NSW Higher School Certificate (HSC) exams. It leverages machine learning to classify questions into subjects and uses OpenAI's GPT-4 to provide detailed answers.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Training the Model](#training-the-model)

## Features

- **Subject Classification**: Classifies questions into three categories: Mathematics, English, and Physics.
- **AI-Powered Responses**: Utilizes OpenAI's GPT-4 to generate coherent and contextually relevant answers to student inquiries.
- **User-Friendly Interface**: Simple chat interface built with React and styled using Tailwind CSS.

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
   cd nsw-hsc-tutor
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

# Usage
1. Open your web browser and go to http://localhost:3000.
2. Select the chat mode and start typing your questions related to Mathematics, English, or Physics.
3. Receive AI-generated responses to help with your studies.

# Training the Model

To train or retrain the machine learning model:
1. Ensure you have the training data (hsc_tutor_training_data.csv) ready.
2. Run the training script:
   ```bash
   python train_model.py
   ```

This will create a pickle file containing the trained model, which is then used by the Django backend.

  


