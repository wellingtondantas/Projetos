#Libs
import streamlit as st
import functions
import inspect
import textwrap

from collections import OrderedDict

#Chamada de funções
FUNCTIONS = OrderedDict(
    [
        ('Início', (functions.main, None)),
        ('Títulos, Texto, Links e Pontos', (functions.text, None)),
        ('Imagens e Mapas', (functions.image, None)),
        ('Tabelas de Dataframe', (functions.dataframe, None)),
        ('Plotagem de Sinal', (functions.plot, None)),
    ]
)

#Principal
def run():
    select = st.sidebar.selectbox('Escolha uma opção', list(FUNCTIONS.keys()),0)
    funcSelected = FUNCTIONS[select][0]
    funcSelected()

    if select == "Início" :
        show_code = False
    else:
        show_code = st.sidebar.checkbox('Ver código', False)

    if show_code:
        st.markdown("# Código")
        sourcelines, _ = inspect.getsourcelines(funcSelected)
        st.code(textwrap.dedent(''.join(sourcelines[1:])))

if __name__ == "__main__":
    run()

