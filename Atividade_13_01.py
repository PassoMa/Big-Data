#DataFrame = conjunto de dados tabulados- 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

print('---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
df_aisp_cvli = df_ocorrencias[['aisp','ano','cvli']]
df_aisp_cvli = df_aisp_cvli.groupby(['aisp']).sum(['aisp']).reset_index() #groupby = agrupamento 

print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_aisp_cvli.head())

array_aisp = np.array(df_aisp_cvli["aisp"])
array_cvli = np.array(df_aisp_cvli["cvli"])

media_cvli = np.mean(array_cvli)

mediana_cvli = np.median(array_cvli)

distancia_cvli  = abs((media_cvli  - mediana_cvli ) / mediana_cvli ) * 100

maximo_cvli = np.max(array_cvli)
minimo_cvli = np.min(array_cvli)

amplitude_cvli = maximo_cvli - minimo_cvli

q1_cvli = np.quantile(array_cvli, 0.25, method='weibull')
q2_cvli = np.quantile(array_cvli, 0.50, method='weibull')
q3_cvli = np.quantile(array_cvli, 0.75, method='weibull')
iqr_cvli = q3_cvli - q1_cvli

limite_superior_cvli = q3_cvli + (1.5 * iqr_cvli)
limite_inferior_cvli = q1_cvli - (1.5 * iqr_cvli)

df_cvli_outliers_superiores = df_aisp_cvli[df_aisp_cvli['cvli'] > limite_superior_cvli]
df_cvli_outliers_inferiores = df_aisp_cvli[df_aisp_cvli['cvli'] < limite_inferior_cvli]

variancia_cvli = np.var(array_cvli)
distancia_var_cvli = variancia_cvli / (media_cvli**2)  #dois ** é para elevar ao quadrado
desvio_padrao_cvli = np.std(array_cvli)
coeficiente_var_cvli = desvio_padrao_cvli / media_cvli

print("\n-- OBTENDO INFORMAÇÕES SOBRE CRIMES VIOLENTOS LETAIS INTENCIONAIS (CVLI) --")
print('---------------Medidas de Tendência Central-----------------')
print(f"\nA média de CVLI é {media_cvli:.0f}")
print(f"A mediana de CVLI é {mediana_cvli:.0f}")
print(f"A distância entre a média e a mediana é {distancia_cvli:.2f} %")
print(f"O menor valor de CVLI  é {minimo_cvli:0f}")
print(f"O maior valor de CVLI  é {maximo_cvli:.0f}")
print(f"A amplitude dos CVLI é {amplitude_cvli:.0f}")
print(f"O valor do q1 - 25% do valor de CVLI é {q1_cvli:.2f}")
print(f"O valor do q2 - 50% do valor de CVLI  é {q2_cvli:.2f}")
print(f"O valor do q3 - 75% do valor de CVLI  é  {q3_cvli:.2f}")
print(f"O valor do iqr = q3 - q1 do valor de CVLI é {iqr_cvli:.2f}")
print(f"O limite inferior do valor de CVLI é {limite_inferior_cvli:.2f}")
print(f"O limite superior do valor de CVLI é {limite_superior_cvli:.2f}")

print(f"A variância de CVLI  é {variancia_cvli:.2f}")
print(f"A distancia da variância X média do CVLI é {distancia_var_cvli:.2f}")
print(f"O desvio padrão da CVLI  é {desvio_padrao_cvli:.2f}")
print(f"O coeficiente da variação do CVLI  é {coeficiente_var_cvli:.2f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_cvli_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_cvli_outliers_superiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_cvli_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_cvli_outliers_superiores)

print('\nVIZUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7)) 
plt.suptitle('Analise de dados sobre Crimes Violentos Letais Intencionais - CVLI',fontweight='bold', color='black',fontsize=15) 

plt.subplot(2,2,1)
plt.title('BoxPlot dos CVLI',fontweight='bold', color='navy')
plt.boxplot(array_cvli,vert=False,showmeans=True)

plt.subplot(2,2,2)
plt.title('Histograma dos CVLI',fontweight='bold', color='navy')
#plt.hist(array_cvli,bins=100,edgecolor='black') #bins= dimenção do histograma
plt.hist(array_cvli, bins=100, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel("Número de CVLI") #escrita abaixo descritiva da tabela
plt.ylabel("Frequência")#escrita lateral descritiva da tabela

plt.subplot(2,2,3)
df_cvli_outliers_superiores_order = df_cvli_outliers_superiores.sort_values(by='cvli',ascending=True)
plt.title('Ranking dos Batalhões com Outliers Superiores',fontweight='bold', color='navy')
plt.barh(df_cvli_outliers_superiores_order['aisp'].astype(str),df_cvli_outliers_superiores_order['cvli'])
cores = ['red']  # Ajuste para o número de barras
plt.barh(df_cvli_outliers_superiores_order['aisp'].astype(str), df_cvli_outliers_superiores_order['cvli'], color=cores[:len(df_cvli_outliers_superiores_order)])

# posição 04: Medidas descritivas (detalhamento das medidas estatísticas)
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos CVLI',fontweight='bold', color='navy')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos CVLI {media_cvli:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos CVLI {mediana_cvli:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos CVLI {distancia_cvli:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos CVLI {maximo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos CVLI {minimo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos CVLI {distancia_var_cvli:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos CVLI {coeficiente_var_cvli:.2f}',fontsize=12)



#Exibindo o Painel
plt.tight_layout() #Distribuiu o grafico da melhor forma (formata o painel)
plt.show()