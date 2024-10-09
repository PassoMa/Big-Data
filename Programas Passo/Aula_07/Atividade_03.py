sexo = ["M" , "F"]
olhos = ["azul" ,  "verde", "castanho"]
cabelo = ["louros", "castanhos", "pretos"]
idade = []
resp = "S"
qnt_sexo_idade = 0
qnt_olhos_cabelos = 0
while  resp == "S" or resp == "s":
    sexo.append(input("Informe seu sexo (M/F): "))
    olhos.append(input("Informe a cor dos olhos A - Azul, : "))
    cabelo.append(input("Informe a cor dos cabelos: "))
    idade.append(int(input("Informe a sua idade: ")))
    resp = input("Deseja Continuar (S/N)? ")
for 