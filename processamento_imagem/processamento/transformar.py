"""
processamento_imagem.processamento.transformar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Funções de transformação geométrica de imagens.
"""

from __future__ import annotations

import numpy as np
from skimage.transform import resize


def redimensionar_imagem(image: np.ndarray, proporcao: float) -> np.ndarray:
    """Redimensiona uma imagem por um fator de proporção.

    Mantém a relação de aspecto original. Usa anti-aliasing para evitar
    artefatos ao reduzir a imagem.

    Args:
        image:     Array NumPy da imagem (H × W ou H × W × C).
        proporcao: Fator de escala no intervalo (0, 1].
                   Ex.: 0.5 reduz a imagem à metade.

    Returns:
        Imagem redimensionada com valores em [0, 1] (float64).

    Raises:
        AssertionError: Se ``proporcao`` não estiver em (0, 1].

    Example:
        >>> img_menor = redimensionar_imagem(img, 0.5)
        >>> print(img_menor.shape)  # (H/2, W/2, C)
    """
    assert 0 < proporcao <= 1, (
        f"Informe uma proporção em (0, 1]. Recebido: {proporcao!r}"
    )

    height = round(image.shape[0] * proporcao)
    width  = round(image.shape[1] * proporcao)

    # BUG CORRIGIDO: variável 'imagem' não definida → deve ser 'image'
    imagem_redimensionada = resize(image, (height, width), anti_aliasing=True)
    return imagem_redimensionada


def recortar_imagem(
    image: np.ndarray,
    topo: int,
    esquerda: int,
    altura: int,
    largura: int,
) -> np.ndarray:
    """Recorta uma região retangular da imagem.

    Args:
        image:    Array NumPy da imagem.
        topo:     Coordenada Y do canto superior esquerdo do recorte.
        esquerda: Coordenada X do canto superior esquerdo do recorte.
        altura:   Altura do recorte em pixels.
        largura:  Largura do recorte em pixels.

    Returns:
        Sub-array correspondente à região recortada.

    Raises:
        ValueError: Se a região especificada ultrapassar os limites da imagem.

    Example:
        >>> recorte = recortar_imagem(img, topo=10, esquerda=20, altura=100, largura=200)
    """
    h, w = image.shape[:2]

    if topo + altura > h or esquerda + largura > w:
        raise ValueError(
            f"Região de recorte ({topo}:{topo+altura}, {esquerda}:{esquerda+largura}) "
            f"ultrapassa os limites da imagem ({h} × {w})."
        )

    return image[topo : topo + altura, esquerda : esquerda + largura]


def rotacionar_imagem(image: np.ndarray, angulo: float) -> np.ndarray:
    """Rotaciona uma imagem por um ângulo em graus (sentido anti-horário).

    Args:
        image:  Array NumPy da imagem.
        angulo: Ângulo de rotação em graus.

    Returns:
        Imagem rotacionada (mesmo shape da entrada).

    Example:
        >>> img_rotacionada = rotacionar_imagem(img, 90)
    """
    from skimage.transform import rotate
    return rotate(image, angulo, preserve_range=True).astype(image.dtype)
