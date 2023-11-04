"""
enumerate - enumera iteráveis (indices)
"""

from typing import List

lista: List[str] = ["abacate", "bola", "cachorro"]

lista.append("dinheiro")


for indice, valor in enumerate(lista):
    print(indice, valor)
