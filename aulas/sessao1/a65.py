from typing import List

def imprimir(a, b, c):
    print(a)
    print(b)
    print(c)


# imprimir(1, 2, 3)

type Vector = List[float]

def saudacao(nome:str):
    print(f'Olá {nome}')
    
saudacao('Maria')
saudacao();