import os
import pickle
from django.http import JsonResponse
from .nlp_utils import preprocess_input

model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')

with open(model_path, 'rb') as f:
    model_pipeline = pickle.load(f)

def process_input(request):
  if request.method == 'POST':
    user_input = request.POST.get('input')

    # Step 1: Preprocess the input using NLP (e.g., tokenization, stemming)
    preprocessed_input = preprocess_input(user_input)

    # Step 2: Predict the category using the Naive Bayes model
    predicted_category = model_pipeline.predict([preprocessed_input])[0]

    # Step 3: Use the predicted category as part of the GPT-4 prompt
    gpt4_prompt = f"This is a {predicted_category} question: {user_input}"

    # Step 4: Send the GPT-4 request and get the response (assuming you've integrated GPT-4)
    gpt4_response = send_to_gpt4(gpt4_prompt)

    return JsonResponse({'response': gpt4_response})

  return JsonResponse({'error': 'Invalid request method.'}, status=400)
