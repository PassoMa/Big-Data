import pandas as pd
dados_vendedores = [
    ['Ana','F',28,120],
    ['Bruno','M',34,150],
    ['Carlos','M',45,110],
    ['Diana','F',30,95],
    ['Eduardo','M',40,130],
    ['Fernada','F',29,140],
    ['Gustavo','M',38,105],
    ['Helena','F',31,125],
    ['Igor','M',27,100],
    ['Juliana','F',33,135],
]
colunas = ['Nome','Sexo','Idade','Qnt_Vendas']

df_dados_vendedores = pd.DataFrame(dados_vendedores,columns=colunas)

print(df_dados_vendedores)

soma_vendas = df_dados_vendedores['Qnt_Vendas'].sum(axis=0)
media_vendas = df_dados_vendedores['Qnt_Vendas'].mean(axis=0)
maior_venda = df_dados_vendedores['Qnt_Vendas'].max(axis=0)
menor_venda = df_dados_vendedores['Qnt_Vendas'].min(axis=0)

media_idade = df_dados_vendedores['Idade'].mean(axis=0)
maior_idade = df_dados_vendedores['Idade'].max(axis=0)
menor_idade = df_dados_vendedores['Idade'].min(axis=0)

qnt_vendas_M = df_dados_vendedores[df_dados_vendedores['Sexo'] == 'M']['Qnt_Vendas'].sum(axis=0) #Acumulado de vendas por sexo
qnt_vendas_F = df_dados_vendedores[df_dados_vendedores['Sexo'] == 'F']['Qnt_Vendas'].sum(axis=0)

maior_venda_nome = df_dados_vendedores[df_dados_vendedores['Qnt_Vendas'] == maior_venda]['Nome']
menor_venda_nome = df_dados_vendedores[df_dados_vendedores['Qnt_Vendas'] == menor_venda]['Nome']




print("\n-----Informações sobre as Vendas-----")
print(f"O Total das  Vendar é de R${soma_vendas}")
print(f"A média é igual a R${media_vendas}")
print(f"O melhor vendedor no período é: {maior_venda_nome.values[0]}")
print(f"O pior vendedor no período é: {menor_venda_nome.values[0]}")

print("\n-----Informações sobre as Idades-----")
print(f"A média é igual a {media_idade}")
print(f"A maior idade é igual a:{maior_idade}")
print(f"A menor idade é igual a: {menor_idade}")

print("\n-----Informações sobre as Vendas por Sexo-----")
print(f"A maior parte das vendas foi feita por vendedores do sexo:{qnt_vendas_M}")
print(f"A menor parte das vendas foi feita por vendedores do sexo:{qnt_vendas_F}")