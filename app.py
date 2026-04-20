import streamlit as st
from agent import agent_executor

st.set_page_config(page_title="TechNova AI - Suporte", page_icon="🤖")

st.title("🤖 NovaQuest - TechNova Solutions")
st.markdown("---")

# Inicializar histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada do usuário
if prompt := st.chat_input("Como posso ajudar você hoje?"):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gerar resposta do Agente
    with st.chat_message("assistant"):
        try:
            # Aqui chamamos o seu agent_executor que já tem memória e ferramentas
            response = agent_executor.invoke({"input": prompt})
            output = response["output"]
            st.markdown(output)
            st.session_state.messages.append({"role": "assistant", "content": output})
        except Exception as e:
            if "429" in str(e):
                st.error("Limite de requisições atingido. Aguarde 30 segundos e tente novamente.")
            else:
                st.error(f"Ocorreu um erro: {e}")