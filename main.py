from utils.menu_utils import *
from utils.processamento_de_arquivo import *
from filtros.filtros_simples import *
from filtros.histogramas import *
from filtros.mascaras import *


def main() -> None:
    clear()

    print("Bem vindo ao editor que só faz operação pontual")
    print("===============================================")
    print("Escolha a sua operacao:\n(1) Limiar\n(2) Negativo\n(3) Histograma\n(4) Equalizar\n(5) Borrar\n(6) Remover "
          "ruído")

    operacao = obter_inteiro()
    valido = validar_operacao(operacao)

    while not valido:
        k = obter_inteiro()
        if k is str:
            return
        valido = validar_operacao(k)

    caminho = obter_caminho()

    if caminho == "q":

        return

    imagem, altura, largura, qtd_tons, tipo_imagem = extrair_imagem(caminho)
    qtd_tons = int(qtd_tons)

    if operacao == 1:
        print("Forneca o limiar desejado:")
        limiar = obter_inteiro()
        if not limiar.isnumeric():
            return

        limiarizar(imagem, limiar[0], altura, largura, qtd_tons)

    elif operacao == 2:
        negativar(imagem, altura, largura, qtd_tons)

    elif operacao == 3:
        hist = histograma(imagem, altura, largura, qtd_tons)
        escrever_arquivo(caminho, operacoes[operacao], 'txt', hist)
        return

    elif operacao == 4:
        equalizacao_histogramica(imagem, altura, largura, qtd_tons)

    elif operacao == 5:
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

        imagem = box_filter(imagem, k)

    elif operacao == 6:
        imagem = mediana(imagem, altura, largura)

    else:
        print("Operação inválida, abortando...")
        return

    escrever_imagem(caminho, operacoes[operacao], "pgm", imagem, altura, largura, qtd_tons, tipo_imagem)


if __name__ == "__main__":
    main()
