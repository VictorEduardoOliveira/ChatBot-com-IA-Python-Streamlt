# titulo
# input do chat (campo de mensagem)
# a cada mensagem que o usuario enviar:
    # mostrar a mensagem que o usario enviou ao chat
    # pegar a pergunta e enviar para uma IA responder
    # exibir a resposta da IA na tela

#Streamlit -> apenas com Python criar o frontend e o Backend
# a IA que vamos usar e: OpneAI

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="Sua_Chave")


st.write("## ChatBot com IA") # markdown

if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = []

print(st.session_state["lista_mensagem"])
mensagem = st.chat_input("Digite a sua mensagem")

for texto in st.session_state["lista_mensagem"]:
    role = texto["role"]
    content = texto["content"]
    st.chat_message(role).write(content)

if mensagem:
    st.chat_message("user").write(mensagem)
    mensagem_usuario = {"role": "user", "content": mensagem}
    st.session_state["lista_mensagem"].append(mensagem_usuario)
    # Nome
    # user
    # assistant

    #resposta ia
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagem"],
        model="gpt-4o"
    )
    print(resposta_ia)
    
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagem"].append(mensagem_ia)


