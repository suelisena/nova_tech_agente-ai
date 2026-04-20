# NovaQuest - Agente Inteligente de E-commerce 🤖🛒

Este projeto consiste em um assistente virtual inteligente desenvolvido para a **TechNova Solutions**. A NovaQuest utiliza inteligência artificial de ponta para auxiliar clientes em consultas de estoque em tempo real, dúvidas sobre políticas da empresa e atendimento geral, integrando processamento de linguagem natural com bases de dados relacionais e documentos privados.

---

## 📌 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [📺 Demonstração](#-demonstração)
- [⚙️ Arquitetura do Sistema](#️-arquitetura-do-sistema)
- [🚀 Funcionalidades Principais](#-funcionalidades-principais)
- [🛠️ Stack Tecnológica](#️-stack-tecnológica)
- [🧠 Desafios Técnicos e Superação](#-desafios-técnicos-e-superação)
- [💻 Como Executar](#-como-executar)

---

## 📖 Sobre o Projeto

A **NovaQuest** foi criada para resolver o desafio de fornecer respostas rápidas e precisas no e-commerce. Diferente de chatbots tradicionais baseados em árvores de decisão, este agente utiliza **Raciocínio ReAct** para decidir, em tempo real, qual ferramenta utilizar para responder ao usuário de forma fidedigna.

---

## 📺 Demonstração


![Demonstração NovaQuest](video_technova_AI.mp4)

> **Nota:** No vídeo, é possível observar o agente consultando o banco de dados para informar preços e lendo documentos internos para explicar a política de trocas.

---

## ⚙️ Arquitetura do Sistema

O sistema opera sob a orquestração do **LangChain**, seguindo o fluxo:
1. **User Input:** O usuário faz uma pergunta via interface **Streamlit**.
2. **Agent Reasoning:** O modelo **Llama 3 (via Groq)** analisa a intenção da pergunta.
3. **Tool Selection:**
   - Se for sobre estoque/preço: O agente aciona a ferramenta **SQL** (conectada ao **MySQL**).
   - Se for sobre políticas/horários: O agente utiliza **RAG** (Retrieval-Augmented Generation) para buscar no contexto de documentos.
4. **Final Answer:** O agente sintetiza a informação técnica em uma resposta natural e amigável.

---

## 🚀 Funcionalidades Principais

- **Consulta de Estoque em Tempo Real:** Integração direta com banco de dados **MySQL** para verificar disponibilidade e preços de produtos.
- **Base de Conhecimento (RAG):** Recuperação de informações de documentos (PDF/TXT), garantindo que as políticas da empresa sejam seguidas sem alucinações da IA.
- **Memória de Contexto:** Utilização de `ConversationBufferMemory` para que o agente se lembre de interações anteriores durante a sessão.
- **Baixa Latência:** Implementação utilizando a infraestrutura da **Groq**, permitindo respostas quase instantâneas.

---

## 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.x
- **Orquestração de IA:** LangChain
- **LLM:** Meta Llama 3 (via Groq Cloud API)
- **Interface de Usuário:** Streamlit
- **Banco de Dados:** MySQL
- **Processamento de Documentos:** PyPDF2 / FAISS (Vector Store)
- **Gestão de Variáveis:** Python-dotenv

---

## 🧠 Desafios Técnicos e Superação

Como Analista de Sistemas, este projeto apresentou desafios reais de engenharia que foram superados com sucesso:

1. **Migração Estratégica de LLM:** Inicialmente planejado para outro provedor, o sistema foi migrado para a **Groq (Llama 3)** para superar limitações de cota e garantir a melhor experiência de usuário com latência reduzida.
2. **Integração SQL Dinâmica:** Configuração de permissões e tratamento de queries para que o agente pudesse ler o schema do **MySQL** e gerar consultas SQL válidas de forma autônoma.
3. **Gestão de Depreciações:** Atualização constante do código para alinhar com as novas versões do LangChain, especificamente na migração de componentes de memória.
4. **Hardware vs Ambiente:** Ajustes finos no ambiente de desenvolvimento para garantir a estabilidade das conexões de banco de dados e APIs.

---

## 💻 Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/technova-ai.git](https://github.com/seu-usuario/technova-ai.git)
   
Instale as dependências:
2. pip install -r requirements.txt
Configure o arquivo .env com suas chaves de API (Groq) e credenciais do MySQL.

Execute a aplicação:
3.streamlit run app.py

Desenvolvido por Sueli Sena – Systems Analyst & Machine Learning Developer
Linkedin: https://www.linkedin.com/in/sueli-sena/
