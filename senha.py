import streamlit as st

login_secreto = 'Pedro.miquelino'
senha_secreta = '1234567'

st.title("Autenticação de usuário")

login = st.text_input("Digite seu login: ")
if (login == login_secreto):
spp = st.text_input("Digite a senha: ", type='password')
 if (spp == senha_secreta):
st.write("Login feito com sucesso!")
 else:
st.write("Sua senha está incorreta")
else:
st.write("Usuário incorreto")
