"""Testes unitários para processamento_imagem.processamento.transformar."""

import numpy as np
import pytest

from processamento_imagem.processamento.transformar import (
    redimensionar_imagem,
    recortar_imagem,
    rotacionar_imagem,
)


def imagem(h=100, w=80, c=3) -> np.ndarray:
    rng = np.random.default_rng(42)
    return rng.integers(0, 256, (h, w, c), dtype=np.uint8)


# ── redimensionar_imagem ──────────────────────────────────────────────────────

class TestRedimensionarImagem:

    def test_reduz_tamanho(self):
        img = imagem(100, 80)
        result = redimensionar_imagem(img, 0.5)
        assert result.shape[0] == 50
        assert result.shape[1] == 40

    def test_proporcao_1_mantem_shape(self):
        img = imagem(100, 80)
        result = redimensionar_imagem(img, 1.0)
        assert result.shape[:2] == (100, 80)

    def test_proporcao_zero_levanta_assertion(self):
        img = imagem()
        with pytest.raises(AssertionError):
            redimensionar_imagem(img, 0.0)

    def test_proporcao_negativa_levanta_assertion(self):
        img = imagem()
        with pytest.raises(AssertionError):
            redimensionar_imagem(img, -0.5)

    def test_proporcao_acima_de_1_levanta_assertion(self):
        img = imagem()
        with pytest.raises(AssertionError):
            redimensionar_imagem(img, 1.5)

    def test_preserva_canais(self):
        img = imagem(100, 80, 3)
        result = redimensionar_imagem(img, 0.5)
        assert result.shape[2] == 3


# ── recortar_imagem ───────────────────────────────────────────────────────────

class TestRecortarImagem:

    def test_recorta_regiao_correta(self):
        img = imagem(100, 80)
        recorte = recortar_imagem(img, topo=10, esquerda=20, altura=30, largura=40)
        assert recorte.shape[:2] == (30, 40)

    def test_regiao_fora_dos_limites_levanta_valor_error(self):
        img = imagem(100, 80)
        with pytest.raises(ValueError, match="ultrapassa os limites"):
            recortar_imagem(img, topo=90, esquerda=0, altura=20, largura=10)


# ── rotacionar_imagem ─────────────────────────────────────────────────────────

class TestRotacionar:

    def test_shape_preservado(self):
        img = imagem(60, 60)
        result = rotacionar_imagem(img, 45)
        assert result.shape == img.shape

    def test_rotacao_360_retorna_imagem_similar(self):
        img = imagem(60, 60).astype(np.float64) / 255
        result = rotacionar_imagem(img, 360)
        np.testing.assert_allclose(result, img, atol=1e-10)
