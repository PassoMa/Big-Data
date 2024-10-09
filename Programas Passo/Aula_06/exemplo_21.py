#todo vetor fica dentro de []
#range = quantas vezes irá repetir
# i = faz associação ao indice
#Quando se coloca string("") e o vetor[], o python entende que cada virgula representa um elemento
nomes_01 = "Marcella,Kevinlyn,Karolayne,Ryan.Miguel"
nomes_02 = ["Marcella", "Kevinlyn" , "Karolayne", "Ryan", "Miguel"]
print(nomes_01)
print(nomes_02)
print(nomes_02[2])
print(len(nomes_02)) #Len - serve para mostrar quantos elementos tem dentro do vetor
n = 1
for i in range(len(nomes_02)):
    print(nomes_02[i])
for i in range(len(nomes_02)):
    print(f"{n} - {nomes_02[i]}")
    n+=1