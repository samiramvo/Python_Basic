print("Voici une liste d'éléments:")
liste=[1,6,7,8,9,4,4,5,6,8,4]
print(liste)
numb=0
for i in liste:
    if i==4:
        numb+=1

print("Le nombre de 4 dans la liste est:",numb)