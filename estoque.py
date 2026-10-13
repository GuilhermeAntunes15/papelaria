import csv
import os

ARQUIVO = "dados/produtos.csv"
CAMPOS = ["codigo", "nome", "preco", "quantidade"]


def eh_numero(texto):
    """Diz se o texto é um número positivo, aceitando vírgula ou ponto (ex.: 3,50)."""
    texto = texto.strip().replace(",", ".", 1)
    return texto.replace(".", "", 1).isdigit()