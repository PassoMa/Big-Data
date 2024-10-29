import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados financeira.csv
endereco_dados = 'BASES\Titanic.csv'

# Criando o DataFrame financeira
df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_fare_age = df_titanic[['Name','Age','Fare']]

# Exibindo a base de dados financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_titanic.head())

# Criando o array do valor da passagem e da idade
array_titanic_fare = np.array(df_titanic["Fare"])
array_titanic_age = np.array(df_titanic["Age"])

# Obtendo a média do valor da passagem e da idade
media_fare = np.mean(array_titanic_fare)
media_age = np.mean(array_titanic_age)

# Obtendo a mediana do valor da passagem e da idade
mediana_fare = np.median(array_titanic_fare)
mediana_age = np.median(array_titanic_age)

# Obtendo a distância entre a média e a mediana do valor da passagem e da idade
distancia_fare = abs((media_fare - mediana_fare) / mediana_fare) * 100
distancia_age = abs((media_age - mediana_age) / mediana_age) * 100

# Obtendo o máximo e o mínimo do valor da passagem e da idade
maximo_fare = np.max(array_titanic_fare)
maximo_age = np.max(array_titanic_age)
minimo_fare = np.min(array_titanic_fare)
minimo_age = np.min(array_titanic_age)

# Obtendo a amplitude do valor da passagem e da idade
amplitude_fare = maximo_fare - minimo_fare
amplitude_age = maximo_age - minimo_age

q1_fare = np.quantile(array_titanic_fare, 0.25, method='weibull') #quantile = calcula os quartis
q2_fare = np.quantile(array_titanic_fare, 0.50, method='weibull')
q3_fare = np.quantile(array_titanic_fare, 0.75, method='weibull')
iqr_fare = q3_fare - q1_fare

limite_superior_fare = q3_fare + (1.5 * iqr_fare) #1.5 = valor de 50% - valor padrão para este calculo
limite_inferior_fare = q1_fare - (1.5 * iqr_fare) 

df_financeira_fare_outliers_superiores = df_fare_age[df_fare_age['Fare'] > limite_superior_fare]
df_financeira_fare_outliers_inferiores = df_fare_age[df_fare_age['Fare'] < limite_inferior_fare]


q1_age = np.quantile(array_titanic_age, 0.25, method='weibull') #quantile = calcula os quartis
q2_age = np.quantile(array_titanic_age, 0.50, method='weibull')
q3_age = np.quantile(array_titanic_age, 0.75, method='weibull')
iqr_age = q3_age - q1_age

limite_superior_age = q3_age + (1.5 * iqr_age) #1.5 = valor de 50% - valor padrão para este calculo
limite_inferior_age = q1_age - (1.5 * iqr_age) 

df_financeira_age_outliers_superiores = df_fare_age[df_fare_age['Age'] > limite_superior_age]
df_financeira_age_outliers_inferiores = df_fare_age[df_fare_age['Age'] < limite_inferior_age]





print("\n-- OBTENDO INFORMAÇÕES SOBRE AS PASSAGENS --")
print(f"A média das passagens é {media_fare:.2f}")
print(f"A mediana das passagens é {mediana_fare:.2f}")
print(f"A distância entre a média e a mediana é {distancia_fare:.2f} %")
print(f"O menor valor das passagens é {minimo_fare:.2f}")
print(f"O maior valor das passagens é {maximo_fare:.2f}")
print(f"A amplitude dos valores das passagens é {amplitude_fare:.2f}")
print(f"O valor do q1 - 25% da passagem é R$ {q1_fare}")
print(f"O valor do q2 - 50% da passagem é R$ {q1_fare}")
print(f"O valor do q1 - 75% da passagem é R$ {q1_fare}")
print(f"O valor do iqr = q3 - q1 da passagem é R$ {iqr_fare}")
print(f"O limite inferior da passagem é R$ {limite_inferior_fare}")
print(f"O limite superior da passagem é R$ {limite_superior_fare}")
print('\n -Verificando a existência de outliers inferiores -')
if len(df_financeira_fare_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_fare_outliers_inferiores) 
print('\n -Verificando a existência de outliers superiores -')
if len(df_financeira_fare_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_fare_outliers_superiores) 

print("\n-- OBTENDO INFORMAÇÕES SOBRE AS IDADES --")
print(f"A média das idades é {media_age:.1f}")
print(f"A mediana das idades é {mediana_age:.1f}")
print(f"A distância entre a média e a mediana é {distancia_age:.1f} %")
print(f"O menor valor das idades é {minimo_age}")
print(f"O maior valor das idades é {maximo_age}")
print(f"A amplitude dos valores das idades é {amplitude_age}")
print(f"O valor do q1 - 25% do age é R$ {q1_age}")
print(f"O valor do q2 - 50% do age é R$ {q2_age}")
print(f"O valor do q1 - 75% do age é R$ {q3_age}")
print(f"O valor do iqr = q3 - q1 do age é R$ {iqr_age}")
print(f"O limite inferior do age é R$ {limite_inferior_age}")
print(f"O limite superior do age é R$ {limite_superior_age}")
print('\n -Verificando a existência de outliers inferiores -')
if len(df_financeira_age_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_age_outliers_inferiores) 
print('\n -Verificando a existência de outliers superiores -')
if len(df_financeira_age_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_age_outliers_superiores)       