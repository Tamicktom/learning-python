from typing import List, Dict, Union

type Person = Dict[str, Union[str, int]]

lista: List[Person] = [
    {
        "nome": "João",
        "idade": 25,
    },
    {
        "nome": "Maria",
        "idade": 30,
    },
    {
        "nome": "José",
        "idade": 18,
    },
    {
        "nome": "Pedro",
        "idade": 22,
    },
    {
        "nome": "Ana",
        "idade": 27,
    },
]


def orderByAge(peoples: List[Person]) -> List[Person]:
    return sorted(peoples, key=lambda person: person["idade"])


def orderByName(peoples: List[Person]) -> List[Person]:
    return sorted(peoples, key=lambda person: person["nome"])


print(orderByAge(lista))
print(orderByName(lista))