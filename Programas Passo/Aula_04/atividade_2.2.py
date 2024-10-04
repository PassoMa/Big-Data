import datetime
data_atual = datetime.date.today()
try:
    name = input("Informe seu nome: ")
    nasc = int(input("Informe o ano de nascimento: "))
    ano_emp = int(input("Informe  ano que entrou na Empresa: "))
except ValueError:
    print("Verifique os valores informados")  
else: 
    idade = data_atual.year - nasc
    tempo = data_atual.year - ano_emp     
    if idade >= 65:
       print(f"Sr {name}, Apto a Aposentadoria {idade} anos")
    elif tempo >= 30:
       print(f"Sr {name}, Apto a Aposentadoria {tempo} anos trabalhados.")
    elif idade >= 60  and tempo >= 25:
       print(f"Sr {name}, Apto a Aposentadoria {idade,tempo} anos.")
    else:
       print(f"Sr {name}, Inapto Aposentadoria")