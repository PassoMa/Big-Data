idade = int(input("Informe sua idade: "))
ano_emp = int(input("Informe  ano que entrou na Empresa: "))
result = 2024 - ano_emp
if idade >= 65:
    print("Apto a Aposentadoria",idade)
elif result >= 30:
    print("Apto a Aposentadoria",result)
elif idade >= 60  and result >= 25:
    print("Apto a Aposentadoria",idade,result)
else:
    print("Inapto Aposentadoria")
