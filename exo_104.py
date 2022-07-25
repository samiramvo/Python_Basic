import os
print("Identifiant du groupe effectif:",os.getgid())
print("L'identifiant d'utilisateur effectif",os.getuid())
print("L'identifiant du groupe reel est :",os.getgid())
print("Liste de groupe supplémentaire d'identifiants:",os.getgroups())