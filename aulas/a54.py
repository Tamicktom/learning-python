# import type List
from typing import List
import os

"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar
valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes.
"""

shopping_list: List[str] = []


def addProduct(product: str) -> None:
    shopping_list.append(product)


def removeProduct(index: int) -> None:
    # verify if index exists
    if (index > len(shopping_list)):
        return print(f"Index {index} não existe dentro da lista.")
    shopping_list.pop(index)


def handleAddProduct():
    os.system("cls")
    product_name: str = input(
        "Digite o nome do produto que deseja adicionar: ")
    addProduct(product_name)
    print("Produto adicionado com sucesso!")


def handleRemoveProduct():
    os.system("cls")
    index: str = input("Digite o indice do produto que deseja remover")
    if (index.isnumeric() != True):
        print("Você não digitou um número!")
        input()
        return
    num_index: int = int(index)
    removeProduct(num_index)


def handleListProducts():
    os.system("cls")
    products = enumerate(shopping_list)
    for index, product in products:
        print(f"{index} - {product}")
    print("")
    input("Pressione qualquer tecla para continuar.")


def shoppingSession():
    keep_shopping: bool = True
    while keep_shopping:
        os.system("cls")
        print("Lista de compras")
        print("Digite uma opção:")
        print("[0] - Adicionar produto")
        print("[1] - Remover produto")
        print("[2] - Listar")
        print("[3] - Sair")

        option = input()

        if (option == "0"):
            handleAddProduct()
        if (option == "1"):
            handleRemoveProduct()
        if (option == "2"):
            handleListProducts()
        if (option == "3"):
            keep_shopping = False


shoppingSession()
