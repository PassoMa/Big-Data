proct = input("Produto: ")
qnt = int(input("Quantidade: "))
prec = float(input("Valor Unitário:"))
total = qnt * prec
print(f"Total Sem desconto R$ {total:.2f}")
if qnt <= 5:
   desc = total * 0.98
elif qnt > 5 and qnt <= 10:
   desc = total * 0.97
else:
   desc = total * 0.95
print(f"Total Com desconto R$ {desc:.2f}")