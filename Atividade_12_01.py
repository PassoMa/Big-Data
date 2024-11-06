import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('---- OBTENDO DADOS ----')

# Importando a base de dados 
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
df_aisp_recuperacao_veiculos = df_ocorrencias[['aisp','ano','recuperacao_veiculos']]
df_aisp_recuperacao_veiculos = df_aisp_recuperacao_veiculos[df_aisp_recuperacao_veiculos['ano'].isin([2022,2023])]
df_aisp_recuperacao_veiculos = df_aisp_recuperacao_veiculos.groupby(['aisp']).sum(['recuperacao_veiculos']).reset_index() #groupby = agrupamento

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_aisp_recuperacao_veiculos.head())

# Criando o array 
array_aisp = np.array(df_aisp_recuperacao_veiculos["aisp"])
array_recuperacao_veiculos = np.array(df_aisp_recuperacao_veiculos["recuperacao_veiculos"])

# Obtendo a média
media_recuperacao_veiculos = np.mean(array_recuperacao_veiculos)

# Obtendo o maior e o menor 
maior_recuperacao_veiculos = np.max(array_recuperacao_veiculos)
menor_recuperacao_veiculos= np.min(array_recuperacao_veiculos)

# Obtendo a mediana 
mediana_recuperacao_veiculos = np.median(array_recuperacao_veiculos)

# Obtendo a distância entre a média e a mediana 
distancia_recuperacao_veiculos = abs((media_recuperacao_veiculos - mediana_recuperacao_veiculos) / mediana_recuperacao_veiculos) * 100

# Obtendo o máximo e o mínimo 
maximo_recuperacao_veiculos = np.max(array_recuperacao_veiculos)
minimo_recuperacao_veiculos = np.min(array_recuperacao_veiculos)

# Obtendo a amplitude 
amplitude_recuperacao_veiculos = maximo_recuperacao_veiculos - minimo_recuperacao_veiculos

# Obtendo os Quartis 
q1_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.25, method='weibull')
q2_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.50, method='weibull')
q3_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.75, method='weibull')
iqr_recuperacao_veiculos = q3_recuperacao_veiculos - q1_recuperacao_veiculos

# Identificando os outliers superiores e inferiores
limite_superior_recuperacao_veiculos = q3_recuperacao_veiculos + (1.5 * iqr_recuperacao_veiculos)
limite_inferior_recuperacao_veiculos = q1_recuperacao_veiculos - (1.5 * iqr_recuperacao_veiculos)

# Filtrando o DataFrame
df_recuperacao_veiculos_outliers_superiores = df_aisp_recuperacao_veiculos[df_aisp_recuperacao_veiculos['recuperacao_veiculos'] > limite_superior_recuperacao_veiculos]
df_recuperacao_veiculos_outliers_inferiores = df_aisp_recuperacao_veiculos[df_aisp_recuperacao_veiculos['recuperacao_veiculos'] < limite_inferior_recuperacao_veiculos]

# Obtendo as medidadas de dispersão 
variancia_recuperacao_veiculos = np.var(array_recuperacao_veiculos)
distancia_var_recuperacao_veiculos = variancia_recuperacao_veiculos / (media_recuperacao_veiculos**2)  #dois ** é para elevar ao quadrado
desvio_padrao_recuperacao_veiculos = np.std(array_recuperacao_veiculos)
coeficiente_var_recuperacao_veiculos = desvio_padrao_recuperacao_veiculos / media_recuperacao_veiculos



print("\n-- OBTENDO INFORMAÇÕES OS ROUBOS DE VEÍCULOS --")
print('---------------Medidas de Tendência Central-----------------')
print(f"\nA média de recuperação de veículos é {media_recuperacao_veiculos:.0f}")
print(f"A mediana de recuperação de veículos s é {mediana_recuperacao_veiculos:.0f}")
print(f"A distância entre a média e a mediana é {distancia_recuperacao_veiculos:.2f} %")
print(f"O menor valor de recuperação de veículos  é {minimo_recuperacao_veiculos:0f}")
print(f"O maior valor de recuperação de veículos  é {maximo_recuperacao_veiculos:.0f}")
print(f"A amplitude das recuperações de veículos  é {amplitude_recuperacao_veiculos:.0f}")
print(f"O valor do q1 - 25% do valor de recuperação de veículos  é {q1_recuperacao_veiculos:.2f}")
print(f"O valor do q2 - 50% do valor de recuperação de veículos  é {q2_recuperacao_veiculos:.2f}")
print(f"O valor do q3 - 75% do valor de recuperação de veículos  é  {q3_recuperacao_veiculos:.2f}")
print(f"O valor do iqr = q3 - q1 do valor de v é {iqr_recuperacao_veiculos:.2f}")
print(f"O limite inferior do valor de recuperação de veículos  é {limite_inferior_recuperacao_veiculos:.2f}")
print(f"O limite superior do valor de recuperação de veículos  é {limite_superior_recuperacao_veiculos:.2f}")

print(f"A variância de recuperação de veículos  é {variancia_recuperacao_veiculos:.2f}")
print(f"A distancia da variância X média do recuperação de veículos é {distancia_var_recuperacao_veiculos:.2f}")
print(f"O desvio padrão da recuperação de veículos  é {desvio_padrao_recuperacao_veiculos:.2f}")
print(f"O coeficiente da variação da recuperação de veículos  é {coeficiente_var_recuperacao_veiculos:.2f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_recuperacao_veiculos_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_recuperacao_veiculos_outliers_superiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_recuperacao_veiculos_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_recuperacao_veiculos_outliers_superiores)



#Vizualizando os dados 
print('\nVIZUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7)) #Cria a divisão da tabela
plt.suptitle('Analise de dados sobre a Recuperação de Veículos ') #Cria o título da tabela 

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot da Recuperação de Veículos')
plt.boxplot(array_recuperacao_veiculos,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos (possivel observar como os dados estão distribuidos)
plt.subplot(2,2,2)
plt.title('Histograma da Recuperação de Veículos')
plt.hist(array_recuperacao_veiculos,bins=100,edgecolor='black')

# posição 03: Medidas descritivas 
plt.subplot(2,2,3)
df_recuperacao_veiculos_outliers_superiores_order = df_recuperacao_veiculos_outliers_superiores.sort_values(by='recuperacao_veiculos',ascending=True)
plt.title('Ranking dos Batalhões com Outliers Superiores')
plt.barh(df_recuperacao_veiculos_outliers_superiores_order['aisp'].astype(str),df_recuperacao_veiculos_outliers_superiores_order['recuperacao_veiculos'])

# posição 04: Medidas descritivas (detalhamento das medidas estatísticas)
plt.subplot(2,2,4)
plt.title('Medidas Descritivas das Recuperações de Veículos')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos Veículos Recuperados {media_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos Veículos Recuperados {mediana_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos Veículos Recuperados {distancia_recuperacao_veiculos:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos Veículos Recuperados {maximo_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos Veículos Recuperados {minimo_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos Veículos Recuperados {distancia_var_recuperacao_veiculos:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos Veículos Recuperados {coeficiente_var_recuperacao_veiculos:.2f}',fontsize=12)


#Exibindo o Painel
plt.tight_layout() #Distribuiu o grafico da melhor forma (formata o painel)
plt.show()