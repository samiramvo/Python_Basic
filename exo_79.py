
import sys

print("Trouvez la taille d'un objet en octet:")
print("Entrez l'objet:")
obj=int(input())
a=sys.getsizeof(obj)
print(a)