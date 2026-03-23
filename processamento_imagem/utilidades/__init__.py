"""Submódulo de utilidades — I/O e visualização."""

from .io import ler_imagem, salvar_imagem
from .plot import exibir_imagem, exibir_resultado, exibir_histograma

__all__ = [
    "ler_imagem",
    "salvar_imagem",
    "exibir_imagem",
    "exibir_resultado",
    "exibir_histograma",
]
