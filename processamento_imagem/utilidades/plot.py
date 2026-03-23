"""
processamento_imagem.utilidades.plot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Funções de visualização de imagens e histogramas via Matplotlib.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def exibir_imagem(
    image: np.ndarray,
    titulo: str = "Imagem",
    figsize: tuple[int, int] = (8, 6),
) -> None:
    """Exibe uma única imagem em escala de cinza ou colorida.

    Args:
        image:   Array NumPy da imagem (2-D ou H × W × 3).
        titulo:  Título exibido acima da imagem.
        figsize: Tamanho da figura em polegadas (largura, altura).

    Example:
        >>> exibir_imagem(img, titulo="Foto original")
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(image, cmap="gray" if image.ndim == 2 else None)
    ax.set_title(titulo, fontsize=13)
    ax.axis("off")
    fig.tight_layout()
    plt.show()


def exibir_resultado(
    *args: np.ndarray,
    titulos: list[str] | None = None,
    figsize: tuple[int, int] = (12, 4),
) -> None:
    """Exibe múltiplas imagens lado a lado para comparação.

    A última imagem é automaticamente rotulada como "Resultado" se nenhuma
    lista de títulos for fornecida.

    Args:
        *args:   Imagens a exibir (mínimo 2).
        titulos: Lista de títulos com o mesmo tamanho que ``args``.
                 Se omitido, usa "Imagem 1", "Imagem 2", … "Resultado".
        figsize: Tamanho total da figura.

    Raises:
        ValueError: Se ``titulos`` for fornecido com tamanho diferente de ``args``.

    Example:
        >>> exibir_resultado(img_original, img_diff, img_resultado)
        >>> exibir_resultado(a, b, c, titulos=["Antes", "Diferença", "Depois"])
    """
    n = len(args)
    if n < 1:
        raise ValueError("Forneça pelo menos uma imagem.")

    if titulos is not None and len(titulos) != n:
        raise ValueError(
            f"'titulos' deve ter {n} elementos, recebido {len(titulos)}."
        )

    if titulos is None:
        titulos = [f"Imagem {i}" for i in range(1, n)]
        titulos.append("Resultado")

    fig, axes = plt.subplots(nrows=1, ncols=n, figsize=figsize)
    if n == 1:
        axes = [axes]

    for ax, titulo, image in zip(axes, titulos, args):
        ax.imshow(image, cmap="gray" if image.ndim == 2 else None)
        ax.set_title(titulo, fontsize=11)
        ax.axis("off")

    fig.tight_layout()
    plt.show()


def exibir_histograma(
    image: np.ndarray,
    bins: int = 256,
    figsize: tuple[int, int] = (12, 4),
) -> None:
    """Plota o histograma de cada canal de cor (R, G, B) da imagem.

    Args:
        image:  Array NumPy colorido (H × W × 3). Se for 2-D (escala de
                cinza), exibe apenas um canal em tom cinza.
        bins:   Número de bins do histograma (padrão: 256).
        figsize: Tamanho da figura.

    Raises:
        ValueError: Se a imagem tiver número de canais inesperado.

    Example:
        >>> exibir_histograma(img_rgb)
    """
    if image.ndim == 2:
        # Escala de cinza
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(image.ravel(), bins=bins, color="gray", alpha=0.8)
        ax.set_title("Histograma — Escala de cinza")
        ax.set_xlabel("Intensidade")
        ax.set_ylabel("Frequência")
        fig.tight_layout()
        plt.show()
        return

    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError(
            f"Esperado array H×W×3, recebido shape: {image.shape}"
        )

    canais = [
        ("Red",   "red"),
        ("Green", "green"),
        ("Blue",  "blue"),
    ]

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=figsize,
                              sharex=True, sharey=True)

    for idx, (ax, (nome, cor)) in enumerate(zip(axes, canais)):
        ax.hist(
            image[:, :, idx].ravel(),
            bins=bins,
            color=cor,
            alpha=0.8,
            edgecolor="none",
        )
        ax.set_title(f"Canal {nome}", fontsize=11)
        ax.set_xlabel("Intensidade")
        ax.set_ylabel("Frequência" if idx == 0 else "")

    fig.suptitle("Histograma por canal de cor", fontsize=13, y=1.02)
    fig.tight_layout()
    plt.show()
