"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar o código
"""

numero_str: str = input('Digite um número: ')

try:
    numero_float: float = float(numero_str)
    print(f"O dobro de {numero_float:.0f} é {numero_float * 2:.0f}")
except:
    print("Digite um número válido")
