# Introdução a List Comprehension

from typing import List, Dict, Union

lista:List[int] = [];

for i in range(1, 11):
    lista.append(i)

print(lista)

# List Comprehension
# [expression for item in iterable if condition]

lista = [i for i in range(1, 11)]
print(lista)

# List Comprehension com condicional
# [expression for item in iterable if condition]

lista = [i for i in range(1, 11) if i % 2 == 0]
print(lista)