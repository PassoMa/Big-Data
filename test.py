import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('---- OBTENDO DADOS ----')

# Importando a base de dados financeira.csv
endereco_dados = 'BASES\Titanic.csv'

# Criando o DataFrame financeira
df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_fare_age = df_titanic[['Name','Age','Fare','Survived']]

# Exibindo a base de dados financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_titanic.head())
print(df_fare_age.head())
