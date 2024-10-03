nome = input("Informe o nome do Estudante: ")
n1 = float(input("Informe a primeira nota de 0 a 100: "))
n2 = float(input("Informe a segunda nota de 0 a 100: "))
media = (n1 + n2) / 2
if media >= 70:
    print(f"{nome}, você está Aprovado, pois sua média foi {media:.2f}")
elif media >= 30:
    print((f"{nome}, você está em Recuperação, pois sua média foi {media:.2f}"))
else:
    print((f"{nome}, você está Reprovado, pois sua média foi {media:.2f}"))
