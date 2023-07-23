"""
Faça um programa que pergunta a hora ao usuário e, baseando-se no horário
descrito, exiba uma saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Digite a hora atual: ")

# converte a hora para inteiro
try:
    hora = int(hora)
    if hora < 0 or hora > 23:
        print("Hora inválida.")
        exit()
except:
    print("Hora inválida.")
    exit()


if hora <= 11:
    print("Bom dia!")
elif hora <= 17:
    print("Boa tarde!")
else:
    print("Boa noite!")
