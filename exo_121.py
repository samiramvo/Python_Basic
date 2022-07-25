def local_func():
    var=12344
    if 'var' in locals():
        print("La variable var existe")
    else:
      print(" Elle n’existe pas")
      
      
local_func()