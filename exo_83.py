   
def test(liste,n):
    for i in liste:
        if i> n:
            return True
    return False
     
print(test([1,4,7,3,9,4,2,6],10))