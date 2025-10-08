import streamlit as st

# Embeddings e vectorstore
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# Documentos e texto
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path

# LLM e chains
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


# Configuração da página
st.set_page_config(page_title="Assistente Empresarial", page_icon="💙")

st.title("💙 Assistente Empresarial")
st.write("Faça uma pergunta sobre um procedimento da empresa.")

# Carrega todos os documentos da pasta docs_processed
docs_dir = Path("docs_processed")

# Verifica se a pasta existe
if not docs_dir.exists():
    st.error("❌ Pasta 'docs_processed' não encontrada. Execute 'build_dataset.py' primeiro.")
    st.stop()

# Carrega todos os arquivos .txt da pasta
loader = DirectoryLoader(
    str(docs_dir),
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"autodetect_encoding": True},
    show_progress=True
)

docs = loader.load()

# Verifica se há documentos carregados
if not docs:
    st.warning("⚠️ Nenhum documento encontrado em 'docs_processed'. Adicione arquivos .txt na pasta.")
    st.stop()

st.success(f"✅ {len(docs)} documento(s) carregado(s)")

# Divide o texto em blocos
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = splitter.split_documents(docs)

# Cria embeddings e base vetorial local
embeddings = OllamaEmbeddings(model="llama3")

vectorstore = Chroma.from_documents(texts, embeddings)

# Configura o prompt em português
prompt_template = """Você é um assistente que responde perguntas sobre regras e procedimentos de uma empresa.
Use o contexto fornecido para responder à pergunta de forma clara e objetiva em português brasileiro.
Se você não souber a resposta, diga "Não encontrei essa informação nas regras e procedimentos.".

Contexto: {context}

Pergunta: {question}

Resposta em português:"""

PROMPT = PromptTemplate(
    template=prompt_template, 
    input_variables=["context", "question"]
)

# Configura o modelo e a cadeia de perguntas
llm = OllamaLLM(model="llama3")
qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=vectorstore.as_retriever(),
    chain_type_kwargs={"prompt": PROMPT}
)

# Interface
question = st.text_input("Pergunta:")
if question:
    with st.spinner("Analisando..."):
        answer = qa.invoke(question)
        st.write("**Resposta:**", answer["result"])
