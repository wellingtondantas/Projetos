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

def htmlcss():
    #Libs
    import streamlit as st
    import streamlit.components.v1 as components

    st.title('Inserir HTML/CSS')

    st.markdown("<h1 style='color:#F00;'>H1 com cor RED</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#0F0;'>H2 com cor GREEN</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#00F;'>H3 com cor BLUE</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color:#F00; font-family:arial'>H1 com cor RED e Arial</h1>", unsafe_allow_html=True)

    st.title('Inserir Iframe')
    components.iframe("https://tecnothink.com.br", height=600)


    st.title('HTML/CSS Puro')
    components.html(
        """
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <div id="accordion">
            <div class="card">
                <div class="card-header" id="headingOne">
                    <h5 class="mb-0">
                        <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                        Item #1
                        </button>
                    </h5>
                </div>
                <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
                    <div class="card-body">
                        Item #1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                    </div>
                </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingTwo">
                    <h5 class="mb-0">
                        <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                        Item #2
                        </button>
                    </h5>
                </div>
                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                    <div class="card-body">
                        Item #2 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    </div>
                </div>
            </div>
            </div>
        """,
        height=400,
    )


def inputs():
    #Libs
    import streamlit as st
    import pandas as pd
    import numpy as np
    import datetime
    

    st.title('Tipos de Entradas')

    info1 = st.slider("Selecione o Ano", 1920, 1995, 2021)
    info2 = st.slider("Selecione o Mês", 1, 12, 6)
    info3 = st.slider("Selecione o Dia", 1, 31, 15)

    info4 = st.date_input("Qual a data de seu anivesário", datetime.date(2019, 7, 6))

    info5 = st.text_input('Digite seu Nome')

    info6 = st.number_input(label='Informe sua idade', min_value=0, max_value=120, value=20, step=1, format=None, key=None)
    info7 = st.number_input(label='Informe seu Peso', min_value=0.0, max_value=200.0, value=20.0, step=0.5, format=None, key=None)

    info8 = st.text_area('Mensagem de Texto', 'Lorem ipsum')

    info9 = st.file_uploader("Escolha o arquivo")
    if info9 is not None:
        #Ler arquivo csv
        dataframe = pd.read_csv(info9)
        st.write(dataframe)

    info10 = st.file_uploader("Escolha um arquivo CSV", accept_multiple_files=True)
    for i in info10:
        bytes_data = i.read()
        st.write("Nome do Arquivo:", i.name)
        st.write(bytes_data)


    info11 = st.selectbox("Qual a sua cor favorita?", ("Verde", "Azul", "Amarelo"))

    info12 = st.multiselect("Quais países você conhece?",  ['EUA', 'Canadá', 'Portugal','Alemanha', 'China'])

    if st.checkbox('Apresenta dataframe'):
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
        st.line_chart(chart_data)


