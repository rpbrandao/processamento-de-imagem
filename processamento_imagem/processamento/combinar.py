"""
processamento_imagem.processamento.combinar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Funções para comparação e combinação de imagens.
"""

from __future__ import annotations

import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def encontrar_diferenca(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    """Calcula a diferença estrutural normalizada entre duas imagens.

    Converte ambas as imagens para escala de cinza, aplica a métrica SSIM
    e retorna o mapa de diferenças normalizado no intervalo [0, 1].

    Args:
        image1: Imagem de referência (H × W × 3).
        image2: Imagem para comparar — deve ter o mesmo shape de ``image1``.

    Returns:
        Array 2-D (H × W) normalizado em [0, 1]. Valores próximos de 0
        indicam regiões idênticas; próximos de 1 indicam grande diferença.

    Raises:
        AssertionError: Se os shapes forem diferentes.

    Example:
        >>> diff = encontrar_diferenca(img_a, img_b)
        >>> print(diff.min(), diff.max())  # 0.0  1.0
    """
    # BUG CORRIGIDO: 'image1.shappe' → 'image1.shape'
    assert image1.shape == image2.shape, (
        f"As imagens devem ter o mesmo shape. "
        f"Recebido: {image1.shape} e {image2.shape}."
    )

    gray1 = rgb2gray(image1)
    # BUG CORRIGIDO: 'gary_image2' → 'gray2'
    gray2 = rgb2gray(image2)

    score, diff = structural_similarity(gray1, gray2, full=True, data_range=1.0)
    print(f"Índice de Similaridade Estrutural (SSIM): {score:.4f}")

    # BUG CORRIGIDO: 'dif_image.np.min(dif_image)' → normalização correta
    diff_min = np.min(diff)
    diff_max = np.max(diff)
    denom = diff_max - diff_min

    # Proteção contra divisão por zero (imagens idênticas)
    if denom == 0:
        return np.zeros_like(diff, dtype=np.float64)

    return (diff - diff_min) / denom


def transferir_histograma(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    """Transfere a distribuição de cores de ``image2`` para ``image1``.

    Args:
        image1: Imagem de entrada cujo histograma será ajustado.
        image2: Imagem de referência para o histograma alvo.

    Returns:
        Imagem com o conteúdo de ``image1`` e a distribuição de ``image2``.

    Example:
        >>> resultado = transferir_histograma(foto_dia, foto_noite)
    """
    # BUG CORRIGIDO: multichannel=True removido no skimage >= 0.19
    # Usa channel_axis=-1 (moderno) com fallback para versões antigas
    try:
        return match_histograms(image1, image2, channel_axis=-1)
    except TypeError:
        return match_histograms(image1, image2, multichannel=True)  # type: ignore[call-arg]
