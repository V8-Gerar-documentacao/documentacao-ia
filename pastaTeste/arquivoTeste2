import os
import sys
from utils import gerar_documentacao

def processar_pasta(caminho):
    documentacoes = []

    if not os.path.isdir(caminho):
        print("O caminho informado não é uma pasta.")
        return

    for root, _, files in os.walk(caminho):
        for file in files:
            caminho_completo = os.path.join(root, file)
            resultado = gerar_documentacao(caminho_completo)
            if not resultado.startswith("Erro"):
                rel_path = os.path.relpath(caminho_completo, caminho)
                documentacoes.append(f"# Documentação: {rel_path}\n\n{resultado}")
            else:
                print(f"[ERRO] {caminho_completo}: {resultado}")

    if documentacoes:
        os.makedirs("documentacoes_geradas", exist_ok=True)
        caminho_saida = os.path.join("documentacoes_geradas", "documentacao_unica.md")
        with open(caminho_saida, "w", encoding="utf-8") as f:
            f.write("\n\n---\n\n".join(documentacoes))
        print(f"Documentação única salva em: {caminho_saida}")
    else:
        print("Nenhuma documentação foi gerada.")

def main():
    if len(sys.argv) < 2:
        print("Uso: python documentar_pasta.py <caminho_da_pasta>")
        sys.exit(1)

    caminho_pasta = sys.argv[1]
    processar_pasta(caminho_pasta)

if __name__ == "__main__":
    main()
