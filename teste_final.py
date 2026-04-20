import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Usando a biblioteca NATIVA (sem LangChain)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents="Olá, você está funcionando?"
    )
    print(f"RESPOSTA DO GOOGLE: {response.text}")
except Exception as e:
    print(f"ERRO NATIVO: {e}")