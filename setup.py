from setuptools import setup, find_packages
from pathlib import Path

# Lê o README para a descrição longa no PyPI
long_description = Path("README.md").read_text(encoding="utf-8")

# Lê dependências — ignora linhas em branco e comentários (#)
def parse_requirements(filename: str) -> list[str]:
    lines = Path(filename).read_text(encoding="utf-8").splitlines()
    return [
        line.strip()
        for line in lines
        if line.strip() and not line.strip().startswith("#")
    ]

setup(
    name="processamento-de-imagem",
    version="1.0.0",
    author="Rodrigo",
    author_email="",
    description="Processamento de imagens com scikit-image: comparação, transformação e visualização.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rpbrandao/processamento-de-imagem",
    packages=find_packages(exclude=["tests*", "docs*"]),
    install_requires=parse_requirements("requirements.txt"),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
    keywords="image processing scikit-image histogram ssim resize",
)
