# � Assistente Empresarial

Um assistente virtual inteligente que responde perguntas sobre regras, procedimentos e documentos da empresa usando **IA local** (Llama3 via Ollama).

## 📋 O que é este projeto?

Este projeto é um **chatbot especializado** que utiliza:

- **RAG (Retrieval Augmented Generation)**: Busca informações específicas em múltiplos documentos
- **Ollama + Llama3**: Modelo de IA open-source rodando 100% localmente
- **LangChain**: Framework para construir aplicações com LLMs
- **Streamlit**: Interface web simples e interativa
- **Processamento automático de documentos**: Converte PDFs, DOCs e TXTs em base de conhecimento

### 🎯 Principais Vantagens

✅ **Privacidade Total**: Todos os dados permanecem na sua máquina  
✅ **Respostas Precisas**: Baseadas em múltiplos documentos da empresa  
✅ **Respostas em Português**: Configurado para responder sempre em português brasileiro  
✅ **Fácil de Usar**: Interface web intuitiva  
✅ **Gratuito**: Sem custos com APIs de IA  
✅ **Múltiplos formatos**: Suporta PDF, DOC, DOCX e TXT

## 🚀 Como Funciona

### Pipeline de Processamento de Documentos

```
� docs_raw/ (PDFs, DOCs, TXTs)
    ↓
🔄 build_dataset.py processa arquivos
    ↓
🤖 Llama3 gera resumos contextuais
    ↓
📁 docs_processed/ (arquivos processados)
```

### Pipeline de Busca e Resposta

```
📂 docs_processed/ (múltiplos documentos)
    ↓
🔪 Divisão em chunks (500 caracteres)
    ↓
🧮 Geração de embeddings vetoriais
    ↓
💾 Armazenamento no ChromaDB
    ↓
❓ Pergunta do usuário (em português)
    ↓
🔍 Busca semântica (RAG) nos documentos
    ↓
🤖 Llama3 gera resposta em português
    ↓
💬 Resposta contextualizada ao usuário
```

## 📦 Pré-requisitos

- **Python 3.10+**
- **Windows 10/11** (para Ollama no Windows)
- **8GB RAM** mínimo (16GB recomendado para Llama3)

## ⚙️ Instalação

### 1️⃣ Instalar o Ollama

**No Windows:**

```powershell
# Opção 1: Download direto
# Acesse: https://ollama.com/download
# Baixe e execute o instalador .exe

# Opção 2: Via winget (recomendado)
winget install --id=Ollama.Ollama
```

**No Linux/Mac:**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2️⃣ Baixar o modelo Llama3

```powershell
# Após instalar o Ollama, baixe o modelo
ollama pull llama3
```

> ⚠️ **Nota**: O download do Llama3 pode levar alguns minutos (aproximadamente 4.7GB)

### 3️⃣ Clonar o repositório

```bash
git clone https://github.com/lukadsant/assistente-regras-ponto.git
cd assistente-regras-ponto
```

### 4️⃣ Criar ambiente virtual e instalar dependências

```powershell
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
.venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt

# Instalar pacotes adicionais necessários
pip install chardet  # Para detecção automática de encoding
```

**Ou usando uv (mais rápido):**

```powershell
uv sync
```

### 5️⃣ Preparar seus documentos

Crie as pastas necessárias:

```powershell
# Criar estrutura de pastas
New-Item -ItemType Directory -Force -Path "docs_raw"
New-Item -ItemType Directory -Force -Path "docs_processed"
```

Coloque seus documentos (PDFs, DOCs, TXTs) na pasta `docs_raw/`:

```
docs_raw/
├── regras_ponto.pdf
├── manual_funcionario.docx
├── procedimento_ferias.txt
└── ...
```

### 6️⃣ Processar os documentos

Execute o script de processamento:

```powershell
python build_dataset.py
```

Este script vai:
- ✅ Extrair texto de PDFs, DOCs e TXTs
- ✅ Gerar resumos contextuais usando Llama3
- ✅ Salvar os documentos processados em `docs_processed/`

## 🎮 Como Usar

### 1. Iniciar a aplicação

```powershell
streamlit run app.py
```

O navegador abrirá automaticamente em `http://localhost:8501`

**Para rodar em rede local (acessível de outros dispositivos):**

```powershell
streamlit run app.py --server.port 7860 --server.address 0.0.0.0
```

### 2. Verificar documentos carregados

Ao iniciar, a aplicação mostra:
- ✅ Quantidade de documentos carregados
- ⚠️ Avisos se não houver documentos
- ❌ Erro se a pasta não existir

### 3. Fazer perguntas

Na interface web, digite suas perguntas sobre procedimentos da empresa. **Todas as respostas são em português brasileiro!**

## 💡 Exemplos de Uso

### Perguntas sobre Regras de Ponto

**Pergunta:** "Qual o horário de trabalho?"  
**Resposta:** "O horário de trabalho é das 8h às 17h, com 1 hora de almoço..."

**Pergunta:** "Posso compensar horas extras?"  
**Resposta:** "Sim, as horas extras podem ser compensadas dentro do mesmo mês..."

**Pergunta:** "Qual a tolerância para atrasos?"  
**Resposta:** "A tolerância é de 10 minutos por dia, até no máximo 3 vezes por semana..."

