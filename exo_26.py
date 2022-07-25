print("Voici une liste:")
liste=[1,3,8,4]
def his(liste):
    for i in liste:
        print("*"*i)
print("L'histogramme associé à cette liste est:",his(liste))