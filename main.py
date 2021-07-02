from mofologia_matematica.morfologia import *
from utils.menu_utils import *
from utils.processamento_de_arquivo import *
from filtros.filtros_simples import *
from filtros.histogramas import *
from filtros.mascaras import *


# Main do preOCR com imagens P1
def main():
    clear()

    print("Bem-vindo ao editor que apenas remove ruídos de imagens")
    print("=======================================================")

    caminho = obter_caminho()
    #altura_mascara = pegar_altura_mascara()

    imagem, altura, largura, tipo_imagem = extrair_imagem_p1(caminho)

    imagem = dilatacao(imagem, 5, 5)
    imagem = erosao(imagem, 3, 3)

    print(contagem(imagem))

    escrever_imagem(caminho, "pbm", imagem, altura, largura, tipo_imagem)


# Main dos exercicios com imagens P2
def main_P2():
    clear()

    print("Bem-vindo ao editor que só faz operação pontual")
    print("===============================================")
    print("Escolha a sua operacao:\n(1) Limiar\n(2) Negativo\n(3) Histograma\n(4) Equalizar\n(5) Borrar\n(6) Remover "
          "ruído\n(7) Dilatar")

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

    imagem, altura, largura, qtd_tons, tipo_imagem = extrair_imagem_p2(caminho)
    qtd_tons = int(qtd_tons)

    if operacao == 1:
        print("Forneca o limiar desejado:")
        limiar = obter_inteiro()
        if limiar is str:
            return

        limiarizar(imagem, limiar[0], altura, largura, qtd_tons)

    elif operacao == 2:
        negativar(imagem, altura, largura, qtd_tons)

    elif operacao == 3:
        hist = histograma(imagem, altura, largura, qtd_tons)
        escrever_arquivo(caminho, 'txt', hist, operacoes[operacao])
        return

    elif operacao == 4:
        equalizacao_histogramica(imagem, altura, largura, qtd_tons)

    elif operacao == 5:

        altura_mascara = pegar_altura_mascara()
        imagem = box_filter(imagem, altura_mascara)

    elif operacao == 6:

        altura_mascara = pegar_altura_mascara()
        imagem = mediana(imagem, altura_mascara)

    elif operacao == 7:

        #ltura_mascara = pegar_altura_mascara()
        imagem = dilatacao(imagem)

    else:
        print("Operação inválida, abortando...")
        return

    escrever_imagem(caminho, "pgm", imagem, altura, largura, tipo_imagem, qtd_tons, operacoes[operacao])


if __name__ == "__main__":
    main()
