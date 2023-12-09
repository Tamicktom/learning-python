primeio_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

maior: bool = primeio_valor > segundo_valor

if maior:
    print(f"O maior valor é {primeio_valor}")
else:
    print(f"O maior valor é {segundo_valor}")
