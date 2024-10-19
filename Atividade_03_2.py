import pandas as pd
def formatar(valor):
     return "{:.2f}%".format(valor)

roubo_aut = pd.Series([100, 90, 80, 120, 110, 90, 70])
furto_aut = pd.Series([80, 60, 70, 60, 100, 50, 30])
recuperacao_aut = pd.Series([70, 50, 90, 80, 100, 70, 50])
total_rou_fur = roubo_aut + furto_aut
taxa_rec_diaria = ((recuperacao_aut / total_rou_fur)* 100).apply(formatar)
print("\n------Total de Roubos e Furtos------")
print(f"{total_rou_fur.sum()}")
print("\n------Roubos e Furtos Diários-----")
print(f"{roubo_aut + furto_aut}")
print("\n------Taxa de Recuperação diária------")
print(f"{taxa_rec_diaria}")
