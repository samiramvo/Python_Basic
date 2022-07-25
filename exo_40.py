from cmath import sqrt

print("Entrez les coordonnées du point A:")
print("xA:")
xA=int(input())
print("yA:")
yA=int(input())
print("Entrez les coordonnées du point B:")
print("xB:")
xB=int(input())
print("yB:")
yB=int(input())
print("La distance entre A et B est:",sqrt(((xB-xA)**2)+((yB-yA)**2)))