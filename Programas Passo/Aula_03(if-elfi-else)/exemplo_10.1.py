# Conectivo - or (ou) = uma coisa ou outra 
h = float(input("Informe a altura: "))
s = input("Informe M - para Masculino e F - para Feminino: ")
if s == "M" or s == "m":
    m = (72.7 * h) - 58
    print(f"O seu peso ideal é {m:.2f}:")
elif s == "F" or s == "f":
    f = (62.1 * h) - 44.7
    print(f"O peso ideal é {f:.2f}:")
else:
    print("Verifique o Sexo Informado")