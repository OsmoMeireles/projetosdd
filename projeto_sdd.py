import sre_parse

import pandas
import pandas as pd
from openpyxl import Workbook, load_workbook
import streamlit as st
import numpy as np
import datetime as dt
from colorama import Fore
from pandas.core.interchange.dataframe_protocol import DataFrame

#SOLICITAÇÃO OTR
tabela = pd.read_excel('PROJETO SDD.xlsx')

solAMPM = tabela.groupby(['PERÍODO', 'DATA', 'VAN SDD', 'VUC SDD'], as_index = False) ['UTILITÁRIOS SDD'].sum()
solAM = solAMPM.loc[solAMPM['PERÍODO']=='AM']
solPM = solAMPM.loc[solAMPM['PERÍODO']=='PM']
print(solAMPM)

#CALENDARIZAÇÃO
calen = tabela.groupby(['TIPO', 'DATA', 'VAN SDD', 'VUC SDD'], as_index = False) ['UTILITÁRIOS SDD'].sum()
calenDIA = calen.loc[calen['TIPO']=='CALEN.']
print(calenDIA)

# ROTEIRIZAÇÃO
tabelarot = pd.read_excel(r'PROJETO SDD.xlsx', sheet_name='Planilha2')

rotAMPM = tabelarot.groupby(['PERÍODO', 'DATA', 'VAN SDD', 'VUC SDD'], as_index = False) ['UTILITÁRIOS SDD'].sum()
rotAM = rotAMPM.loc[rotAMPM['PERÍODO']=='AM']
rotPM = rotAMPM.loc[rotAMPM['PERÍODO']=='PM']
print(rotAMPM)

# DISPONIBILIZADO TRANSPORTADORA

disptp = tabela.groupby(['TIPO', 'DATA', 'VAN SDD', 'VUC SDD'], as_index = False) ['UTILITÁRIOS SDD'].sum()
dispTPDIA = disptp.loc[disptp['TIPO']=='DISP TP']
print(dispTPDIA)

st.set_page_config(layout='wide')

with st.container():
    st.title('PROJETO: FROTA SDD')
    st.write('Informações sobre Frota SDD a partir de jan/25 até a presente data')

with st.container():
    st.sidebar.header('Filtros')

@st.cache_data
def carregar_dados():
    df = pd.read_excel('PROJETO SDD.xlsx')
    return tabela

with st.container():
    st.write('---')
    tabela = carregar_dados()
    st.write('DISPONIBILIZADO PELA TRANSPORTADORA P/ CARREGAMENTO')
    st.dataframe(dispTPDIA)
    datatp = {'UTILITÁRIOS SDD': [dispTPDIA], 'VAN SDD': [dispTPDIA], 'VUC SDD': [dispTPDIA]}
    df = pd.DataFrame(dispTPDIA)
    total_coluna1 = df[['UTILITÁRIOS SDD']].sum()
    total_coluna2 = df[['VAN SDD']].sum()
    total_coluna3 = df[['VUC SDD']].sum()

    st.write("TOTAL UTILITÁRIOS SDD:")
    st.dataframe(total_coluna1)

    st.write("TOTAL VAN SDD:")
    st.dataframe(total_coluna2)

    st.write("TOTAL VUC SDD:")
    st.dataframe(total_coluna3)

