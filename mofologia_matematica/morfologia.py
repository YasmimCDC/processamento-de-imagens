from typing import *
Matriz = List[List[int]]


def dilatacao(imagem: Matriz, alturaMascara: int, larguraMascara: int) -> Matriz:
    print("Aplicando a dilatação na imagem...")
    alturaMascara = alturaMascara
    larguraMascara = larguraMascara
    deltaAltura = round((alturaMascara-1)/2)
    deltaLargura = round((larguraMascara-1)/2)
    nova_imagem = []

    for i in range(0, len(imagem)):
        linha = []
        for j in range(0, len(imagem[0])):
            if (i <= deltaAltura or i >= len(imagem)-deltaAltura) or (j <= deltaLargura or j >= len(imagem[0])-deltaLargura):
                linha.append(imagem[i][j])

            else:
                aux = []
                for n in range(-deltaAltura, deltaAltura+1):
                    for m in range(-deltaLargura, deltaLargura+1):
                        aux.append(imagem[i + n][j + m])

                if 1 in aux:
                    linha.append(1)
                else:
                    linha.append(0)

        nova_imagem.append(linha)

    return nova_imagem


def erosao(imagem: Matriz, alturaMascara: int, larguraMascara: int) -> Matriz:
    print("Aplicando a erosão na imagem...")
    alturaMascara = alturaMascara
    larguraMascara = larguraMascara
    deltaAltura = round((alturaMascara-1)/2)
    deltaLargura = round((larguraMascara-1)/2)
    nova_imagem = []

    for i in range(0, len(imagem)):
        linha = []
        for j in range(0, len(imagem[0])):
            if (i <= deltaAltura or i >= len(imagem)-deltaAltura) or (j <= deltaLargura or j >= len(imagem[0])-deltaLargura):
                linha.append(imagem[i][j])

            else:
                aux = []
                for n in range(-deltaAltura, deltaAltura+1):
                    for m in range(-deltaLargura, deltaLargura+1):
                        aux.append(imagem[i + n][j + m])

                aplicar = True
                for x in aux:
                    if x != 1:
                        aplicar = False

                if aplicar:
                    linha.append(1)
                else:
                    linha.append(0)

        nova_imagem.append(linha)

    return nova_imagem


def contagem(imagem: Matriz) -> [int, int]:
    print("Contando...")
    x = y = 0
    palavras = []

    # Procurando a primeira palavra
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            if imagem[i][j] == 1:
                y = i
                x = j
                break
        if x != 0 or y != 0:
            break

    # Achando o pixel inferior esquerdo da palavra
    for i in range(y, len(imagem)):
        if imagem[i+1][x] == 0:
            y = i
            break
    linhas = 0
    while y < len(imagem):
        contagem_palavras(imagem, palavras,  x, y)
        linhas += 1
        y += 1

        while imagem[y][x] == 0:
            y += 1
            if y >= len(imagem):
                break

        # Achando o pixel inferior esquerdo da palavra
        for i in range(y, len(imagem)):
            if imagem[i+1][x] == 0:
                y = i
                break

    return len(palavras), linhas


def contagem_palavras(imagem: Matriz, palavras,  x: int, y: int):
    # Obtendo o retangulo ao redor das palavras da linha
    while True:
        palavras.append(definir_bordas(imagem, x, y))
        x = palavras[-1][2][1]

        while imagem[y-3][x] == 0:
            x += 1
            if x >= len(imagem[0]):
                break

        if x >= len(imagem[0]):
            break


def definir_bordas(imagem: Matriz, x: int, y: int):
    i = x
    j = y

    while imagem[y-3][i] == 1 and i < len(imagem):
        i += 1

    while imagem[j][x] == 1 and j > 0:
        j -= 1

    # x, i => largura, y, j => altura
    return [(y, x), (j, x), (y, i)]
