# 🕒 Assistente de Regras de Ponto

Um assistente virtual inteligente que responde perguntas sobre as regras de ponto da empresa usando **IA local** (Llama3 via Ollama).

## 📋 O que é este projeto?

Este projeto é um **chatbot especializado** que utiliza:
- **RAG (Retrieval Augmented Generation)**: Busca informações específicas no documento de regras
- **Ollama + Llama3**: Modelo de IA open-source rodando 100% localmente
- **LangChain**: Framework para construir aplicações com LLMs
- **Streamlit**: Interface web simples e interativa

### 🎯 Principais Vantagens

✅ **Privacidade Total**: Todos os dados permanecem na sua máquina  
✅ **Respostas Precisas**: Baseadas no documento oficial de regras  
✅ **Fácil de Usar**: Interface web intuitiva  
✅ **Gratuito**: Sem custos com APIs de IA  

## 🚀 Como Funciona

```
📄 Documento de Regras
    ↓
🔪 Divisão em chunks
    ↓
🧮 Geração de embeddings
    ↓
💾 Armazenamento vetorial (ChromaDB)
    ↓
❓ Pergunta do usuário
    ↓
🔍 Busca semântica (RAG)
    ↓
🤖 Llama3 gera resposta contextualizada
    ↓
💬 Resposta ao usuário
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
```

**Ou usando uv (mais rápido):**
```powershell
uv sync
```

## 🎮 Como Usar

### Iniciar a aplicação

```powershell
streamlit run app.py
```

O navegador abrirá automaticamente em `http://localhost:8501`

### Fazer perguntas

Na interface web, digite suas perguntas sobre as regras de ponto:

## 💡 Exemplos de Uso

**Pergunta:** "Qual o horário de trabalho?"  
**Resposta:** "O horário de trabalho é das 8h às 17h, com 1 hora de almoço..."

**Pergunta:** "Posso compensar horas extras?"  
**Resposta:** "Sim, as horas extras podem ser compensadas dentro do mesmo mês..."

**Pergunta:** "Qual a tolerância para atrasos?"  
**Resposta:** "A tolerância é de 10 minutos por dia, até no máximo 3 vezes por semana..."

**Pergunta:** "Como funciona o banco de horas?"  
**Resposta:** "O banco de horas permite acumular horas extras que podem ser compensadas..."

## 📁 Estrutura do Projeto

```
assistente-regras-ponto/
├── app.py                 # Aplicação principal Streamlit
├── main.py                # Script alternativo/testes
├── docs/
│   └── regras_ponto.txt   # Documento com regras da empresa
├── requirements.txt       # Dependências Python
├── pyproject.toml         # Configuração do projeto (uv)
├── uv.lock               # Lock file do uv
└── README.md             # Este arquivo
```

## 🔧 Personalização

### Alterar o documento de regras

Edite o arquivo `docs/regras_ponto.txt` com as regras específicas da sua empresa.

### Trocar o modelo de IA

No arquivo `app.py`, altere o modelo:

```python
# Modelos disponíveis: llama3, llama3.1, mistral, codellama, etc.
embeddings = OllamaEmbeddings(model="llama3.1")
llm = OllamaLLM(model="llama3.1")
```

Para listar modelos disponíveis:
```bash
ollama list
```

### Ajustar configurações do Streamlit

Para rodar em porta/endereço específico:
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

### Aplicação lenta

- Verifique se tem RAM suficiente (mínimo 8GB)
- Considere usar um modelo menor: `ollama pull llama3:8b`
- Ajuste o `chunk_size` no código para valores menores

### ChromaDB warnings

São avisos normais do SQLite. Podem ser ignorados ou desabilitados com:
```python
import warnings
warnings.filterwarnings('ignore')
```

## 🛠️ Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/) - Interface web
- [LangChain](https://python.langchain.com/) - Framework LLM
- [Ollama](https://ollama.com/) - Execução local de LLMs
- [Llama3](https://llama.meta.com/) - Modelo de linguagem
- [ChromaDB](https://www.trychroma.com/) - Banco de dados vetorial

## 📝 Licença

Este projeto é de código aberto. Sinta-se livre para usar e modificar.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 👤 Autor

**lukadsant**
- GitHub: [@lukadsant](https://github.com/lukadsant)

---

⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!
