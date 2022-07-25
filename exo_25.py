print("Voici une liste d'éléments:")
liste=[1,3,"Samira","Paul","Jean",5,6,8,"Sasha"]
print(liste)

def liste1(valeur):
  for i in liste:
    if i==valeur:
      return True
      
  return False
      
print(liste1(3))   
