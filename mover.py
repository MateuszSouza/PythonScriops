import shutil
from os import path

arquivoComNomes = open('./test/test.txt')
nomesArquivos = arquivoComNomes.readlines()
arquivoComNomes.close()


caminho_antigo_base = './test/images'
caminho_novo_base   = './test/labels'

for nome in nomesArquivos:
    oldPath = caminho_antigo_base + '/' + nome.replace('\n','')
    newPath = caminho_novo_base + '/' + nome.replace('\n','')
    print("OldPath: " + oldPath )
    shutil.move(oldPath,newPath)
