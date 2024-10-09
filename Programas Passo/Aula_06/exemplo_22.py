#comando 'sum' = soma
#comando 'max' = maior/maximo
#comando 'min" = menor
# Não tem comando para calcular a MÉDIA -- SOMA 'SUM' TODAS AS IDADES E DIVIDE POR 'LEN'
# sort = coloca em ordem crescente
#mediana divide literalmente o meio
#media não é um bom parametro para a analise e sim a mediana
idades = [20,10,15,30,50,12,60,22,55,35]
print(f"A soma das idades é: {sum(idades)} anos.")
print(f"A maior idades é: {max(idades)} anos.")
print(f"A menor idades é: {min(idades)} anos.")
print(f"A média das idades é: {sum(idades)/len(idades)} anos.") #media
idades.sort()
print(idades)