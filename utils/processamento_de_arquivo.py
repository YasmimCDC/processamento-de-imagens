import os
import re
from typing import *

Matriz = List[List[int]]


def extrair_imagem(dir: str) -> [Matriz, int, int, int, str]:
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


def escrever_imagem(dir: str,
                    operacao: str,
                    extensao: str,
                    matriz: Matriz,
                    linhas: int,
                    colunas: int,
                    qtd_tons: int,
                    tipo_imagem: str):
    dir_escrita = definir_caminho_de_saida(dir, operacao, extensao)

    with open(dir_escrita, "w") as novo_arquivo:
        novo_arquivo.write(tipo_imagem + "\n")
        novo_arquivo.write("# Imagem processada\n")
        novo_arquivo.write(str(colunas) + " " + str(linhas) + "\n")
        novo_arquivo.write(str(qtd_tons) + "\n")

        for x in range(linhas):
            for y in range(colunas):
                novo_arquivo.write(str(matriz[x][y]) + "\n")

    novo_arquivo.close()


def escrever_arquivo(dir: str,
                    operacao: str,
                    extensao: str,
                    dados: List[int]):

    dir_escrita = definir_caminho_de_saida(dir, operacao, extensao)

    with open(dir_escrita, "w") as novo_arquivo:
        novo_arquivo.write("# Arquivo gerado para analise de operacoes\n")

        for x in range(len(dados)):
            novo_arquivo.write(str(dados[x]) + "\n")

    novo_arquivo.close()


def definir_caminho_de_saida(caminho: str,  operacao: str, extensao: str) -> str:
    nome_arquivo_entrada = os.path.basename(caminho)

    if not os.path.isdir("../output"):
        os.mkdir("../output/")

    caminho_saida = "output/" + re.search(r"^(.+)(?:\.pgm)$", nome_arquivo_entrada).group(1) + "_" + operacao + "." + extensao

    return caminho_saida
