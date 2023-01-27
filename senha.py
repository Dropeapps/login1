users = {"Pedro": "1234"}

def login():
    st.set_page_config(page_title="Login", page_icon=":guardsman:", layout="wide")
    st.title("Login")

    # Obtendo dados de login do usuário
    username = st.text_input("Pedro")
    password = st.text_input("1234", type='password')

    if st.button("Entrar"):
        # Verificando se as credenciais estão corretas
        if username in users and users[username] == password:
            st.success("Login efetuado com sucesso!")
        else:
            st.error("Usuário ou senha incorretos.")

if __name__=='__main__':
    login()
