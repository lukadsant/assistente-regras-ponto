import streamlit as st
from langchain_community.embeddings import OllamaEmbeddings,FakeEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

# Configuração da página
st.set_page_config(page_title="Assistente de Regras de Ponto", page_icon="🕒")

st.title("🕒 Assistente de Regras de Ponto")
st.write("Faça uma pergunta sobre as regras de ponto da empresa.")

# Carrega o documento
loader = TextLoader("docs/regras_ponto.txt")
docs = loader.load()

# Divide o texto em blocos
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = splitter.split_documents(docs)

# Cria embeddings e base vetorial local
#embeddings = OllamaEmbeddings(model="llama3")
embeddings = FakeEmbeddings(size=768)

vectorstore = Chroma.from_documents(texts, embeddings)

# Configura o modelo e a cadeia de perguntas
llm = Ollama(model="llama3")
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

# Interface
question = st.text_input("Pergunta:")
if question:
    with st.spinner("Analisando..."):
        answer = qa.run(question)
        st.write("**Resposta:**", answer)
