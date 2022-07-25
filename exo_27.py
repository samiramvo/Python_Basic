print("Voici une liste:")
liste=[1,3,4,6,7,8]
liste=str(liste)
result=''
for i in liste:
    result+=str(i)
result=result.split(",")
print("La concaténation des éléments de cette liste est:","".join(result))