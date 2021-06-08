import os
from typing import *

from filtros.mascaras import validar_mascara

operacoes = {
    1: "Limiar",
    2: "Negativo",
    3: "Histograma",
    4: "Equalizar",
    5: "Borrar",
    6: "Remover_ruído",
}


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def try_parse_int(numero: Any) -> [Any, bool]:
    try:
        return int(numero), True
    except ValueError:
        return numero, False


def obter_caminho() -> str:
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


def obter_inteiro() -> Any:
    inteiro, conseguiu = try_parse_int(input())

    while not conseguiu:
        print("Entrada invalida, por favor digite um numero inteiro ou envie 'q' para sair")
        inteiro, conseguiu = try_parse_int(input())

        if inteiro == "q":
            break

    return inteiro


def pegar_altura_mascara() -> Optional[int]:
    print("Forneca a altura da mascara: ")

    k = obter_inteiro()
    if k is str:
        return

    valido = validar_mascara(k)

    while not valido:
        k = obter_inteiro()

        if k is str:
            return

        valido = validar_mascara(k)

    return k


def validar_caminho(caminho: str) -> bool:
    arquivo_existe = os.path.isfile(caminho)
    return arquivo_existe


def validar_operacao(operacao: int) -> bool:
    op = [1, 2, 3, 4, 5, 6]

    if operacao in op:
        return True
    else:
        print("Operação inválida, por favor digite uma das operações do menu")
        return False
