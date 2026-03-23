"""Testes unitários para processamento_imagem.processamento.combinar."""

import numpy as np
import pytest

from processamento_imagem.processamento.combinar import (
    encontrar_diferenca,
    transferir_histograma,
)


def imagem_rgb(h=50, w=50, seed=0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, (h, w, 3), dtype=np.uint8)


def imagem_float(h=50, w=50, seed=0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.random((h, w, 3)).astype(np.float64)


# ── encontrar_diferenca ───────────────────────────────────────────────────────

class TestEncontrarDiferenca:

    def test_retorna_array_2d(self):
        img = imagem_float()
        diff = encontrar_diferenca(img, img)
        assert diff.ndim == 2

    def test_valores_normalizados_0_a_1(self):
        a = imagem_float(seed=1)
        b = imagem_float(seed=2)
        diff = encontrar_diferenca(a, b)
        assert diff.min() >= 0.0 - 1e-9
        assert diff.max() <= 1.0 + 1e-9

    def test_imagens_identicas_retornam_zeros(self):
        img = imagem_float()
        diff = encontrar_diferenca(img, img)
        np.testing.assert_array_equal(diff, np.zeros_like(diff))

    def test_shapes_diferentes_levantam_assertion(self):
        a = imagem_float(h=50, w=50)
        b = imagem_float(h=60, w=60)
        with pytest.raises(AssertionError, match="mesmo shape"):
            encontrar_diferenca(a, b)

    def test_shape_resultado_igual_ao_input(self):
        a = imagem_float(h=40, w=80)
        b = imagem_float(h=40, w=80)
        diff = encontrar_diferenca(a, b)
        assert diff.shape == (40, 80)


# ── transferir_histograma ─────────────────────────────────────────────────────

class TestTransferirHistograma:

    def test_shape_preservado(self):
        src = imagem_rgb(seed=1)
        ref = imagem_rgb(seed=2)
        result = transferir_histograma(
            src.astype(np.float64) / 255,
            ref.astype(np.float64) / 255,
        )
        assert result.shape == src.shape

    def test_retorna_ndarray(self):
        src = imagem_rgb(seed=3).astype(np.float64) / 255
        ref = imagem_rgb(seed=4).astype(np.float64) / 255
        result = transferir_histograma(src, ref)
        assert isinstance(result, np.ndarray)
