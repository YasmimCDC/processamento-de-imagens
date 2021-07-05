from mofologia_matematica.morfologia import *
from utils.menu_utils import *
from utils.processamento_de_arquivo import *
from filtros.mascaras import *


# Main do preOCR com imagens P1
def main():
    clear()

    print("Bem-vindo ao editor que apenas remove ruídos de imagens")
    print("=======================================================")

    caminho = obter_caminho()

    imagem, altura, largura, tipo_imagem = extrair_imagem_p1(caminho)
    imagem = mediana(imagem, 3)

    imagemDeSaida = [x for x in imagem]

    imagem = dilatacao(imagem, 7, 9)
    imagem = erosao(imagem, 5, 3)

    coordenadasDasPalavras = contagem(imagem)
    imagemDeSaida = circunscrever_palavras(coordenadasDasPalavras, imagemDeSaida)

    escrever_imagem(caminho, "pbm", imagemDeSaida, altura, largura, tipo_imagem)


if __name__ == "__main__":
    main()
