#Média calcula separada pois não sabe ao certo quantas serão acumulados
soma = 0
media = 0
for i in range(5):
    nome = input("Informe um nome do usuário: ")
    idade = int(input("Informe a idade do usuário: "))
    soma = soma + idade
media = soma / (i + 1)
print(f"A Soma das idades é igual a: {soma}")
print(f"A Média das idades é igual a: {media:.0f}")