#try- pode ter quantos quiser. Colocar um Try para cada entrada. Dentro de cada Try colocar um except
try:
    n1 = int(input("Informe o primeiro valor."))
    n2 = int(input("Informe o segundo valor."))
except ValueError:
    print("Verifique a entrada de dados.")
else:    
    try:
        div = n1/n2
    except ZeroDivisionError:
        print("Não é possivel dividir por zero")
    else:       
        print(div)