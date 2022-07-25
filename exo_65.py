print(" Entrez un nombre de secondes:")
sec1=int(input())
j=sec1//(24*3600)
print(" Le nombre de jours donne:",j)
sec=sec1%(24*3600)
h=sec//3600
print("Le nombre d' heure donne:",h)
sec=sec%3600
print("Le nombre de minutes donne",sec//60)
sec=sec%60
print("Le nombre de secondes est:",sec)