import os
import sys
from utils import gerar_documentacao

def salvar_documentacao(caminho_arquivo, conteudo):
    pasta_base = "documentacoes_geradas"
    nome_arquivo = os.path.splitext(os.path.basename(caminho_arquivo))[0] + ".md"
    caminho_saida = os.path.join(pasta_base, nome_arquivo)

    os.makedirs(pasta_base, exist_ok=True)

    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"Documentação salva em: {caminho_saida}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python documentar_arquivo.py <caminho_arquivo>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]

    if not os.path.isfile(caminho_arquivo):
        print("O caminho informado não é um arquivo.")
        sys.exit(1)

    resultado = gerar_documentacao(caminho_arquivo)
    if resultado.startswith("Erro"):
        print(f"[ERRO] {caminho_arquivo}: {resultado}")
    else:
        salvar_documentacao(caminho_arquivo, resultado)

if __name__ == "__main__":
    main()
