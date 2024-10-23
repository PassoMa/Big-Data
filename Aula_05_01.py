# pip install xlrd - Biblioteca para manipular arquivos xlsx
import pandas as pd
enderecos_dados = 'BASES\ENEM_2020_2023.xlsx'
df_enem = pd.read_excel(enderecos_dados)

print('----------BASE DE DADOS ENEM-----------')
print(df_enem.head()) #HEAD = resumo de linha


