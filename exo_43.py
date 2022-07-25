import os
import platform
import sys
import sysconfig
print("Le système d'exploitation utilisée est:",platform.system())
print("Le nom de la plateforme utilisée est:",sys.platform)
print("Le nom de l'OS est:",os.name)
print("La version de l'OS est:",platform.release())