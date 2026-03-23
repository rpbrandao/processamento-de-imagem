"""
tests/test_processamento.py
Testes unitários para o pacote processamento_imagem.
"""

import numpy as np
import pytest

from processamento_imagem.processamento.combinar import (
    encontrar_diferenca,
    transferir_histograma,
)
from processamento_imagem.processamento.transformar import redimensionar_imagem


# ── Fixtures ────────────────────────────────────────────────────────────────

@pytest.fixture
def imagem_rgb():
    """Imagem RGB sintética 60×80."""
    rng = np.random.default_rng(42)
    return (rng.integers(0, 256, size=(60, 80, 3), dtype=np.uint8))


@pytest.fixture
def imagem_rgb_2():
    """Segunda imagem RGB sintética 60×80."""
    rng = np.random.default_rng(99)
    return (rng.integers(0, 256, size=(60, 80, 3), dtype=np.uint8))


# ── encontrar_diferenca ──────────────────────────────────────────────────────

class TestEncontrarDiferenca:
    def test_retorna_array_2d(self, imagem_rgb, imagem_rgb_2):
        diff = encontrar_diferenca(imagem_rgb, imagem_rgb_2)
        assert diff.ndim == 2

    def test_normalizado_entre_0_e_1(self, imagem_rgb, imagem_rgb_2):
        diff = encontrar_diferenca(imagem_rgb, imagem_rgb_2)
        assert diff.min() >= 0.0
        assert diff.max() <= 1.0

    def test_imagens_identicas_retorna_zeros(self, imagem_rgb):
        diff = encontrar_diferenca(imagem_rgb, imagem_rgb)
        assert diff.max() == 0.0

    def test_shapes_diferentes_levanta_assertion(self):
        img1 = np.zeros((60, 80, 3), dtype=np.uint8)
        img2 = np.zeros((50, 80, 3), dtype=np.uint8)
        with pytest.raises(AssertionError, match="mesmo formato"):
            encontrar_diferenca(img1, img2)


# ── transferir_histograma ────────────────────────────────────────────────────

class TestTransferirHistograma:
    def test_retorna_mesmo_shape(self, imagem_rgb, imagem_rgb_2):
        resultado = transferir_histograma(imagem_rgb, imagem_rgb_2)
        assert resultado.shape == imagem_rgb.shape

    def test_retorna_array_numpy(self, imagem_rgb, imagem_rgb_2):
        resultado = transferir_histograma(imagem_rgb, imagem_rgb_2)
        assert isinstance(resultado, np.ndarray)


# ── redimensionar_imagem ─────────────────────────────────────────────────────

class TestRedimensionarImagem:
    def test_metade_do_tamanho(self, imagem_rgb):
        resultado = redimensionar_imagem(imagem_rgb, 0.5)
        assert resultado.shape[0] == round(60 * 0.5)
        assert resultado.shape[1] == round(80 * 0.5)

    def test_preserva_canais_de_cor(self, imagem_rgb):
        resultado = redimensionar_imagem(imagem_rgb, 0.5)
        assert resultado.shape[2] == 3

    def test_proporcao_1_mantem_tamanho(self, imagem_rgb):
        resultado = redimensionar_imagem(imagem_rgb, 1.0)
        assert resultado.shape[:2] == (60, 80)

    def test_proporcao_zero_levanta_assertion(self, imagem_rgb):
        with pytest.raises(AssertionError, match="intervalo"):
            redimensionar_imagem(imagem_rgb, 0.0)

    def test_proporcao_negativa_levanta_assertion(self, imagem_rgb):
        with pytest.raises(AssertionError):
            redimensionar_imagem(imagem_rgb, -0.5)

    def test_proporcao_maior_que_1_levanta_assertion(self, imagem_rgb):
        with pytest.raises(AssertionError):
            redimensionar_imagem(imagem_rgb, 1.5)

    def test_imagem_grayscale(self):
        img_gray = np.zeros((60, 80), dtype=np.uint8)
        resultado = redimensionar_imagem(img_gray, 0.5)
        assert resultado.shape == (30, 40)
