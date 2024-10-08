maior = 0
for i in range(5):
    idade = int(input("Informe a idade do usuário: "))
    if  idade > maior:
        maior = idade 
print(f"A maior idade é:{maior}")
