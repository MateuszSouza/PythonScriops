def TrocaCodigo(arquivoName):
    print(arquivoName)
    arquivoName = arquivoName.replace('\n','')
    arquivo = open(arquivoName, encoding="utf8")
    lines = arquivo.readlines()
    arquivo.close()
    newLines =  []

    for line in lines:
        if  line[0] == '0':
            newLine = line.replace('0 ','0 ')
            newLines.append(newLine)
        elif line[0] == '1':
            newLine = line.replace('1 ','0 ')
            newLines.append(newLine)
        elif line[0] == '2':
            newLine = line.replace('2 ','0 ')
            newLines.append(newLine)
        elif line[0] == '3':
            newLine = line.replace('3 ','1')
            newLines.append(newLine)
        elif line[0] == '4':
            newLine = line.replace('4 ','0 ')
            newLines.append(newLine)
        elif line[0] == '5':
            newLine = line.replace('5 ','0 ')
            newLines.append(newLine)
        elif line[0] == '6':
            newLine = line.replace('6 ','0 ')
            newLines.append(newLine)
        elif line[0] == '7':
            newLine = line.replace('7 ','1 ')
            newLines.append(newLine)
        else:
            newLines.append(line)
        if newLines.__len__()>1:
            print(nome)
            print(newLines)

    arquivo = open(arquivoName,'w')
    arquivo.writelines(newLines)

arquivoComNomes = open('test.txt')
nomesArquivos = arquivoComNomes.readlines()
for nome in nomesArquivos:
    TrocaCodigo(nome)


#0 0.69453125 0.53515625 0.14765625 0.140625
#0 0.32109375 0.56015625 0.04140625 0.2390625
#