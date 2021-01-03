#Libs
import streamlit as st
import functions

from collections import OrderedDict

#Chamada de funções


FUNCTIONS = OrderedDict(
    [
        ('Início', (functions.main, None)),
        ('Títulos, Texto, Links e Pontos', (functions.text, None)),
        ('Dataframe', (functions.dataframe, None)),
        ('Plot', (functions.plot, None)),
    ]
)

def run():
    select = st.sidebar.selectbox('Escolha uma opção', list(FUNCTIONS.keys()),0)
    selected = FUNCTIONS[select][0]
    selected()


if __name__ == "__main__":
    run()

