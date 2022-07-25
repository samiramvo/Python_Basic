import os.path,time
print("Ce fichier a ete modifié le :",time.ctime(os.path.getmtime("exo_63.py")))
print("Ce fichier a été créé en",time.ctime(os.path.getctime("exo_63.py")))