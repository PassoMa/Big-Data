import pandas as pd
import numpy as np

# Importando a Base de Dados
endereco_dados = 'BASES\Funcionarios.csv'

# Criando o DataFrame 
df_funcionarios = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')

# Exibindo a base de dados funcionarios
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_funcionarios.head())

# Criando o array do salário e das idades dos funcionários
array_salario = np.array(df_funcionarios["Salário"])
array_idade = np.array(df_funcionarios["Idade"])

# Obtendo a média do salário e das idades dos funcionários
media_salario = np.mean(array_salario)
media_idade = np.mean(array_idade)

# Obtendo a mediana do salário e das idades dos funcionários
mediana_salario = np.median(array_salario)
mediana_idade = np.median(array_idade)

# Obtendo a distância entre a média e a mediana do salário e das idades dos funcionários
distancia_salario = abs((media_salario - mediana_salario) / mediana_salario) * 100
distancia_idade = abs((media_idade - mediana_idade) / mediana_idade) * 100

# Obtendo o máximo e o mínimo do valor do salário e das idades dos funcionários
maximo_salario = np.max(array_salario)
minimo_salario = np.min(array_salario)
maximo_idade = np.max(array_idade)
minimo_idade = np.min(array_idade)

# Obtendo a amplitude do valor do salário e das idades dos funcionários
amplitude_salario = maximo_salario - minimo_salario
amplitude_idade = maximo_idade - minimo_idade

q1_salario = np.quantile(array_salario, 0.25, method='weibull') #quantile = calcula os quartis
q2_salario = np.quantile(array_salario, 0.50, method='weibull')
q3_salario = np.quantile(array_salario, 0.75, method='weibull')
iqr_salario = q3_salario - q1_salario

limite_superior_salario = q3_salario + (1.5 * iqr_salario) #1.5 = valor de 50% - valor padrão para este calculo
limite_inferior_salario = q1_salario - (1.5 * iqr_salario) 

df_financeira_salario_outliers_superiores = df_funcionarios[df_funcionarios['Salario'] > limite_superior_salario]
df_financeira_salario_outliers_inferiores = df_funcionarios[df_funcionarios['Salario'] < limite_inferior_salario]





# Exibindo os dados solicitados sobre os salários dos funcionários
print("\n-- OBTENDO INFORMAÇÕES SOBRE OS SALÁRIOS DOS FUNCIONÁRIOS --")
print(f"A média dos salários é R$ {media_salario:.2f}")
print(f"A mediana dos salários é R$ {mediana_salario:.2f}")
print(f"A distância entre a média e a mediana é {distancia_salario:.2f} %")
print(f"O menor valor dos salários é R$ {minimo_salario:.2f}")
print(f"O maior valor dos salários é R$ {maximo_salario:.2f}")
print(f"A amplitude dos valores dos salários é {amplitude_salario:.2f}")

print(f"O valor do q1 - 25% da renda é R$ {q1_salario}")
print(f"O valor do q2 - 50% da renda é R$ {q1_salario}")
print(f"O valor do q1 - 75% da renda é R$ {q1_salario}")
print(f"O valor do iqr = q3 - q1 da renda é R$ {iqr_salario}")
print(f"O limite inferior da renda é R$ {limite_inferior_salario}")
print(f"O limite superior da renda é R$ {limite_superior_salario}")
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

# Exibindo os dados solicitados sobre as idades dos funcionários
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS IDADES DOS FUNCIONÁRIOS --")
print(f"A média das idades é {media_idade:.1f}")
print(f"A mediana das idades é {mediana_idade:.1f}")
print(f"A distância entre a média e a mediana é {distancia_idade:.1f} %")
print(f"O menor valor das idades é {minimo_idade}")
print(f"O maior valor das idades é {maximo_idade}")
print(f"A amplitude dos valores das idades é {amplitude_idade}")