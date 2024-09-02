import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os

# Configuração do escopo e autenticação
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(os.getcwd(), "cred.json"), scope)
client = gspread.authorize(creds)

# Acessando a planilha
spreadsheet = client.open("CONTROLEGERENCIALPERDCOMP")  # Substitua pelo nome da sua planilha

sheet1 = spreadsheet.worksheet("TRIBUTOS_COMPENSADOS")
data = sheet1.get_all_records()
df_1 = pd.DataFrame(data)
#print(df.dtypes)

sheet2 = spreadsheet.worksheet("PERCOMPS")
data2 = sheet2.get_all_records()
df_2 = pd.DataFrame(data2)

sheet3 = spreadsheet.worksheet("SALDO_DE_CREDITO")
data3 = sheet3.get_all_records()
df_3 = pd.DataFrame(data3)
#st.title("Dados do Google Sheets")
#st.write(df_1, df_2, df_3)

with st.form(key= "incluir_analista"):
    input_nome = st.text_input(label= "Insira seu email")
    input_cargo= st.selectbox("Selecione seu cargo", options= ["Analista Tributário", "Gerente/Supervisor Tributário"])
    input_cliente = st.text_input(label = "Insira o CNPJ do Cliente")
    input_button_submit = st.form_submit_button("Identificar-se")

# if input_button_submit:
#     st.write(df_1)
