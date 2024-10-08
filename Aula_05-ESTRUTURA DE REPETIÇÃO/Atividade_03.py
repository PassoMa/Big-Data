#Estrutura de repetição
soma_f = 0
soma_m = 0
cont_f = 0
cont_m = 0
maior = 0
for i in range(5):
    nome = input("Informe um nome do usuário: ")
    idade = int(input("Informe a idade do usuário: "))
    sexo = input("Informe seu sexo: ")
    if idade > maior:
        maior = idade
    if sexo == "f" or sexo == "F":
        soma_f = soma_f + idade
        cont_f += 1
    if sexo == "m" or sexo == "M":
        soma_m = soma_m + idade
        cont_m += 1
media_f = soma_f / cont_f
media_m = soma_m / cont_m
print(f"A Soma das idades dos homens é {soma_m} e a media é {media_m:.0f}")
print(f"A Soma das idades das mulheres é {soma_f} e a media é {media_f:.0f}")
print(f"A maior idade é {maior}")