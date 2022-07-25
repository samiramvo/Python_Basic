import os
from glob import glob
liste=glob(os.getcwd()+"/*/",recursive=True)
print (liste.sort(key=os.path.getmtime))