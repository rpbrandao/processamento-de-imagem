"""Testes unitários para processamento_imagem.utilidades.io."""

import numpy as np
import pytest
from pathlib import Path

from processamento_imagem.utilidades.io import ler_imagem, salvar_imagem


class TestLerImagem:

    def test_arquivo_inexistente_levanta_file_not_found(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            ler_imagem(tmp_path / "nao_existe.jpg")

    def test_extensao_invalida_levanta_valor_error(self, tmp_path):
        f = tmp_path / "arquivo.xyz"
        f.write_bytes(b"dados")
        with pytest.raises(ValueError, match="não suportada"):
            ler_imagem(f)


class TestSalvarImagem:

    def test_salva_e_le_imagem_corretamente(self, tmp_path):
        img = np.zeros((10, 10, 3), dtype=np.uint8)
        img[5, 5] = [255, 0, 0]
        caminho = tmp_path / "test.png"
        salvar_imagem(img, caminho)
        assert caminho.exists()
        lida = ler_imagem(caminho)
        assert lida.shape == img.shape

    def test_cria_diretorios_automaticamente(self, tmp_path):
        img = np.zeros((5, 5, 3), dtype=np.uint8)
        caminho = tmp_path / "subdir" / "deep" / "img.png"
        salvar_imagem(img, caminho)
        assert caminho.exists()

    def test_tipo_invalido_levanta_type_error(self, tmp_path):
        with pytest.raises(TypeError):
            salvar_imagem([[1, 2], [3, 4]], tmp_path / "img.png")
