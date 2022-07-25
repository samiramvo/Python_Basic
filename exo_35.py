print("Entrez l'entier1:")
a=int(input())
print("Entrez l'entier2:")
b=int(input())
def cond():
    if (a==b) or (a+b)==5 or abs(a-b)==5:
        return True
    else:
        return False
print(cond())