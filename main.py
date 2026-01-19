from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise RuntimeError("API_KEY não configurada. Copie .env.example para .env e preencha.")

print("Ambiente OK.")