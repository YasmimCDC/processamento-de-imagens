import os
import re
from typing import *

Matriz = List[List[int]]


def extrair_imagem_p2(dir: str) -> [Matriz, int, int, int, str]:
    print("Extraindo dados da imagme...")
    with open(dir, "r") as arquivo:
        imagem = arquivo.read().splitlines()
        tipo_imagem = imagem[0]
        colunas, linhas = imagem[2].split()
        qtd_tons = int(imagem[3])

        matriz = []
        cont = 4
        for i in range(int(linhas)):
            linha = []
            for j in range(int(colunas)):
                linha.append(int(imagem[cont]))
                cont = cont + 1

            matriz.append(linha)

    arquivo.close()

    return matriz, int(linhas), int(colunas), qtd_tons, tipo_imagem


def extrair_imagem_p1(dir: str) -> [Matriz, int, int, str]:
    print("Extraindo dados da imagem...")
    with open(dir, "r") as arquivo:
        tipo_imagem = arquivo.readline()
        arquivo.readline()
        colunas, linhas = [int(x) for x in arquivo.readline().split()]

        matriz = []
        linha = []

        cont = 0
        for line in arquivo:
            for s in line:
                if s != '\n':
                    if cont < colunas:
                        linha.append(int(s))
                        cont += 1
                    else:
                        matriz.append(linha)
                        linha = [int(s)]
                        cont = 1

        matriz.append(linha)

    arquivo.close()

    return matriz, linhas, colunas, tipo_imagem


def escrever_imagem(dir: str,
                    extensao: str,
                    matriz: Matriz,
                    linhas: int,
                    colunas: int,
                    tipo_imagem: str,
                    qtd_tons: int = None,
                    operacao: str = None):
    dir_escrita = definir_caminho_de_saida(dir, extensao, operacao)
    print("Criando nova imagem...")
    with open(dir_escrita, "w") as novo_arquivo:
        novo_arquivo.write(tipo_imagem)
        novo_arquivo.write("# Imagem processada\n")
        novo_arquivo.write(str(colunas) + " " + str(linhas) + "\n")
        if qtd_tons is not None:
            novo_arquivo.write(str(qtd_tons) + "\n")

        for x in range(linhas):
            for y in range(colunas):
                novo_arquivo.write(str(matriz[x][y]) + "\n")

    novo_arquivo.close()


def escrever_arquivo(dir: str,
                    extensao: str,
                    dados: List[int],
                    operacao: str = None):

    dir_escrita = definir_caminho_de_saida(dir, extensao, operacao)

    with open(dir_escrita, "w") as novo_arquivo:

        novo_arquivo.write("# Arquivo gerado para analise de operacoes\n")

        for x in range(len(dados)):
            novo_arquivo.write(str(dados[x]) + "\n")

    novo_arquivo.close()


def definir_caminho_de_saida(caminho: str, extensao: str, operacao: str = None) -> str:
    nome_arquivo_entrada = os.path.basename(caminho)

    if not os.path.isdir("output"):
        os.mkdir("output/")

    if operacao is None:
        caminho_saida = "output/" + nome_arquivo_entrada
    else:
        caminho_saida = "output/" + re.search(r"^(.+)(?:\.pgm)$", nome_arquivo_entrada).group(1) + "_" + operacao + "." + extensao

    return caminho_saida
