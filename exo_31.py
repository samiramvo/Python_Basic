print("Calculer le pgcd:")
print("Entrer le premier nombre:")
a=int(input())
print("Entrez le second nombre:")
b=int(input())
def pgcd(x,y):
    pgcd=1
    if x%y==0:
        return y
    for k in range(int(y/2),0,-1):
        if x%k==0 and y%k==0:
            pgcd=k
            break
    return pgcd

print(pgcd(a,b))