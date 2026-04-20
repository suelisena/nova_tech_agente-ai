import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import mysql.connector

load_dotenv()


def consultar_estoque(nome_produto):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",      
            password="admin123",
            database="technova_db"
        )
        cursor = conn.cursor(dictionary=True)
        query = "SELECT nome, preco, estoque, descricao FROM produtos WHERE nome LIKE %s"
        cursor.execute(query, (f"%{nome_produto}%",))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if resultado:
            return f"Produto: {resultado['nome']} | Preço: R${resultado['preco']} | Estoque: {resultado['estoque']} unidades | Detalhes: {resultado['descricao']}"
        else:
            return "Produto não encontrado no catálogo."
    except Exception as e:
        return f"Erro ao acessar banco de dados: {e}"

def configurar_rag():
    # 1. Carregar o documento
    loader = TextLoader("data/politicas_empresa.txt", encoding="utf-8")
    documents = loader.load()

    # 2. Dividir o texto em pedaços menores (Chunks)
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    # 3. Criar os Embeddings usando HuggingFace (modelo leve e eficiente)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 4. Criar o Banco de Dados Vetorial (FAISS)
    vectorstore = FAISS.from_documents(docs, embeddings)
    
    # Salva localmente para não precisar processar toda vez
    vectorstore.save_local("faiss_index")
    return vectorstore

if __name__ == "__main__":
    print("Processando documentos e criando base vetorial...")
    configurar_rag()
    print("Base RAG criada com sucesso!")