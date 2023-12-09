from typing import List, Union, Tuple

""" Exercicios com funções

crie uma função que multiplica todos os argumentos
não nomeados recebidos
retorne o total para uma variavel e mostre o valor
da variavel no final

crie uma função que fala se um número é par ou impar
"""

type MultiplyProps = Union[List[Union[int, float]], Tuple[Union[int, float]]]


def multiplica(*num: MultiplyProps) -> Union[int, float]:
    total = 1
    for n in num:
        total *= n
    return total


print(multiplica(1, 2, 3))


def par_impar(num: int) -> str:
    if num % 2 == 0:
        return "par"
    return "impar"


print(par_impar(2))
print(par_impar(3))
