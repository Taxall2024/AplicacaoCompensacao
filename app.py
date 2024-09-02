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
spreadsheet = client.open("CONTROLEGERENCIALPERDCOMP") 

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

#st.title("")

with st.form(key= "incluir_usuario"):
    input_nome = st.text_input(label= "Insira seu email")
    input_cargo= st.selectbox("Selecione seu cargo", options= ["Analista Tributário", "Gerente/Supervisor Tributário"])
    #input_cliente = st.text_input(label = "Insira o CNPJ do Cliente")
    input_button_submit = st.form_submit_button("Identificar-se")

if input_button_submit:
    if input_cargo == "Analista Tributário":
        #st.write(df_1)
        st.subheader("Tributos Compensados")
        with st.form(key= "incluir_compensacoes"):
            input_perdcomp = st.text_input(label= "Número de PERDCOMP")
            input_tipo_credito = st.text_input (label = "Tipo de Crédito")
            input_periodo_credito = st.text_input( label= "Periodo do Crédito")
            input_tributo = st.text_input(label = "Tributo")
            input_cod_darf = st.text_input(label= "Código DARF")
            #input_competencia = st.
            input_button_submit = st.form_submit_button("Atualizar")
        
        # def read_data(sheet_name):
        # sheet = spreadsheet.worksheet(sheet_name)
        # data = sheet.get_all_records()
        # return pd.DataFrame(data)
    
        # def add_data(sheet_name, new_row):
        # sheet = spreadsheet.worksheet(sheet_name)
        # sheet.append_row(new_row)

        # def update_data(sheet_name, row, col, value):
        # sheet = spreadsheet.worksheet(sheet_name)
        # sheet.update_cell(row, col, value)

        # def delete_data(sheet_name, row):
        # sheet = spreadsheet.worksheet(sheet_name)
        # sheet.delete_row(row)

    else:
        st.write(df_3)


    
