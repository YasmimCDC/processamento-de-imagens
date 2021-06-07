from filtros import *


def validar_mascara(k: int) -> bool:
    if k % 2 == 0:
        return False

    return True


def criar_mascara_media(k: int) -> Matriz:
    linha = [1 for x in range(k)]
    mascara = [linha for x in range(k)]

    return mascara


def copiar_bordas(imagem: Matriz, deltaAltura: int, deltaLargura: int):
    for n in range(len(imagem)):
        for k in range(deltaAltura):
            imagem[n].insert(0, imagem[n][0])
            imagem[n].insert(len(imagem[n]) - 1, imagem[n][len(imagem[n]) - 1])

    # Duplicando pixels de cima e de baixo
    for k in range(deltaLargura):
        imagem.insert(0, imagem[0])
        imagem.insert(len(imagem[0]) - 1, imagem[len(imagem[0]) - 1])


def mediana(imagem: Matriz, altura: int, largura: int) -> Matriz:
    alturaMascara = 3
    deltaAltura = deltaLargura = round((alturaMascara-1)/2)
    med = ((alturaMascara * alturaMascara)-1)//2
    nova_imagem = []

    copiar_bordas(imagem, deltaAltura, deltaAltura)

    for i in range(deltaAltura, len(imagem)-deltaAltura):
        linha = []
        for j in range(deltaLargura, len(imagem[0])-deltaLargura):
            aux = []
            for n in range(-deltaAltura, deltaAltura+1):
                for m in range(-deltaLargura, deltaLargura+1):
                    aux.append(imagem[i + n][j + m])
            aux.sort()
            linha.append(aux[med])
        nova_imagem.append(linha)

    return nova_imagem


def convolucao(imagem: Matriz, mascara: Matriz) -> List:
    alturaMascara = len(mascara)
    larguraMascara = len(mascara[0])

    deltaAltura = round((alturaMascara - 1) / 2)
    deltaLargura = round((larguraMascara - 1) / 2)

    # Duplicando pixels das bordas
    copiar_bordas(imagem, deltaAltura, deltaLargura)

    saida = []
    pesos = somar_pesos(mascara)
    for i in range(deltaAltura, len(imagem)-deltaAltura):
        linha = []
        for j in range(deltaLargura, len(imagem[0])-deltaLargura):
            soma = 0
            for m in range(-deltaAltura, deltaAltura+1):
                for n in range(-deltaLargura, deltaLargura+1):
                    soma += imagem[i+m][j+n]*mascara[m][n]
            pixel = soma/(alturaMascara * larguraMascara * pesos)
            linha.append(round(pixel))

        saida.append(linha)

    return saida


def somar_pesos(mascara: Matriz) -> float:
    soma = 0
    for i in range(len(mascara)):
        for j in range(len(mascara[0])):
            soma += mascara[i][j]

    return soma/9


def box_filter(imagem: Matriz, k: int):
    mascara = criar_mascara_media(k)
    return convolucao(imagem, mascara)
