import os
for filename in os.listdir():
    info=os.stat(filename)
    print(info.st_mtime)