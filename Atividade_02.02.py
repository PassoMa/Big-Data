# prompt: uma serie "temp_max" outra serie "temp_min". onde se tem sete temperaturas em cada. logo depois saber a media da "temp_max", a media da "temp_min". e a variação entre as duas series

import pandas as pd

temp_max = pd.Series([37, 38, 30, 29, 42, 30, 33])
temp_min = pd.Series([15, 25, 17, 6, 8, 22, 20])

media_temp_max = temp_max.mean()
media_temp_min = temp_min.mean()
variacao = temp_max - temp_min

print("Média da Temperatura Máxima:", media_temp_max)
print("Média da Temperatura Mínima:", media_temp_min)
print("Variação entre as temperaturas máxima e mínima:")
print(variacao)


print("-----------------------------------------------------")


import pandas as pd
temp_max = pd.Series([30,31,38,32,25,22,30])
temp_min = pd.Series([25,24,26,19,18,16,22])
media_max = temp_max.mean()
media_min = temp_min.mean()
print("Amplitude Térmica em Grau ºC")
print(temp_max - temp_min)
print("----------------------------")
print(f"A média da temperatura máxima foi {media_max:.1f}ºC")
print(f"A média da temperatura mínima foi {media_min:.1f}ºC")