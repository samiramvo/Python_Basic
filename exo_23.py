print("Entrez une chaine de caractere:")
chaine=str(input())
print("Entrez le nombre de copies de la chaine:")
copies=int(input())

def chn(chaine):
   chaine=chaine*copies
   if len(chaine)<2:
    print(chaine[0:2])

print("Les n copies de la chaine entière est:",chn(chaine))