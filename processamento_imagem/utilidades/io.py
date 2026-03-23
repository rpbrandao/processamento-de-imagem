"""
processamento_imagem.utilidades.io
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Funções para leitura e escrita de imagens em disco.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from skimage.io import imread, imsave


def ler_imagem(path: str | Path, is_gray: bool = False) -> np.ndarray:
    """Lê uma imagem do disco e retorna um array NumPy.

    Args:
        path:    Caminho para o arquivo de imagem (JPG, PNG, BMP, TIFF…).
        is_gray: Se ``True``, converte para escala de cinza (array 2-D).
                 Se ``False`` (padrão), retorna RGB (array H × W × 3).

    Returns:
        Array NumPy com dtype uint8 (ou float64 se gray=True).

    Raises:
        FileNotFoundError: Se o arquivo não existir.
        ValueError:        Se a extensão não for suportada.

    Example:
        >>> img = ler_imagem("foto.jpg")
        >>> img_cinza = ler_imagem("foto.jpg", is_gray=True)
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    extensoes_suportadas = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif", ".webp"}
    if path.suffix.lower() not in extensoes_suportadas:
        raise ValueError(
            f"Extensão '{path.suffix}' não suportada. "
            f"Use uma de: {sorted(extensoes_suportadas)}"
        )

    return imread(str(path), as_gray=is_gray)


def salvar_imagem(image: np.ndarray, path: str | Path) -> None:
    """Salva um array NumPy como arquivo de imagem.

    Se o diretório de destino não existir, ele é criado automaticamente.

    Args:
        image: Array NumPy da imagem a ser salva.
        path:  Caminho de destino (a extensão determina o formato).

    Raises:
        ValueError: Se a extensão não for suportada.
        TypeError:  Se ``image`` não for um array NumPy.

    Example:
        >>> salvar_imagem(img_processada, "output/resultado.png")
    """
    if not isinstance(image, np.ndarray):
        raise TypeError(f"'image' deve ser np.ndarray, recebido: {type(image).__name__}")

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    imsave(str(path), image)
    print(f"Imagem salva em: {path.resolve()}")
