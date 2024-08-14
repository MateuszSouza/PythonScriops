import os

pasta = "./"
nomes = os.listdir(pasta)

nomes2 = []
for n in nomes:
    print(n)
    newmane1 = n.replace('_jpg.rf.','_')
    print("<<"+newmane1)
    os.rename(n, newmane1)

