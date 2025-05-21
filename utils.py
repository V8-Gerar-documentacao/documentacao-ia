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
Você é um engenheiro DevOps sênior com ampla experiência em infraestrutura como código, CI/CD, automação, containers, monitoramento, cloud e boas práticas de segurança.

Sua tarefa é analisar o conteúdo abaixo e gerar uma **documentação técnica comentada**, **em português**, voltada para desenvolvedores, engenheiros de infraestrutura e times DevOps.

Siga estas diretrizes:

---

### 🧾 Estrutura da Documentação

1. **Título:** Crie um título claro e descritivo para o tema.
2. **Descrição Geral:** Apresente um resumo técnico do que está sendo documentado.
3. **Pré-requisitos (se aplicável):** Liste ferramentas, versões, permissões ou dependências necessárias.
4. **Seções Técnicas:** Explique passo a passo cada parte do conteúdo, incluindo:
   - Código ou configuração comentada linha a linha
   - Justificativas técnicas para decisões de arquitetura ou ferramentas usadas
   - Boas práticas DevOps associadas

---

### 🧑‍💻 Estilo de Escrita

- Linguagem técnica, clara e direta
- Use Markdown com **formatação limpa** e organizada:
  - `códigos em blocos`
  - **negrito** para termos importantes
  - ✅ listas com checkmarks para checklists ou boas práticas
  - 🛑 para avisos ou erros críticos

---

### 📦 Exemplo de Aplicação

Com base no conteúdo fornecido, escreva a documentação seguindo o padrão acima. Aqui está um exemplo de estrutura esperada:

---

# Configuração de Pipeline CI/CD com GitHub Actions para Aplicações em Go

## Descrição Geral

Este documento descreve como configurar um pipeline de integração contínua (CI) usando o GitHub Actions para aplicações desenvolvidas em Go. O pipeline realiza testes automatizados a cada push na branch `main`.

## Pré-requisitos

- Conta no GitHub
- Projeto Go com estrutura de módulos (`go.mod`)
- GitHub Actions habilitado no repositório

## Estrutura do Workflow `.github/workflows/go.yml`

```yaml
name: Go CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Setup Go
        uses: actions/setup-go@v4
        with:
          go-version: 1.21
      - name: Run tests
        run: go test ./...

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
