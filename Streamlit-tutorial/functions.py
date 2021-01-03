#Functions utils to development fast

def main():
    #libs
    import streamlit as st

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
    #libs
    import streamlit as st

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
            - Docs [download](https://docs.streamlit.io/_/downloads/en/latest/pdf/)
        """
    )

def image():
    #libs
    import streamlit as st
    import pandas as pd
    import numpy as np
    from PIL import Image

    st.title('Imagem')
    image = Image.open('resources/img/fortaleza-city.png')
    st.image(image, caption='Beautiful Fortaleza City', use_column_width=True)

    st.title('Mapa')
    map_data = pd.DataFrame(np.random.randn(25, 2) / [50, 50] + [-3.7381, -38.5350], columns=['lat', 'lon'])
    st.map(map_data)


def dataframe():
    #libs
    import streamlit as st
    import pandas as pd
    import numpy as np
    import pandas_datareader as web
    
    st.title('Tabelas de Dataframe')
    #Obtem os dados históricos
    df = web.DataReader('PETR4.SA', data_source='yahoo', start='2013-01-01', end='2021-01-02') 
    st.write("Histórico de Preços da Ação PETR4.SA") 
    st.dataframe(df)


def plot():
    #Libs
    import streamlit as st
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import pandas_datareader as web


    st.title('Plotagem de Sinal (Histograma)')
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.pyplot(fig)

    st.title('Plotagem de Sinal')
    df = web.DataReader('PETR4.SA', data_source='yahoo', start='2013-01-01', end='2021-01-02') 
    st.line_chart(df['Close'])