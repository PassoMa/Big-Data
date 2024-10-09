temp = []
resp = "S"
while  resp == "S" or resp == "s":
    temp.append(float(input("Informe a temperatura: ")))
    resp = input("Deseja Continuar (S/N)? ")
print(f"A menor temperatura é: {min(temp)} ºC.")
print(f"A maior temperatura é: {max(temp)} ºC.")
print(f"A média das Temperaturas é: {sum(temp)/len(temp)} ºC.")