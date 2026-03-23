# processamento-de-imagem

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![scikit-image](https://img.shields.io/badge/scikit--image-0.19+-9E1B32?style=flat)](https://scikit-image.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

> Pacote Python para processamento de imagens com **scikit-image** — comparação, transformação e visualização.

---

## Funcionalidades

### Processamento
| Função | Descrição |
|--------|-----------|
| `encontrar_diferenca(img1, img2)` | Mapa de diferenças SSIM normalizado [0, 1] |
| `transferir_histograma(img1, img2)` | Transfere distribuição de cores de `img2` para `img1` |
| `redimensionar_imagem(img, proporcao)` | Redimensiona por fator em (0, 1] com anti-aliasing |
| `recortar_imagem(img, topo, esq, h, w)` | Recorta região retangular |
| `rotacionar_imagem(img, angulo)` | Rotaciona em graus (anti-horário) |

### Utilidades
| Função | Descrição |
|--------|-----------|
| `ler_imagem(path, is_gray)` | Lê JPG, PNG, TIFF, BMP… |
| `salvar_imagem(img, path)` | Salva e cria diretórios automaticamente |
| `exibir_imagem(img, titulo)` | Exibe uma única imagem |
| `exibir_resultado(*imgs, titulos)` | Exibe múltiplas imagens lado a lado |
| `exibir_histograma(img)` | Plota histograma por canal R/G/B |

---

## Instalação

```bash
pip install processamento-de-imagem
```

Ou direto do repositório:

```bash
git clone https://github.com/rpbrandao/processamento-de-imagem.git
cd processamento-de-imagem
pip install -e .
```

---

## Uso rápido

```python
from processamento_imagem import (
    ler_imagem,
    encontrar_diferenca,
    redimensionar_imagem,
    transferir_histograma,
    exibir_resultado,
    exibir_histograma,
)

# Carregar imagens
img_a = ler_imagem("foto_original.jpg")
img_b = ler_imagem("foto_modificada.jpg")

# Comparar estruturalmente
diff = encontrar_diferenca(img_a, img_b)
exibir_resultado(img_a, img_b, diff, titulos=["Original", "Modificada", "Diferença"])

# Redimensionar para 50%
img_pequena = redimensionar_imagem(img_a, 0.5)

# Transferir cores
img_noturna = ler_imagem("referencia_noite.jpg")
img_recolorida = transferir_histograma(img_a, img_noturna)
exibir_histograma(img_recolorida)
```

---

## Estrutura

```
processamento-de-imagem/
├── processamento_imagem/
│   ├── __init__.py                  # API pública
│   ├── processamento/
│   │   ├── combinar.py              # encontrar_diferenca, transferir_histograma
│   │   └── transformar.py           # redimensionar, recortar, rotacionar
│   └── utilidades/
│       ├── io.py                    # ler_imagem, salvar_imagem
│       └── plot.py                  # exibir_imagem, exibir_resultado, exibir_histograma
├── tests/
│   ├── test_combinar.py
│   ├── test_transformar.py
│   └── test_io.py
├── requirements.txt
├── requirements-dev.txt
├── setup.py
└── README.md
```

---

## Testes

```bash
pip install -r requirements-dev.txt
pytest tests/ -v --cov=processamento_imagem
```

---

## O que foi corrigido na refatoração

| Arquivo | Bug original | Correção |
|---------|-------------|----------|
| `combinar.py` | `image1.shappe` | `image1.shape` |
| `combinar.py` | `gary_image2` | `gray2` |
| `combinar.py` | `dif_image.np.min(dif_image)` | `np.min(diff)` com proteção ÷0 |
| `combinar.py` | `multichannel=True` quebra no skimage ≥ 0.19 | `channel_axis=-1` com fallback |
| `transformar.py` | Variável `imagem` não definida | Corrigido para `image` |
| `setup.py` | Lê linhas comentadas como dependências | `parse_requirements()` ignora `#` |
| `requirements.txt` | 20+ linhas comentadas | Apenas 3 dependências reais |
| `__init__.py` (todos) | Vazios, sem exports | API pública declarada com `__all__` |
