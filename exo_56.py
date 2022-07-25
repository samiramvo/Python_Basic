import os
rows,columns=os.popen('stty size','r').read().split()
print("La hauteur de la console est:",rows)
print("La largeur de la console est:",columns)