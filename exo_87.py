import os
def taille_fichier(fichier):
    return os.path.getsize(fichier)

taille_fichier1=taille_fichier("exo_67.py")
print("La taille du fichier1 est:",taille_fichier1)