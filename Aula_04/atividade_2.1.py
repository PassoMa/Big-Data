try:
    name = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    ano_emp = int(input("Informe  ano que entrou na Empresa: "))
    result = 2024 - ano_emp
except ValueError:
    print("Verifique os valores informados")  
else:      
    if idade >= 65:
       print(f"Sr,{name} Apto a Aposentadoria {idade} anos")
    elif result >= 30:
       print(f"Sr,{name} Apto a Aposentadoria {result} anos trabalhados.")
    elif idade >= 60  and result >= 25:
       print(f"Sr,{name} Apto a Aposentadoria {idade,result} anos.")
    else:
       print(f"Sr, {name} Inapto Aposentadoria")