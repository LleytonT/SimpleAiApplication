import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_input(user_input):
  tokens = word_tokenize(user_input.lower())
  
  stop_words = set(stopwords.words('english'))
  tokens = [word for word in tokens if word not in stop_words]
  
  lemmatizer = WordNetLemmatizer()
  lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
  
  return ' '.join(lemmatized_tokens)