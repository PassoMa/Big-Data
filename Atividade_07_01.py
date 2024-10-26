import pandas as pd
import numpy as np

print('-----------OBTENDO DADOS-----------')

endereco_dados = 'BASES\Titanic.csv'
df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

print('\n----------EXIBINDO A BASE DE DADOS----------')
print(df_titanic.head())

array_ticket = np.array(df_titanic['Fare'])

media_ticket = np.mean(array_ticket)
mediana_ticket = np.median(array_ticket)

print('\n----- OBTENDO INFORMAÇOES SOBRE TARIFAS PAGAS PELOS PASSAGEIROS  -----')
print((f"A média das tarifas pagas pelos passageiros é R$ {media_ticket:.2f}"))
print((f"A mediana das tarifas pagas pelos passageiros é R$ {mediana_ticket:.2f}"))