# append = comando para preencher os vetores
nomes = []
medias = []
resp = "S"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do estudante: "))
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja Continuar(S/N)? ")
print("Nome dos estudante: ",nomes)
print("Média dos estudantes: ", medias)    
print(f"A maior média é: {max(medias)}.")
print(f"A menor média é: {min(medias)}.")
print(f"A média da turma é: {(sum(medias)/len(medias)):.2f}.")
print(f"A soma das médias é: {sum(medias)}.")
medias.sort(reverse = True)
print("Média na ordem Decrescente:", medias)
medias.sort()
print("Média na ordem Crescente:",medias)
