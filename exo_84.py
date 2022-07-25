def occurence(chaine,carac):
     som=0
     for lettr in chaine:
         if lettr==carac:
             som+=1
     return som
      
print(occurence("Samira","a"))