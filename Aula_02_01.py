#Código usando listas
media = [80,90,10,50,30,70,100,20,90,50]
ap = []
rep = []
for i in range(len(media)):
    if media [i] >= 70:
        ap.append(media[i])
    else:
        rep.append(media[i])
print(ap)
print(rep)        