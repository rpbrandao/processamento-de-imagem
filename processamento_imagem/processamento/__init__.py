"""Submódulo de processamento — comparação, transformação e combinação."""

from .combinar import encontrar_diferenca, transferir_histograma
from .transformar import redimensionar_imagem, recortar_imagem, rotacionar_imagem

__all__ = [
    "encontrar_diferenca",
    "transferir_histograma",
    "redimensionar_imagem",
    "recortar_imagem",
    "rotacionar_imagem",
]
