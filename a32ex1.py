"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um
número inteiro, informe que não é um número inteiro.
"""

numero = input("Digite um número inteiro: ")

try:
    numero = int(numero)
    e_par = numero % 2 == 0
    if (e_par):
        print(f"O número {numero}, é par.")
    else:
        print(f"O número {numero} é ímpar.")
except:
    print("O número digitado não é inteiro.")
