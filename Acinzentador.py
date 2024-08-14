import cv2

arquivo = open("test.txt")

linhas = arquivo.readlines()
#print(linhas[0])
linhas = list(map(lambda l: l.strip(), linhas)) 

for linha in linhas:
    print(linha)
    imagem = cv2.imread(linha)
    imagem_gs = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(linha, imagem_gs)
    cv2.imshow("Original", imagem)



#imagem = cv2.imread("BAG_0001_jpg.rf.12cb76933da0cf1ea2e048d97e869ef4.jpg")
#


