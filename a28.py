"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {quantidade de letras} letras
        A primeira letra do seu nome é {primeira letra}
        A última letra do seu nome é {última letra}
Se nada for digitado em nomeou idade:
    Exiba uma mensagem de erro
"""

name = input('Digite seu nome: ')
safe_name = name.strip()
years = input('Digite sua idade: ')
safe_years = 0
# verify if years is a number
if years.isnumeric():
    safe_years = int(years)
else:
    print('Idade inválida')
    exit()

if safe_name == '' or safe_years == 0:
    print('Nome ou idade inválidos')
    exit()

print("-"*30)
print(f'Seu nome é {safe_name}')
print(f'Seu nome invertido é {safe_name[::-1]}')
print(f'Seu nome contém espaços? {"Sim" if " " in safe_name else "Não"}')
print(f'Seu nome tem {len(safe_name)} letras')
print(f'A primeira letra do seu nome é {safe_name[0]}')
print(f'A última letra do seu nome é {safe_name[-1]}')
