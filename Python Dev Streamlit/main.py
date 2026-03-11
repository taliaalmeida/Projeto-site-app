
# titutlo
# Campo de mensagem -> input do chat para o usuario mandar msg
# A cada msg que o usuario enviar
    # aparecer a msg que o usuario enviou no chat
    # pegar a pergunta e enviar para uma ia responder
    # exibir a resposta da IA na tela

# Frameworks .> apenas com o python criar o frontend e o backend

#Streamlit -> para criar a interface do chat
#Flask -> para criar a API que vai receber as perguntas do chat e enviar para a IA responder
#Django -> para criar a API que vai receber as perguntas do chat e enviar para a IA responder
#FastAPI -> para criar a API que vai receber as perguntas do chat e enviar para a IA responder

# a IA que vamos usar: OpenAI
# None -> é não existe
# st.file_uploader() -> para o usuario selecionar um arquivo do computador e enviar para a IA responder

import streamlit as st
from openai import OpenAI

modelo_ia = "SUA CHAVE AQUI"
st.write("## Chatbot da Nati") # markdown (texto)


# st.session_state["mensagens"] = [] # lista para armazenar as mensagens do chat

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)


if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    # Nome
    # User
    # Assistant

    # ia respondeu
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-3.5-turbo"
    )

    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)



    # role = quem pe o usuário
    # content = conteudo da mensagem

 #hugging face -> para criar a IA responder as perguntas do chat   






