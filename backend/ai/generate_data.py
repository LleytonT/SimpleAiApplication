import pandas as pd
import random

# Define categories and sample questions
categories = ['health', 'finance', 'technology', 'education', 'entertainment']
questions = {
    'health': [
        "What are the symptoms of flu?",
        "How can I maintain a healthy diet?",
        "What exercises are best for weight loss?",
        "What is the recommended amount of sleep for adults?",
        "How can I boost my immune system?",
        "What are the benefits of yoga?",
        "How do vaccines work?",
        "What is mental health?",
        "How to manage stress effectively?",
        "What are the signs of depression?"
    ],
    'finance': [
        "How to save money effectively?",
        "What is a good credit score?",
        "How to invest in stocks?",
        "What are the basics of personal finance?",
        "How to budget my expenses?",
        "What is the difference between a Roth and traditional IRA?",
        "How do I improve my credit score?",
        "What is cryptocurrency?",
        "How to plan for retirement?",
        "What are the best ways to reduce debt?"
    ],
    'technology': [
        "What is the latest smartphone on the market?",
        "How does artificial intelligence work?",
        "What are the benefits of cloud computing?",
        "How can I protect my online privacy?",
        "What is the difference between machine learning and deep learning?",
        "How to build a website?",
        "What programming languages should I learn?",
        "What is blockchain technology?",
        "How do I get started with coding?",
        "What are the best practices for cybersecurity?"
    ],
    'education': [
        "What are the benefits of online learning?",
        "How to choose the right college?",
        "What is the importance of early childhood education?",
        "How to improve study habits?",
        "What subjects are essential for a career in science?",
        "How to apply for scholarships?",
        "What are the advantages of vocational training?",
        "How to write a good essay?",
        "What are effective teaching methods?",
        "What is the impact of technology on education?"
    ],
    'entertainment': [
        "What are the top movies of this year?",
        "How to get into the music industry?",
        "What are the best TV shows to binge-watch?",
        "How to plan a fun weekend?",
        "What are the latest video games?",
        "How to start a YouTube channel?",
        "What are the best books to read?",
        "How to organize a movie night?",
        "What is the history of rock music?",
        "How to write a screenplay?"
    ]
}

# Generate synthetic data
data = []

for _ in range(1000):
    category = random.choice(categories)
    question = random.choice(questions[category])
    data.append({'input': question, 'label': category})

# Create a DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv('training_data.csv', index=False)

print("Synthetic training data generated and saved to 'training_data.csv'.")
