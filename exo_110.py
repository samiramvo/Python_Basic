
def anonyme(liste):
    new_liste=[]
    for i in liste:
        if i%15==0:
            new_liste.append(i)
    return new_liste

liste1=[15,30,56,60,45,32,76,2,6]
print(anonyme(liste1))