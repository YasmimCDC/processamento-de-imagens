import os
import re
from typing import *

Matriz = List[List[int]]


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def try_parse_int(numero) -> [Any, bool]:
    try:
        return int(numero), True
    except ValueError:
        return numero, False


def obter_caminho():
    print("Forneca o caminho da imagem:")

    caminho = str(input())
    valido = validar_caminho(caminho)

    while not valido:
        print("Caminho inválido, por favor forneca um caminho válido ou envie 'q' para sair")
        caminho = obter_caminho()

        if caminho == "q":
            break

        valido = validar_caminho(caminho)

    return caminho


def obter_inteiro():
    inteiro, conseguiu = try_parse_int(input())

    while not conseguiu:
        print("Entrada invalida, por favor digite um numero inteiro ou envie 'q' para sair")
        inteiro, conseguiu = try_parse_int(input())

        if inteiro == "q":
            break

    return inteiro


def validar_caminho(caminho):
    arquivo_existe = os.path.isfile(caminho)
    return arquivo_existe


def extrair_imagem(dir: str) -> [Matriz, int, int, int, str]:
    with open(dir, "r") as arquivo:
        imagem = arquivo.read().splitlines()
        tipo_imagem = imagem[0]
        linhas, colunas = imagem[2].split()
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
        novo_arquivo.write(str(linhas) + " " + str(colunas) + "\n")
        novo_arquivo.write(str(qtd_tons) + "\n")

        for x in range(linhas):
            for y in range(colunas):
                novo_arquivo.write(str(matriz[x][y]) + "\n")

    novo_arquivo.close()


def definir_caminho_de_saida(caminho: str,  operacao: str, extensao: str) -> str:
    nome_arquivo_entrada = os.path.basename(caminho)

    if not os.path.isdir("../output"):
        os.mkdir("../output/")

    caminho_saida = "output/" + re.search(r"^(.+)(?:\.pgm)$", nome_arquivo_entrada).group(1) + "_" + operacao + "." + extensao

    return caminho_saida
