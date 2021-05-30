import os


dirname = os.path.dirname(__file__)
codefilePath = os.path.join(dirname, 'output/' , 'mytext.txt')

with open(codefilePath,"w") as file:
    file.write("I know how to use docker.")