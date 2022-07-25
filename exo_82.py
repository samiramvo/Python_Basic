def somme(conteneur):
    som=0
    
    for i in conteneur:
        som+=i
    return som
          
     
print(somme([1,2,3]))   
print(somme((1,2,5)))
print(somme({1,0,8}))
def somme2(conteneur):
    som=0
    
    for value in conteneur.values():
        som+=value
    return som

dictionnaire={
    "banane":2311,
    "Ananas":234
    
}
print(somme2(dictionnaire))