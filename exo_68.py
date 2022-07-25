print("Entrez un nombre:")
nombre=int(input())

def somme(entier):
    som=0
    while entier>0:
        som+=entier%10
        entier//=10
    return som
print("La somme des chiffres de ce nombre est:",somme(nombre))
