from typing import List, Union, Tuple

type SumProps = Union[List[Union[int, float]], Tuple[Union[int, float]]]


def soma(*num: SumProps) -> Union[int, float]:
    total = 0
    for n in num:
        total += n
    return total


print(soma(1, 2, 3, 4, 5.5))

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(soma(*numeros))