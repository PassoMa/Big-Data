# append = comando para preencher os vetores
# index = rastrea no vetor até encontar a posição em qual o elemento se encontra
nomes = []
medias = []
resp = "S"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do estudante: "))
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja Continuar(S/N)? ")
for i in range(len(medias)):
    print(i, "-", nomes[i], "-" , medias[i])  
maior_media = max(medias)
pos = medias.index(maior_media)
print(f"{nomes[pos]}, possui a maior média.")
print(f"A média da turma é: {(sum(medias)/len(medias)):.1f}.")
print(f"A maior média é: {max(medias)}.")
print(f"A menor média é: {min(medias)}.")
print(f"Amplitude da média da turma é {max(medias)-min(medias)}") 
medias.sort()
print("Média na ordem Crescente:" , medias)