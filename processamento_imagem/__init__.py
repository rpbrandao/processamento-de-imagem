"""
processamento_imagem
~~~~~~~~~~~~~~~~~~~~
Pacote Python para processamento de imagens com scikit-image.

Uso rápido::

    from processamento_imagem.utilidades import ler_imagem, exibir_resultado
    from processamento_imagem.processamento import encontrar_diferenca

    img1 = ler_imagem("foto_a.jpg")
    img2 = ler_imagem("foto_b.jpg")
    diff = encontrar_diferenca(img1, img2)
    exibir_resultado(img1, img2, diff, titulos=["Original", "Modificada", "Diferença"])
"""

from .processamento.combinar import encontrar_diferenca, transferir_histograma
from .processamento.transformar import (
    redimensionar_imagem,
    recortar_imagem,
    rotacionar_imagem,
)
from .utilidades.io import ler_imagem, salvar_imagem
from .utilidades.plot import exibir_imagem, exibir_resultado, exibir_histograma

__version__ = "1.0.0"
__author__  = "Rodrigo"

__all__ = [
    # processamento
    "encontrar_diferenca",
    "transferir_histograma",
    "redimensionar_imagem",
    "recortar_imagem",
    "rotacionar_imagem",
    # utilidades
    "ler_imagem",
    "salvar_imagem",
    "exibir_imagem",
    "exibir_resultado",
    "exibir_histograma",
]
