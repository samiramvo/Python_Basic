from os import listdir
from os.path import isfile,join
fichiers=[f for f in listdir('/Documents/Python_exos/Python_Basic')if isfile(join('/Documents/Python_exos/Python_Basic',f))]
print(fichiers)