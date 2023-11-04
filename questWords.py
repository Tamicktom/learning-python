import random
import os

"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

 - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma leta.
 - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palabvra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra.
    - Se a letra digitada não estiver na palavra secreta; exxiba *.
Faça a contagem de tentativas do seu usuário.
"""

print("Jogo de acertar as palavras.")
print("Você tem 5 tentativas para acertar a palavra secreta. Em cada tentativa você pode digitar apenas uma letra.")

palavras = {"casa": "lugar onde moramos", "carro": "meio de transporte", "moto": "meio de transporte", "bicicleta": "meio de transporte", "computador": "aparelho eletrônico", "celular": "aparelho eletrônico", "televisão": "aparelho eletrônico", "cadeira": "móvel para sentar", "mesa": "móvel para apoiar objetos", "sofá": "móvel para sentar e deitar", "cama": "móvel para dormir", "geladeira": "eletrodoméstico para conservar alimentos", "fogão": "eletrodoméstico para cozinhar alimentos", "microondas": "eletrodoméstico para aquecer alimentos",
            "liquidificador": "eletrodoméstico para triturar alimentos", "batedeira": "eletrodoméstico para bater massas", "torradeira": "eletrodoméstico para torrar pão", "chuveiro": "objeto para tomar banho", "banheira": "objeto para tomar banho de imersão", "pia": "objeto para lavar as mãos e objetos", "vaso sanitário": "objeto para fazer necessidades fisiológicas", "espelho": "objeto para refletir a imagem", "armário": "móvel para guardar objetos", "guarda-roupa": "móvel para guardar roupas"}

palavras_keys = list(palavras.keys())
palavras_length = len(palavras_keys)
rng = random.randint(0, palavras_length - 1)
palavra = palavras_keys[rng]
tentativas = 5


letras_digitadas = []

while True:
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print("-" * 24)
    print("Dica: " + palavras[palavra])
    print("Letras digitadas: " + str(letras_digitadas))

    print("-" * 24)
    print("Palavra: ")
    for letra in palavra:
        if letra in letras_digitadas:
            print(letra, end=" ")
        else:
            print("*", end=" ")
    print()

    print("Tentativas: %d" % tentativas)

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra in letras_digitadas:
        print("Você já digitou essa letra.")
        continue

    letras_digitadas.append(letra)

    if letra in palavra:
        print("A letra %s está na palavra." % letra)
        # if the user guessed all the letters
        win = True
        for letra in palavra:
            if letra not in letras_digitadas:
                win = False
                break
        if win:
            print("=" * 24)
            print("Você ganhou!")
            print("A palavra era: %s" % palavra)
            break
    else:
        print("A letra %s não está na palavra." % letra)
        tentativas -= 1
        if tentativas == 0:
            print("=" * 24)
            print("Você perdeu!")
            break
