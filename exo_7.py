print("Entrez l nom du fichier:")
fichier=str(input())
fichier=fichier.split(".")
print("L'extension du fichier est:" +repr (fichier[-1]))