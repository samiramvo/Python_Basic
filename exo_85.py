
import os

def fch_rep(fid):
    if os.path.isdir(fid):
        print("Il s' agit d'un répertoire")
    elif os.path.isfile(fid):
        print("Il s’agit d’un fichier")
     
    else:
        print(" Il ne s’agit ni d’un répertoire ni d’un fichier")

print(fch_rep("exo_80.py"))
     