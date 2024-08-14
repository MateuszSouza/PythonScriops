def TrocaCodigo(arquivoName):
    contadorAmeaça = 0
    contadorLimpo = 0
    total = 0
    outros = 0
    print(arquivoName)
    arquivoName = arquivoName.replace('\n','')
    arquivo = open(arquivoName, encoding="utf8")
    lines = arquivo.readlines()
    arquivo.close()
    

    for line in lines:
        if  line[0] == '1':
            contadorAmeaça = contadorAmeaça + 1
        elif line[0] == '0':
            contadorLimpo = contadorLimpo + 1
        else:
            outros = outros + 1
        total = total + 1
    print("numero de ameaças: ", contadorAmeaça )
    print("Numero de imagens limpas: ", contadorLimpo)
    
    return contadorLimpo, contadorAmeaça, total, outros

arquivoComNomes = open('train.txt')
nomesArquivos = arquivoComNomes.readlines()
ca = 0
cl = 0
total = 0  
outros = 0
for nome in nomesArquivos:
    c1, c2, t, o = TrocaCodigo(nome)
    cl = cl + c1
    ca = ca + c2
    outros = outros + o
    total = total + t


print("final:")
print("numero de ameaças: ", ca )
print("Numero de imagens limpas: ", cl)
print("total ", total)
print("outros ", outros)

#0 0.69453125 0.53515625 0.14765625 0.140625
#0 0.32109375 0.56015625 0.04140625 0.2390625
#