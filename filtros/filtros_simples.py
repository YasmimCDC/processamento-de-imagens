from filtros import *


def limiarizar(imagem: Matriz, limiar: int, altura: int, largura: int, qtd_tons: int):
    for i in range(altura):
        for j in range(largura):
            pixel = imagem[i][j]
            if pixel > limiar:
                imagem[i][j] = qtd_tons
            else:
                imagem[i][j] = 0


def negativar(imagem: Matriz, altura: int, largura: int, qtd_tons: int):
    for i in range(altura):
        for j in range(largura):
            pixel = imagem[i][j]
            imagem[i][j] = qtd_tons - pixel
