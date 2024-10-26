#numpy = Biblioteca para cálculos

import pandas as pd
import numpy as np

print('-----------OBTENDO DADOS-----------')

endereco_dados = 'BASES\Financeira.csv'
df_financeira = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

print('\n----------EXIBINDO A BASE DE DADOS----------')
print(df_financeira.head())

#Obtendo dados sobre renda e valor emprestado
array_financeira_renda = np.array(df_financeira["Renda"])
array_financeira_Vlr_emprestado = np.array(df_financeira["Vlr_emprestado"])
#cálculos das médias
media_renda = np.mean(array_financeira_renda)
media_Vlr_emprestado = np.mean(array_financeira_Vlr_emprestado)
#cálculos das medianas
mediana_renda = np.median(array_financeira_renda)
mediana_Vlr_emprestado = np.median(array_financeira_Vlr_emprestado)

distancia_renda = abs((media_renda - mediana_renda) / mediana_renda) * 100 #asb = valor absoluto
distancia_Vlr_emprestado = abs((media_Vlr_emprestado - mediana_Vlr_emprestado) / mediana_Vlr_emprestado) * 100

maior_renda = np.max(array_financeira_renda)
maior_Vlr_emprestado = np.max(array_financeira_Vlr_emprestado)
menor_renda = np.min(array_financeira_renda)
menor_Vlr_emprestado = np.min(array_financeira_Vlr_emprestado)

amplitude_renda = maior_renda - menor_renda
amplitude__Vlr_emprestado = maior_Vlr_emprestado - menor_Vlr_emprestado

print('\n----- OBTENDO INFORMAÇOES SOBRE RENDA -----')
print((f"A média das rendas dos clientes é R$ {media_renda:.2f}"))
print((f"A mediana das rendas dos clientes é R$ {mediana_renda:.2f}"))
print((f"A distância entre a média e mediana das rendas dos clientes é: {distancia_renda:.2f}%"))
print((f"A maior rendas dos clientes é R$ {maior_renda:.2f}"))
print((f"A maior valor das rendas dos clientes é R$ {maior_renda:.2f}"))
print((f"O menor valor das rendas dos clientes é R$ {menor_renda:.2f}"))
print((f"A amplitude das rendas dos clientes é R$ {amplitude_renda:.2f}"))

print('\n----- OBTENDO INFORMAÇOES SOBRE EMPRÉSTIMO-----')
print((f"A média dos empréstimos dos clientes é R$ {media_Vlr_emprestado:.2f}"))
print((f"A mediana dos empréstimos dos clientes é R$ {mediana_Vlr_emprestado:.2f}"))
print((f"A distância entre a média e mediana dos empréstimos dos clientes é:  {distancia_Vlr_emprestado:.2f}%"))
print((f"O maior valor dos empréstimos dos clientes é R$ {maior_Vlr_emprestado:.2f}"))
print((f"O menor valor dos empréstimos dos clientes é R$ {menor_Vlr_emprestado:.2f}"))
print((f"A amplitude dos empréstimos dos clientes é R$ {amplitude__Vlr_emprestado:.2f}"))



