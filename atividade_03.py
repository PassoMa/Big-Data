try:
   nome = input("Nome do Estudante: ")
   not1 = float(input("Informe a Primeira nota: "))
   not2 = int(input("Informe a Segunda nota: "))
   not3 = int(input("Informe a Terceira nota: "))
except ValueError:
   print("Verifique os valores informados: ")
else:     
   result = (not1 + not2 + not3) / 3
   if result >= 7.5:
      print(f"Aprovado{result:.2f}")
   elif result >= 4.0 and result  <= 7.5:
      print("Recuperacao,",result)
   else:
      print("Reprovado",result)
