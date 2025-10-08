# assistente-regras-ponto


curl -fsSL https://ollama.com/install.sh | sh
uv add langchain langchain-community langchain-ollama
pip install -U langchain langchain-community langchain-ollama
pip install -U sentence-transformers

ollama serve &
curl http://localhost:11434/api/tags

ollama pull llama3

streamlit run app.py
streamlit run app.py --server.port 7860 --server.address 0.0.0.0
