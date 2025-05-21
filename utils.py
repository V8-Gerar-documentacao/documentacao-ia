import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()  # <- isso carrega o .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

def gerar_documentacao(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()

        prompt = f"""
Você é um engenheiro DevOps sênior. Documente em português, com explicações claras e técnicas, o conteúdo abaixo como se fosse uma documentação comentada para desenvolvedores ou engenheiros de infraestrutura. Use markdown com formatação limpa e organizada.

Script ou código:
{conteudo}
"""

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.4
        }

        for tentativa in range(5):  # tenta no máximo 5 vezes
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            elif response.status_code == 429:
                print("Limite de tokens excedido. Aguardando 6 segundos...")
                time.sleep(6)  # espera e tenta de novo
            else:
                raise Exception(f"Erro {response.status_code}: {response.text}")

        raise Exception("Limite de tentativas excedido.")

    except Exception as e:
        return f"Erro ao gerar documentação: {e}"
