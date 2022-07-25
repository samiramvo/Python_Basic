print("Entrez un objet:")
a=input()
print("Entrez un objet:")
b=input()
def cond():
    if not (isinstance(a,int) and isinstance(b,int)):
        return "Error"

    return a+b
print(cond())