import os
import pickle
import json
from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .nlp_utils import preprocess_input

model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')

with open(model_path, 'rb') as f:
  model_pipeline = pickle.load(f)

client = OpenAI()

@csrf_exempt
def process_input(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body.decode('utf-8'))
      user_input = data.get('input', None)
      context_mode = data.get('contextMode', None)
      messages = data.get('messages', [])
      
      if user_input is None:
        return JsonResponse({'error': 'No input provided.'}, status=400)
      
      preprocessed_input = preprocess_input(user_input)

      predicted_category = model_pipeline.predict([preprocessed_input])[0]

      gpt4_prompt = f"""You are an assistant focussed on helping students for the Australian NSW HSC.
      You will receive a predicted category and a user input. Anything before the 'User input' line is context. 
      This is a {predicted_category} input. User input: {user_input}"""

      gpt4_response = send_to_gpt4(gpt4_prompt, context_mode, messages)

      return JsonResponse({'response': gpt4_response})
    except json.JSONDecodeError:
      return JsonResponse({'error': 'Invalid JSON.'}, status=400)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=500)

  return JsonResponse({'error': 'Invalid request method.'}, status=400)


def send_to_gpt4(prompt, context_mode, messages):
  conversation_history = []

  if context_mode:
    for message in messages:
      role = "user" if message['user'] == "User" else "assistant"
      conversation_history.append({"role": role, "content": message['text']})
      
  conversation_history.append({"role": "user", "content": prompt})

  try:
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=conversation_history,
    )
    bot_response = response.choices[0].message.content

    print(bot_response)
    return bot_response
  except Exception as e:
    print(f"Error calling GPT-4: {e}")
    return "Error generating response."