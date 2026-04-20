import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory

# Importamos as funções que você criou no engine.py
from engine import consultar_estoque, configurar_rag

# 1. Configuração do Ambiente e LLM
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Usamos o Gemini 2.0 Flash com configurações de retentativa
llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1,
)

# 2. Configurar a ferramenta de RAG (Busca em documentos)
vectorstore = configurar_rag()
retriever = vectorstore.as_retriever()

def buscar_nas_politicas(query):
    docs = retriever.invoke(query)
    return "\n".join([doc.page_content for doc in docs])

# 3. Toolkit (Ferramentas)
tools = [
    Tool(
        name="ConsultaEstoque",
        func=consultar_estoque,
        description="Útil para perguntas sobre disponibilidade, preço ou detalhes de produtos específicos."
    ),
    Tool(
        name="BuscaPoliticas",
        func=buscar_nas_politicas,
        description="Útil para horários de funcionamento, formas de pagamento e políticas da empresa."
    )
]

# 4. Configurar a Memória
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 5. O Prompt (OTIMIZADO para economizar tokens e evitar erro 429)
template = """Você é a NovaQuest, assistente da TechNova.
Responda de forma CURTA e DIRETA em Português.

FERRAMENTAS:
------
Você tem acesso:
{tools}

Para usar uma ferramenta, use EXATAMENTE este formato:

Thought: Do I need to use a tool? Yes
Action: [{tool_names}]
Action Input: o que buscar
Observation: resultado

Se já tiver a resposta ou não precisar de ferramenta:
Thought: Do I need to use a tool? No
Final Answer: [sua resposta curta aqui]

Histórico:
{chat_history}

Pergunta: {input}
{agent_scratchpad}"""

prompt = PromptTemplate.from_template(template)

# 6. Inicializar o Agente com limite estrito de iterações
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    memory=memory, 
    verbose=True, 
    max_iterations=2, # Reduzimos para 2 para economizar cota de API
    handle_parsing_errors=True 
)

# Teste rápido
if __name__ == "__main__":
    print("NovaQuest Ativa! (Aguarde 30s entre as perguntas para evitar erro de cota)")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit"]: break
        try:
            response = agent_executor.invoke({"input": user_input})
            print(f"NovaQuest: {response['output']}")
        except Exception as e:
            print(f"Erro: {e}. Aguarde um momento antes de tentar novamente.")