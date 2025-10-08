import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_ollama import OllamaLLM

# Caminhos das pastas
RAW_DIR = Path("docs_raw")
PROCESSED_DIR = Path("docs_processed")

PROCESSED_DIR.mkdir(exist_ok=True)

# Inicializa o modelo local (Ollama precisa estar rodando: `ollama serve`)
llm = OllamaLLM(model="llama3")

# Função: gerar resumo detalhado + técnico
def gerar_resumo_completo(texto, nome_arquivo):
    prompt = f"""
Você é um analista de Recursos Humanos especializado em documentação interna.

Analise o documento abaixo e escreva um **resumo completo** que inclua:
- O tipo e o objetivo do documento;
- Quem o utiliza e em que situação;
- **Resumo detalhado do conteúdo interno**, como:
  - Requisitos, qualificações e habilidades citadas;
  - Processos ou etapas operacionais;
  - Campos importantes, se for formulário;
  - Tabelas, listas ou seções relevantes.
Mantenha o tom profissional e objetivo.

Documento: {nome_arquivo}

Conteúdo:
\"\"\"
{texto[:4000]}
\"\"\"
"""
    try:
        resumo = llm.invoke(prompt)
        return str(resumo)
    except Exception as e:
        print(f"⚠️ Erro ao gerar resumo: {e}")
        return "Resumo não gerado devido a erro."

# Função: extrair texto conforme tipo de arquivo
def extrair_texto(filepath: Path) -> str:
    ext = filepath.suffix.lower()
    try:
        if ext == ".pdf":
            loader = PyPDFLoader(str(filepath))
        elif ext in [".doc", ".docx"]:
            loader = Docx2txtLoader(str(filepath))
        elif ext == ".txt":
            loader = TextLoader(str(filepath))
        else:
            print(f"❌ Tipo não suportado: {filepath.name}")
            return ""
        docs = loader.load()
        return "\n".join([d.page_content for d in docs])
    except Exception as e:
        print(f"⚠️ Erro ao ler {filepath.name}: {e}")
        return ""

# Loop principal
for file in RAW_DIR.rglob("*"):
    if not file.is_file():
        continue

    nome_saida = PROCESSED_DIR / f"{file.stem}.txt"
    if nome_saida.exists():
        print(f"⏭️ Já processado: {file.name}")
        continue

    print(f"📄 Processando: {file.name}")
    texto_original = extrair_texto(file)

    if not texto_original.strip():
        print(f"⚠️ Sem texto extraído: {file.name}")
        continue

    resumo = gerar_resumo_completo(texto_original, file.name)

    # Salva no formato "Resumo + Conteúdo Original"
    with open(nome_saida, "w", encoding="utf-8") as f:
        f.write("### RESUMO GERADO ###\n")
        f.write(resumo.strip())
        f.write("\n\n---\n\n")
        f.write("### CONTEÚDO ORIGINAL ###\n")
        f.write(texto_original.strip())

    print(f"✅ Documento processado e salvo: {nome_saida.name}")

print("\n🎉 Processamento concluído! Arquivos disponíveis em:", PROCESSED_DIR)