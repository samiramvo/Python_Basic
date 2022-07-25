def imprimer(x,y):
    return "{}+{}={}".format(x,y,(x+y))

print("Entrez x:")
x=int(input())
print("Entrez y:")
y=int(input())
print(str(imprimer(x,y)))