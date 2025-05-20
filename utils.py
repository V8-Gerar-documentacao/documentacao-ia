import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")

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

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Erro {response.status_code}: {response.text}")

    except Exception as e:
        return f"Erro ao gerar documentação: {e}"
