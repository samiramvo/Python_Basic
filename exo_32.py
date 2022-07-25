print("Calculer le ppcm:")
print("Entrer le premier nombre:")
a=int(input())
print("Entrez le second nombre:")
b=int(input())
def ppcm(x,y):
    if x>y:
        z=x
    else:
        z=y
    while(1):
        if((z%x==0)and (z%y==0)):
            ppcm=z
            break
        z+=1
    return ppcm

print(ppcm(a,b))