entrada = input("Você quer 'entrar' ou 'sair'? ")

if entrada.lower() == "entrar":
    print("Bem vindo!")
elif entrada.lower() == "sair":
    print("Até logo!")
else:
    print("Você não digitou uma opção válida!")
