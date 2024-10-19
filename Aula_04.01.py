import pandas as pd
#Criando a tabela Alunos
aluno = [
    ['João',18,100],
    ['Maria',15,80],
    ['Antônia',18,100],
    ['Erica',20,60],
    ['Pedro',16,10],
]
#Criando as Clunas da tabela Alunos
colunas = ['Nome','Idade','Média']

#Criando o DataFrame
df_alunos = pd.DataFrame(aluno,columns=colunas) #Columns = Identificar as colunas do DataFrame

#Exibindo os Dados
print(df_alunos)

#Realizando os Cálculos das Idades
soma_idade = df_alunos['Idade'].sum(axis=0)
media_idade = df_alunos['Idade'].mean(axis=0) #axis = igual ao eixo da coluna(sintaxe)
maior_idade = df_alunos['Idade'].max(axis=0)
menor_idade = df_alunos['Idade'].min(axis=0)
maior_nome = df_alunos[df_alunos['Idade'] == maior_idade]['Nome']
menor_nome = df_alunos[df_alunos['Idade'] == menor_idade]['Nome']

#Realizando os Cálculos das Médias
soma_media = df_alunos['Média'].sum(axis=0)
media_media = df_alunos['Média'].mean(axis=0) #axis = igual ao eixo da coluna(sintaxe)
maior_media = df_alunos['Média'].max(axis=0)
menor_media = df_alunos['Média'].min(axis=0)
mai_med_nome = df_alunos[df_alunos['Média'] == maior_media]['Nome']
men_med_nome = df_alunos[df_alunos['Média'] == menor_media]['Nome']

#Exibindo os Cálculos das Idades
print("\n-----Informações sobre as Idades dos Alunos-----")
print(f"A soma da idades dos Alunos é igual a: {soma_idade} anos")
print(f"A média das Idades é igual a: {media_idade}")
print(f"A maior idade é igual a:{maior_idade}")
print(f"A menor idade é igual a: {menor_idade}")
print(f"O nome do aluno mais velho é: {maior_nome.values[0]}")
print(f"O nome do aluno mais novo é: {menor_nome.values[0]}")

#Exibindo os Cálculos das Médias
print("\n-----Informações sobre a Média dos Alunos-----")
print(f"A soma da média dos Alunos é igual a: {soma_media}")
print(f"A média dos Alunos é igual a: {media_media}")
print(f"A maior média é igual a:{maior_media}")
print(f"A menor média é igual a: {menor_media}")
print(f"O nome do aluno com a maior média é: {mai_med_nome.values[0]}")
print(f"O nome do aluno com a menor média é: {men_med_nome.values[0]}")