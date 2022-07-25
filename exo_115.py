from functools import reduce

print(" Voici une liste:")
liste=[3,3,5,-4,5,-1]
mult=reduce(lambda x,y: x* y,liste)
print("La multiplication des elements de la liste est:",mult)