nome = input("Qual seu nome? ")
numero_1 = input("Digite um número: ")
numero_2 = input("Digite outro número: ")

# verify if the input is a number
if numero_1.isnumeric() and numero_2.isnumeric():
    print(f"Olá {nome=}! Seja bem vindo(a)!")
    print(f"A soma de {numero_1=} e {numero_2=} é {numero_1 + numero_2}")
else:
    print("Você não digitou um número!")
