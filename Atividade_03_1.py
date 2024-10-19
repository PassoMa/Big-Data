import pandas as pd
# Criando uma função para formatar número
def formatar(valor):  # def - comando para criara função
    return "{:.2f}%".format(valor)


pop_vac = pd.Series([30000000, 25000000, 10000000, 5000000])
pop_tot =pd.Series([213317639, 214477744, 215574303, 216687971])
taxa_vacinacao = ((pop_vac / pop_tot) * 100).apply(formatar)
print("\n-------Dados da vacinação------")# \n - pula linha
print(f"Total de pessoas vacinadas: {pop_vac.sum()}")
print(f"Média de pessoas vacinadas: {pop_vac.mean():.2f}")
print("\n------Dados População------")
print(f"Total da população: {pop_tot.sum()}")
print(f"Média da população: {pop_tot.mean():.2f}")
print("\n------Taxa de Vacinação------")
print("\nTaxa de vacinação anual:")
print(f"A taxa de vacinação atual é de: {taxa_vacinacao}")