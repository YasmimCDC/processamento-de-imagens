from typing import *
Matriz = List[List[int]]


def dilatacao(imagem: Matriz, alturaMascara: int, larguraMascara: int) -> Matriz:
    print("Aplicando a dilatação na imagem...")
    # Quantos pixels pra cima ou pra baixo estamos acessando com a mascara
    deltaAltura = (alturaMascara-1)//2
    # Quantos pixels pro a esquerda ou pra direita estamos acessando com a mascara
    deltaLargura = (larguraMascara-1)//2
    nova_imagem = []

    for i in range(0, len(imagem)):
        linha = []
        for j in range(0, len(imagem[0])):
            # Optamos por nao duplicar os pixels das bordas novamente entao estamos so repetindo eles
            # confiando na margem do texto
            if (i <= deltaAltura or i >= len(imagem)-deltaAltura) or (j <= deltaLargura or j >= len(imagem[0])-deltaLargura):
                linha.append(imagem[i][j])

            # Se qualquer um dos pixels na regiao da mascara for 1 entao o pixel central sera 1
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
    # Quantos pixels pra cima ou pra baixo estamos acessando com a mascara
    deltaAltura = (alturaMascara-1)//2
    # Quantos pixels pro a esquerda ou pra direita estamos acessando com a mascara
    deltaLargura = (larguraMascara-1)//2
    nova_imagem = []

    for i in range(0, len(imagem)):
        linha = []
        for j in range(0, len(imagem[0])):
            # Optamos por nao duplicar os pixels das bordas novamente entao estamos so repetindo eles confiando
            # na margem do texto
            if (i <= deltaAltura or i >= len(imagem)-deltaAltura) or (j <= deltaLargura or j >= len(imagem[0])-deltaLargura):
                linha.append(imagem[i][j])

            # Se todos os pixels na regiao da mascara forem 1 entao o pixel central sera 1
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


def contagem(imagem: Matriz):
    print("Contando palavras e linhas...")
    x = y = 0
    # Lista que armazena as coordenadas dos pontos para contornar cada palavra
    palavras = []

    # Percorre a imagem até encontrar a primeira palavra
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            if imagem[i][j] == 1:
                y = i
                x = j
                break
        if x != 0 or y != 0:
            break

    # Achando o pixel inferior esquerdo da primeira palavra da linha
    for i in range(y, len(imagem)):
        if imagem[i+1][x] == 0:
            y = i
            break

    linhas = 0
    while y < len(imagem):
        # Identificando as palavras e guardandos as coordenadas na lista "palavras"
        identificar_palavras(imagem, palavras, x, y)
        linhas += 1
        y += 1

        # Procurando a primeira palavra da proxima linha
        while imagem[y][x] == 0:
            y += 1
            if y >= len(imagem):
                break

        # Achando o pixel inferior esquerdo da palavra primira palavra da proxima linha
        for i in range(y, len(imagem)):
            if imagem[i+1][x] == 0:
                y = i
                break

    print(f"O arquivo possui:\n {linhas} linhas e {len(palavras)} palavras")
    return palavras


# Dizemos que possivelmente existe uma palavra entre (x, y) e (x, j) se existirem mais pixeis que o limiar
def e_palavra(imagem: Matriz, x: int, y: int, j: int, limiar: int) -> bool:
    contador = 0
    for i in range(j, y):
        if imagem[i][x] == 1:
            contador += 1

    if contador >= limiar:
        return True
    return False


def identificar_palavras(imagem: Matriz, palavras, x: int, y: int):
    x0 = x
    y0 = y
    #j = len(imagem)
    # Obtendo as coordenadas dos retangulos ao redor das palavras de uma linha
    while True:
        palavras.append(definir_bordas(imagem, x0, y0))
        x0 = palavras[-1][2][1]
        #j = j if j < palavras[-1][1][0] else palavras[-1][1][0]
        j = palavras[-1][1][0]
        # Coordenada que busca mirar em pixel proximo ao centro vertical da palavra
        y0 = (y+j)//2
        # Passando pelo espaco vazio entre as palavras da mesma linha
        while (not e_palavra(imagem, x0, y, j, (y-j)//2)) or imagem[y0][x0] == 0:
            x0 += 1
            if x0 >= len(imagem[0]):
                break

        if x0 >= len(imagem[0]):
            break




# Define os 3 cantos necessarios para tracar o retangulo ao redor da palavra
def definir_bordas(imagem: Matriz, x: int, y: int):
    i = x
    j = y

    # Busca o pixel superior esquerdo da palavra
    while imagem[j][x] == 1 and j > 0:
        j -= 1

    # Busca o pixel inferior esquerdo da palavra
    while imagem[y+1][x] == 1 and y < len(imagem):
        y += 1

    # Busca o pixel mais a direita da palavra
    while i < len(imagem[0]) and e_palavra(imagem, i, y, j, 1):
        i += 1

    # x, i => largura, y, j => altura
    # Estrutura => [pixel inferior esquerdo, pixel superior esquerdo, pixel inferior direito]
    # Essa estrutura representa uma palavra
    return [(y, x), (j, x), (y, i)]


# Desenha uma reta baseada nos dois pontos
def desenhar_reta(inicio, fim, imagem):
    if inicio[0] == fim[0]:
        for i in range(inicio[1], fim[1]):
            imagem[inicio[0]][i] = 1
    elif inicio[1] == fim[1]:
        for j in range(inicio[0], fim[0]):
            imagem[j][inicio[1]] = 1


# Escreve na imagem sem ruído os retangulos ao redor das palavras baseado nas coordenadas encontradas
# Circunscreve as palavras
def circunscrever_palavras(palavras, imagem: Matriz) -> Matriz:
    print("Circunscrevendo palavras...")
    for palavra in palavras:
        inferiorEsquerdo = palavra[0]
        superiorEsquerdo = palavra[1]
        inferiorDireito = palavra[2]
        superiorDireito = (superiorEsquerdo[0], inferiorDireito[1])

        desenhar_reta(superiorEsquerdo, inferiorEsquerdo, imagem)
        desenhar_reta(superiorEsquerdo, superiorDireito, imagem)
        desenhar_reta(superiorDireito, inferiorDireito, imagem)
        desenhar_reta(inferiorEsquerdo, inferiorDireito, imagem)

    return imagem
