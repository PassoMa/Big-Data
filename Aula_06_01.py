import pandas as pd

endereco_dados = 'BASES\Funcionarios.csv'
df_funcionarios = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')
print('---- DADOS FUNCIONÁRIOS ----')
print(df_funcionarios.head())


media_salarial = df_funcionarios['Salário'].mean(axis=0)
media_idade = df_funcionarios['Idade'].mean(axis=0)
maior_tempo = df_funcionarios['Tempo'].max(axis=0)
menor_tempo = df_funcionarios['Tempo'].min(axis=0)
diferenca_tempo = maior_tempo - menor_tempo
maior_nome = df_funcionarios[df_funcionarios['Tempo'] == maior_tempo]['Nome']
menor_nome = df_funcionarios[df_funcionarios['Tempo'] == menor_tempo]['Nome']
media_tempo = df_funcionarios['Tempo'].mean(axis=0)
qnt_funcionario = df_funcionarios['Nome'].count # Cout = Contar
maior_idade = df_funcionarios['Idade'].max(axis=0)
menor_idade = df_funcionarios['Idade'].min(axis=0)
mais_velho = df_funcionarios[df_funcionarios['Idade'] == maior_idade]['Nome']
mais_novo = df_funcionarios[df_funcionarios['Idade'] == menor_idade]['Nome']
diferenca_idade = maior_idade - menor_idade
maior_salario = df_funcionarios['Salário'].max(axis=0)
func_maior_salario = df_funcionarios[df_funcionarios['Salário'] == maior_salario]['Nome']
qtd_func = df_funcionarios['Nome'].count()

#.to_string(index=False) = usa-se toda vez que não queira exibir uma informação do DataFrame 

print("\n---- Informações Solicitadas ----")
print(f"A média Salárial é de R$ {media_salarial:.0f}")
print(f"A média de Idade é {media_idade:.0f} anos.")
print(f"O maior tempo de casa é {maior_tempo} anos.")
print(f"O menor tempo de casa é {menor_tempo} anos.")
print(f"A diferença entre o tempo de casa é igual a {maior_tempo - menor_tempo} anos.")
print(f"A média do Tempo de casa é igual {media_tempo:.0f} anos")
print(f"O nome do Funcionário mais velho é: {maior_nome.to_string(index=False)}.")
print(f"O nome do Funcionário mais novo é: {menor_nome.to_string(index=False)}")
print(f"A diferença de idade entre estes funcionarios é de {maior_idade - menor_idade} anos.")
print(f"O funcionário com o maior salario é:{func_maior_salario.to_string(index=False)}")
print(f"O nome do Funcionário com maior tempo de casa é: {mais_velho.to_string(index=False)}.")
print(f"A Quantidade de funcionários na empresa são: {qtd_func}")




