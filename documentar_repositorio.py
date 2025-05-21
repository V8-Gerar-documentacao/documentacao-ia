import os
import sys
import shutil
import subprocess
from datetime import datetime
import pytz  # Importando o módulo pytz para trabalhar com fusos horários
from utils import gerar_documentacao

EXTENSOES_SUPORTADAS = (".py", ".js", ".ts", ".java", ".go", ".yaml", ".yml", "Dockerfile")

def clonar_repositorio(repo_url, destino="repositorio_clonado"):
    if os.path.exists(destino):
        shutil.rmtree(destino)
    subprocess.run(["git", "clone", repo_url, destino], check=True)
    return destino

def listar_arquivos_analise(caminho):
    arquivos = []
    for root, _, files in os.walk(caminho):
        for file in files:
            if file.endswith(EXTENSOES_SUPORTADAS) or file == "Dockerfile":
                arquivos.append(os.path.join(root, file))
    return arquivos

def obter_informacoes_commit(caminho_repo):
    # Obtemos as informações do último commit
    try:
        commit_info = subprocess.check_output(
            ["git", "-C", caminho_repo, "log", "-1", "--pretty=format:%an|%ad|%s"],
            encoding="utf-8"
        )
        autor, data_commit, mensagem_commit = commit_info.split("|")
        
        # Formatar a data do commit (assumindo que é uma data com fuso horário)
        data_commit = datetime.strptime(data_commit, "%a %b %d %H:%M:%S %Y %z")

        # Tornar a data atual 'aware' (com fuso horário UTC)
        utc_now = datetime.now(pytz.utc)
        
        # Calcula o tempo passado
        tempo_passado = utc_now - data_commit
        
        return autor, data_commit, tempo_passado, mensagem_commit
    except subprocess.CalledProcessError as e:
        return None, None, None, None

def salvar_documentacao_unica(conteudo, base_saida="documentacao_repositorio"):
    os.makedirs(base_saida, exist_ok=True)
    caminho_saida = os.path.join(base_saida, "DOCUMENTACAO_COMPLETA.md")

    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"[OK] Documentação gerada em: {caminho_saida}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python documentar_repositorio.py <url_repositorio_git>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        caminho_repo = clonar_repositorio(url)
        arquivos = listar_arquivos_analise(caminho_repo)

        # Obtemos as informações sobre o último commit
        autor, data_commit, tempo_passado, mensagem_commit = obter_informacoes_commit(caminho_repo)

        # Adiciona as informações do commit no início da documentação
        conteudo_documentacao = "# Documentação do Repositório\n\n"

        if autor:
            conteudo_documentacao += f"**Último Commit**\n\n"
            conteudo_documentacao += f"- **Autor**: {autor}\n"
            conteudo_documentacao += f"- **Data do Commit**: {data_commit.strftime('%d/%m/%Y %H:%M:%S')}\n"
            conteudo_documentacao += f"- **Tempo desde o Commit**: {str(tempo_passado).split('.')[0]} (hh:mm:ss)\n"
            conteudo_documentacao += f"- **Mensagem do Commit**: {mensagem_commit}\n\n"

        # Adiciona a documentação dos arquivos
        for arquivo in arquivos:
            resultado = gerar_documentacao(arquivo)
            if resultado.startswith("Erro"):
                print(f"[ERRO] {arquivo}: {resultado}")
            else:
                conteudo_documentacao += f"## {arquivo}\n\n"
                conteudo_documentacao += resultado + "\n\n"

        # Salva toda a documentação gerada em um único arquivo
        salvar_documentacao_unica(conteudo_documentacao)

        print("📄 Documentação finalizada.")
    except Exception as e:
        print(f"[FALHA]: {e}")

if __name__ == "__main__":
    main()
