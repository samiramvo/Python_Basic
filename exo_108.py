import os.path
for file in[__file__,os.path.dirname(__file__),'/','broken_link']:
    print(file)
    print(os.path.isabs(file))
    print(os.path.isfile(file))