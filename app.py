import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

text = "こんにちは"
len(get_embedding(text))
embedding_length = len(get_embedding(text))
print(embedding_length)

print(get_embedding(text))