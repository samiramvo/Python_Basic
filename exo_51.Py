import cProfile
def sum():
    print(1+2)
print(cProfile.run('sum()'))
    