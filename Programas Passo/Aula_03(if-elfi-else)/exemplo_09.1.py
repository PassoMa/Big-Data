#Para cada if só pode 1 else, e ele só pode ser o ultimo comando 
idade = int(input("Informe a idade: "))
if idade < 18:
    print("Você é Menor de Idade")
elif idade == 18:
    print("Quase lá!") 
elif idade > 65:
    print("Acesso Liberado - Aprecie com Moderação!")       
else:
    print("Acesso liberado!")


    