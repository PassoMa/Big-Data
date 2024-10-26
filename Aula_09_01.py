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

#Obendo os Quartis da renda - Método weibull
q1_renda = np.quantile(array_financeira_renda, 0.25, method='weibull') #quantile = calcula os quartis
q2_renda = np.quantile(array_financeira_renda, 0.50, method='weibull')
q3_renda = np.quantile(array_financeira_renda, 0.75, method='weibull')
iqr_renda = q3_renda - q1_renda

#Identificando os outliers superiores e inferiores da renda 
limite_superior_renda = q3_renda + (1.5 * iqr_renda) #1.5 = valor de 50% - valor padrão para este calculo
limite_inferior_renda = q1_renda - (1.5 * iqr_renda) 

#Filtrando o DataFrame financeira / Renda
df_financeira_renda_outliers_superiores = df_financeira[df_financeira['Renda'] > limite_superior_renda]
df_financeira_renda_outliers_inferiores = df_financeira[df_financeira['Renda'] < limite_inferior_renda]

#Obendo os Quartis  do valor emprestado 
q1_emprestimo = np.quantile(array_financeira_Vlr_emprestado, 0.25, method='weibull') #quantile = calcula os quartis
q2_emprestimo = np.quantile(array_financeira_Vlr_emprestado, 0.50, method='weibull')
q3_emprestimo = np.quantile(array_financeira_Vlr_emprestado, 0.75, method='weibull')
iqr_emprestimo = q3_emprestimo - q1_emprestimo

#Identificando os outliers superiores e inferiores  do valor emprestado 
limite_superior_emprestimo = q3_emprestimo + (1.5 * iqr_emprestimo) #1.5 = valor de 50% - valor padrão para este calculo
limite_inferior_emprestimo = q1_emprestimo - (1.5 * iqr_emprestimo) 

#Filtrando o DataFrame financeira/ Emprestado
df_financeira_emprestimo_outliers_superiores = df_financeira[df_financeira['Vlr_emprestado'] > limite_superior_emprestimo]
df_financeira_emprestimo_outliers_inferiores = df_financeira[df_financeira['Vlr_emprestado'] < limite_inferior_emprestimo]

print('\n----- OBTENDO INFORMAÇOES SOBRE RENDA -----')
print('\nMedidas de Tendência Central')
print((f"A média das rendas dos clientes é R$ {media_renda:.2f}"))
print((f"A mediana das rendas dos clientes é R$ {mediana_renda:.2f}"))
print((f"A distância entre a média e mediana das rendas dos clientes é: {distancia_renda:.2f}%"))
print((f"A maior rendas dos clientes é R$ {maior_renda:.2f}"))
print((f"A maior valor das rendas dos clientes é R$ {maior_renda:.2f}"))
print((f"O menor valor das rendas dos clientes é R$ {menor_renda:.2f}"))
print((f"A amplitude das rendas dos clientes é R$ {amplitude_renda:.2f}"))
print(f"O valor do q1 - 25% da renda é R$ {q1_renda}")
print(f"O valor do q2 - 50% da renda é R$ {q1_renda}")
print(f"O valor do q1 - 75% da renda é R$ {q1_renda}")
print(f"O valor do iqr = q3 - q1 da renda é R$ {iqr_renda}")
print(f"O limite inferior da renda é R$ {limite_inferior_renda}")
print(f"O limite superior da renda é R$ {limite_superior_renda}")
print('\n -Verificando a existência de outliers inferiores -')
if len(df_financeira_renda_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_renda_outliers_inferiores) 
print('\n -Verificando a existência de outliers superiores -')
if len(df_financeira_renda_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_renda_outliers_superiores)       

print('\n----- OBTENDO INFORMAÇOES SOBRE EMPRÉSTIMO-----')
print((f"A média dos empréstimos dos clientes é R$ {media_Vlr_emprestado:.2f}"))
print((f"A mediana dos empréstimos dos clientes é R$ {mediana_Vlr_emprestado:.2f}"))
print((f"A distância entre a média e mediana dos empréstimos dos clientes é:  {distancia_Vlr_emprestado:.2f}%"))
print((f"O maior valor dos empréstimos dos clientes é R$ {maior_Vlr_emprestado:.2f}"))
print((f"O menor valor dos empréstimos dos clientes é R$ {menor_Vlr_emprestado:.2f}"))
print((f"A amplitude dos empréstimos dos clientes é R$ {amplitude__Vlr_emprestado:.2f}"))
print(f"O valor do q1 - 25% do empréstimo é R$ {q1_emprestimo}")
print(f"O valor do q2 - 50% do empréstimo é R$ {q2_emprestimo}")
print(f"O valor do q1 - 75% do empréstimo é R$ {q3_emprestimo}")
print(f"O valor do iqr = q3 - q1 do empréstimo é R$ {iqr_renda}")
print(f"O limite inferior do emprestimo é R$ {limite_inferior_emprestimo}")
print(f"O limite superior do emprétimo é R$ {limite_superior_emprestimo}")
print('\n -Verificando a existência de outliers inferiores -')
if len(df_financeira_emprestimo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_emprestimo_outliers_inferiores) 
print('\n -Verificando a existência de outliers superiores -')
if len(df_financeira_emprestimo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_emprestimo_outliers_superiores)       