### Perguntas sobre Procedimentos

**Pergunta:** "Como solicito férias?"  
**Resposta:** "Para solicitar férias, você deve preencher o formulário Form 80.02..."

**Pergunta:** "Qual o procedimento para abertura de vaga?"  
**Resposta:** "O procedimento envolve o preenchimento do Form 85.00 - Pedido de Abertura de Vaga..."

### Perguntas sobre Formulários

**Pergunta:** "Que formulários existem disponíveis?"  
**Resposta:** "Temos diversos formulários, incluindo Form 85.00 para abertura de vagas..."

## 📁 Estrutura do Projeto

```
assistente-regras-ponto/
├── app.py                    # Aplicação principal Streamlit (RAG + Chat)
├── build_dataset.py          # Script de processamento de documentos
├── main.py                   # Script alternativo/testes
│
├── docs_raw/                 # 📥 Documentos originais (PDFs, DOCs, TXTs)
│   ├── regras_ponto.pdf
│   ├── manual.docx
│   └── procedimento.txt
│
├── docs_processed/           # 📤 Documentos processados (TXTs resumidos)
│   ├── regras_ponto.txt
│   ├── manual.txt
│   └── procedimento.txt
│
├── docs/                     # 📚 Documentos legados (opcional)
│   └── regras_ponto.txt
│
├── requirements.txt          # Dependências Python
├── pyproject.toml            # Configuração do projeto (uv)
├── uv.lock                   # Lock file do uv
└── README.md                 # Este arquivo
```

## 🔧 Personalização

### Adicionar novos documentos

1. Coloque os documentos em `docs_raw/`
2. Execute `python build_dataset.py`
3. Reinicie o Streamlit

### Trocar o modelo de IA

No arquivo `app.py`, altere o modelo:

```python
# Modelos disponíveis: llama3, llama3.1, llama3.2, mistral, codellama, etc.
embeddings = OllamaEmbeddings(model="llama3.1")
llm = OllamaLLM(model="llama3.1")
```

Para listar modelos disponíveis:

```bash
ollama list
```

Para baixar um modelo diferente:

```bash
ollama pull llama3.1
```

### Alterar o prompt do assistente

No arquivo `app.py`, edite a variável `prompt_template`:

```python
prompt_template = """Você é um assistente especializado em [SEU DOMÍNIO].
Use o contexto fornecido para responder perguntas sobre [SUA ÁREA]...
"""
```

### Ajustar tamanho dos chunks

Para documentos maiores ou menores, ajuste no `app.py`:

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Tamanho do chunk (padrão: 500)
    chunk_overlap=100  # Sobreposição (padrão: 50)
)
```

### Configurar porta/endereço do Streamlit

```powershell
streamlit run app.py --server.port 7860 --server.address 0.0.0.0
```

## 🐛 Solução de Problemas

### Erro: "Ollama não encontrado"

Certifique-se de que o Ollama está instalado e no PATH:

```powershell
ollama --version
```

Se não funcionar, reinicie o terminal ou adicione ao PATH:  
`C:\Users\SEU_USUARIO\AppData\Local\Programs\Ollama`

### Erro: "Model not found"

Baixe o modelo novamente:

```powershell
ollama pull llama3
```

### Erro: "No module named 'chardet'"

Instale o pacote necessário:

```powershell
pip install chardet
```

### Erro: "UnicodeDecodeError" ou "Error loading file"

O código já está configurado com `autodetect_encoding=True`, mas se persistir:

1. Verifique se o `chardet` está instalado
2. Tente reprocessar o documento com `build_dataset.py`
3. Salve manualmente o arquivo com encoding UTF-8

### Erro: "Pasta 'docs_processed' não encontrada"

Execute o script de processamento primeiro:

```powershell
python build_dataset.py
```

### Aplicação lenta

- Verifique se tem RAM suficiente (mínimo 8GB)
- Considere usar um modelo menor: `ollama pull llama3:8b`
- Reduza o `chunk_size` no código
- Reduza o número de documentos processados

### Respostas em inglês

O código já está configurado para responder em português, mas se persistir:

1. Verifique se o `prompt_template` está correto no `app.py`
2. Adicione mais instruções explícitas no prompt
3. Considere usar um modelo diferente

### ChromaDB warnings

São avisos normais do SQLite. Podem ser ignorados ou desabilitados com:

```python
import warnings
warnings.filterwarnings('ignore')
```

## 🛠️ Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/) - Interface web interativa
- [LangChain](https://python.langchain.com/) - Framework para LLMs
- [Ollama](https://ollama.com/) - Execução local de LLMs
- [Llama3](https://llama.meta.com/) - Modelo de linguagem (Meta AI)
- [ChromaDB](https://www.trychroma.com/) - Banco de dados vetorial
- [PyPDF](https://pypdf.readthedocs.io/) - Processamento de PDFs
- [python-docx](https://python-docx.readthedocs.io/) - Processamento de DOCs
- [chardet](https://chardet.readthedocs.io/) - Detecção de encoding

## 📝 Licença

Este projeto é de código aberto. Sinta-se livre para usar e modificar.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 👤 Autor

**lukadsant**

- GitHub: [@lukadsant](https://github.com/lukadsant)

---

⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!