with st.container():
    st.write('---')
    tabelarot = carregar_dados()
    st.write('ROTEIRIZAÇÃO AM')
    st.dataframe(data=rotAM)
    datarotam = {'UTILITÁRIOS SDD': [rotAM], 'VAN SDD': [rotAM], 'VUC SDD': [rotAM]}
    df = pd.DataFrame(rotAM)
    total_coluna1 = df[['UTILITÁRIOS SDD']].sum()
    total_coluna2 = df[['VAN SDD']].sum()
    total_coluna3 = df[['VUC SDD']].sum()

    st.write("TOTAL ROTEIRIZADO UTILITÁRIOS SDD AM:")
    st.dataframe(total_coluna1)

    st.write("TOTAL ROTEIRIZADO VAN SDD AM:")
    st.dataframe(total_coluna2)

    st.write("TOTAL ROTEIRIZADO VUC SDD AM:")
    st.dataframe(total_coluna3)

    st.write('ROTEIRIZAÇÃO PM')
    st.dataframe(data=rotPM)
    datarotpm = {'UTILITÁRIOS SDD': [rotPM], 'VAN SDD': [rotPM], 'VUC SDD': [rotPM]}
    df = pd.DataFrame(rotPM)
    total_coluna1 = df[['UTILITÁRIOS SDD']].sum()
    total_coluna2 = df[['VAN SDD']].sum()
    total_coluna3 = df[['VUC SDD']].sum()

    st.write("TOTAL ROTEIRIZADO UTILITÁRIOS SDD PM:")
    st.dataframe(total_coluna1)

    st.write("TOTAL ROTEIRIZADO VAN SDD PM:")
    st.dataframe(total_coluna2)

    st.write("TOTAL ROTEIRIZADO VUC SDD PM:")
    st.dataframe(total_coluna3)

with st.container():
    st.write('---')
    tabela = carregar_dados()
    st.write('SOLICITADO PELO OTR P/ CARREGAMENTO AM')
    st.dataframe(data=solAM)
    datasolam = {'UTILITÁRIOS SDD': [solAM], 'VAN SDD': [solAM], 'VUC SDD': [solAM]}
    df = pd.DataFrame(solAM)
    total_coluna1 = df[['UTILITÁRIOS SDD']].sum()
    total_coluna2 = df[['VAN SDD']].sum()
    total_coluna3 = df[['VUC SDD']].sum()

    st.write("TOTAL SOLICITADO UTILITÁRIOS SDD AM:")
    st.dataframe(total_coluna1)

    st.write("TOTAL SOLICITADO VAN SDD AM:")
    st.dataframe(total_coluna2)

    st.write("TOTAL SOLICITADO VUC SDD AM:")
    st.dataframe(total_coluna3)


    st.write('SOLICITADO PELO OTR P/ CARREGAMENTO PM')
    st.dataframe(data=solPM)
    datasolpm = {'UTILITÁRIOS SDD': [solPM], 'VAN SDD': [solPM], 'VUC SDD': [solPM]}
    df = pd.DataFrame(solPM)
    total_coluna1 = df[['UTILITÁRIOS SDD']].sum()
    total_coluna2 = df[['VAN SDD']].sum()
    total_coluna3 = df[['VUC SDD']].sum()

    st.write("TOTAL SOLICITADO UTILITÁRIOS SDD PM:")
    st.dataframe(total_coluna1)

    st.write("TOTAL SOLICITADO VAN SDD PM:")
    st.dataframe(total_coluna2)

    st.write("TOTAL SOLICITADO VUC SDD PM:")
    st.dataframe(total_coluna3)

with st.container():
    st.write('---')
    tabela = carregar_dados()
    st.write('CALENDARIZAÇÃO')
    st.dataframe(data=calenDIA)
    datacal = {'UTILITÁRIOS SDD': [calenDIA], 'VAN SDD': [calenDIA], 'VUC SDD': [calenDIA]}
    df = pd.DataFrame(calenDIA)
    total_coluna1 = df[['UTILITÁRIOS SDD']].sum()
    total_coluna2 = df[['VAN SDD']].sum()
    total_coluna3 = df[['VUC SDD']].sum()

    st.write("TOTAL UTILITÁRIOS SDD:")
    st.dataframe(total_coluna1)

    st.write("TOTAL VAN SDD:")
    st.dataframe(total_coluna2)

    st.write("TOTAL VUC SDD:")
    st.dataframe(total_coluna3)


with st.container():
    st.write('---')
    st.caption('Desenvolvido por: Osmo Meireles | Contato: osmo.cmeireles@mercadolivre.com')
