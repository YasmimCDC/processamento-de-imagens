from filtros import *


def histograma(imagem: Matriz, altura: int, largura: int, qtd_tons: int) -> List[int]:
    intensidades = [0 for x in range(0, qtd_tons + 1)]

    for i in range(altura):
        for j in range(largura):
            pixel = imagem[i][j]
            intensidades[pixel] += 1

    return intensidades


def histograma_normalizado(histograma: List[int], qtd_pixels: int) -> List[float]:
    probabilidades = [nk/qtd_pixels for nk in histograma]
    return probabilidades


def histograma_cumulativo(histogram: List[float]) -> List[int]:
    hist_cumulativo = [histogram[0]]

    for h in range(1, len(histogram)):
        aux = histogram[h] + hist_cumulativo[h - 1]
        hist_cumulativo.append(aux)

    return hist_cumulativo


def equalizacao_histogramica(imagem: Matriz, altura: int, largura: int, qtd_tons: int):
    qtd_pixels = altura*largura
    intensidades = histograma(imagem, altura, largura, qtd_tons)
    internsidadesNormalizadas = histograma_normalizado(intensidades, qtd_pixels)
    intensidadesAcumuladas = histograma_cumulativo(internsidadesNormalizadas)

    for i in range(altura):
        for j in range(largura):
            pixel = imagem[i][j]
            imagem[i][j] = round(qtd_tons * intensidadesAcumuladas[pixel] / qtd_pixels)
