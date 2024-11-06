import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('---- OBTENDO DADOS ----')

# Importando a base de dados 
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
df_cisp_roubo = df_ocorrencias[['cisp','roubo_veiculo']]
df_cisp_roubo = df_cisp_roubo.groupby(['cisp']).sum(['roubo_veiculo']).reset_index() #groupby = agrupamento

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_cisp_roubo.head())

# Criando o array 
array_cisp = np.array(df_cisp_roubo["cisp"])
array_roubo_veiculo = np.array(df_cisp_roubo["roubo_veiculo"])

# Obtendo a média
media_roubo_veiculo = np.mean(array_roubo_veiculo)

# Obtendo o maior e o menor 
maior_roubo_veiculo = np.max(array_roubo_veiculo)
menor_roubo_veiculo= np.min(array_roubo_veiculo)

# Obtendo a mediana 
mediana_roubo_veiculo = np.median(array_roubo_veiculo)

# Obtendo a distância entre a média e a mediana 
distancia_roubo_veiculo = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo) * 100

# Obtendo o máximo e o mínimo 
maximo_roubo_veiculo = np.max(array_roubo_veiculo)
minimo_roubo_veiculo = np.min(array_roubo_veiculo)

# Obtendo a amplitude 
amplitude_roubo_veiculo = maximo_roubo_veiculo - minimo_roubo_veiculo

# Obtendo os Quartis 
q1_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
q2_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
q3_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.75, method='weibull')
iqr_roubo_veiculo = q3_roubo_veiculo - q1_roubo_veiculo

# Identificando os outliers superiores e inferiores
limite_superior_roubo_veiculo = q3_roubo_veiculo + (1.5 * iqr_roubo_veiculo)
limite_inferior_roubo_veiculo = q1_roubo_veiculo - (1.5 * iqr_roubo_veiculo)

# Filtrando o DataFrame
df_ocorrencias_roubo_veiculos_outliers_superiores = df_cisp_roubo[df_cisp_roubo['roubo_veiculo'] > limite_superior_roubo_veiculo]
df_ocorrencias_roubo_veiculos_outliers_inferiores = df_cisp_roubo[df_cisp_roubo['roubo_veiculo'] < limite_inferior_roubo_veiculo]

# Obtendo as medidadas de dispersão 
variancia_roubo_veiculo = np.var(array_roubo_veiculo)
distancia_var_roubo_veiculo = variancia_roubo_veiculo / (media_roubo_veiculo**2)  #dois ** é para elevar ao quadrado
desvio_padrao_roubo_veiculo = np.std(array_roubo_veiculo)
coeficiente_var_roubo_veiculo = desvio_padrao_roubo_veiculo / media_roubo_veiculo



print("\n-- OBTENDO INFORMAÇÕES OS ROUBOS DE VEÍCULOS --")
print('Medidas de Tendência Central')
print(f"\nA média de roubos de veículos é {media_roubo_veiculo:.0f}")
print(f"A mediana de roubos de veículos é {mediana_roubo_veiculo:.0f}")
print(f"A distância entre a média e a mediana é {distancia_roubo_veiculo:.2f} %")
print(f"O menor valor de roubos de veículos é {minimo_roubo_veiculo:0f}")
print(f"O maior valor de roubos de veículos é {maximo_roubo_veiculo:.0f}")
print(f"A amplitude dos roubos de veículos é {amplitude_roubo_veiculo:.0f}")
print(f"O valor do q1 - 25% do valor de roubos de veículos é {q1_roubo_veiculo:.2f}")
print(f"O valor do q2 - 50% do valor de roubos de veículos é {q2_roubo_veiculo:.2f}")
print(f"O valor do q3 - 75% do valor de roubos de veículos é  {q3_roubo_veiculo:.2f}")
print(f"O valor do iqr = q3 - q1 do valor de roubos de veículos é {iqr_roubo_veiculo:.2f}")
print(f"O limite inferior do valor de roubos de veículos é {limite_inferior_roubo_veiculo:.2f}")
print(f"O limite superior do valor de roubos de veículos é {limite_superior_roubo_veiculo:.2f}")

print(f"A variância de roubos de veículos é {variancia_roubo_veiculo:.2f}")
print(f"A distancia da variância X média do roubos de veículos é {distancia_var_roubo_veiculo:.2f}")
print(f"O desvio padrão do roubos de veículos é {desvio_padrao_roubo_veiculo:.2f}")
print(f"O coeficiente da variação do roubos de veículos é {coeficiente_var_roubo_veiculo:.2f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_ocorrencias_roubo_veiculos_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_ocorrencias_roubo_veiculos_outliers_superiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_ocorrencias_roubo_veiculos_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_ocorrencias_roubo_veiculos_outliers_superiores)



#Vizualizando os dados 
print('\nVIZUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7)) #Cria a divisão da tabela
plt.suptitle('Analise de dados sobre Roubo de Veículos') #Cria o título da tabela 

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot dos Roubos de Veículos')
plt.boxplot(array_roubo_veiculo,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,2)
plt.title('Histograma dos Roubos de Veículos')
plt.hist(array_roubo_veiculo,bins=100,edgecolor='black')

# posição 03: Medidas descritivas 
plt.subplot(2,2,3)
df_roubo_veiculo_outliers_superiores_order = df_ocorrencias_roubo_veiculos_outliers_superiores.sort_values(by='roubo_veiculo',ascending=True)
plt.title('Ranking das Delegacias com Outliers Superiores')
plt.barh(df_roubo_veiculo_outliers_superiores_order['cisp'].astype(str),df_roubo_veiculo_outliers_superiores_order['roubo_veiculo'])

# posição 04: Medidas descritivas 
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Roubos de Veículos')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos Roubos de Veículos {media_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos Roubos de Veículos {mediana_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos Roubos de Veículos {distancia_roubo_veiculo:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos Roubos de Veículos {maximo_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos Roubos de Veículos {minimo_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos Roubos de Veículos {distancia_var_roubo_veiculo:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos Roubos de Veículos {coeficiente_var_roubo_veiculo:.2f}',fontsize=12)


#Exibindo o Painel
plt.tight_layout() #Distribuiu o grafico da melhor forma (formata o painel)
plt.show()
