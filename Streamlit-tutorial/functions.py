#Functions utils to development fast

#Lib
import streamlit as st

def main():
    st.sidebar.success('Selecione um item abaixo')

    st.markdown("<h1 style='color:#F00;'>Tutorial de desenvolvimento rápido com Streamlit Python (tags mais úteis)</h1>", unsafe_allow_html=True)

    st.markdown(
        """
            O **Streamlit** 👈 é um pacote Python open-source para criação de layout fácil e com aparência bonita. 

            Pode ser customizado para projetos de **Inteligência Artificial** e **Data Sciente**.

            **Requisitos:** Python: 3.6 - 3.8

            **Instalação:** pip install streamlit

            **Teste:** streamlit hello

            **Execução:** streamlit run app.py

            **Última atualização do tutorial:** Jan/2021

            **Desenvolvido por:** [Wellington Dantas] (https://wellingtondantas.com.br)
        """
    )


def text():
    st.title('Títulos, Texto, Links e Pontos')

    st.markdown(
        """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

            **👈 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

            ### Want to learn more?

            - Google [google.com](https://google.com)
            - Python [python.org](https://python.org)
            - Streamlit [streamlit.io](https://www.streamlit.io)

            ### See more complex demos

            - Use a neural net to [analyze the Udacity Self-driving Car Image
            Dataset] (https://github.com/streamlit/demo-self-driving)
            - Explore a [New York City rideshare dataset]
            (https://github.com/streamlit/demo-uber-nyc-pickups)
        """
    )

def dataframe():
    st.title('Dataframe')

def plot():
    st.title('Plots')
