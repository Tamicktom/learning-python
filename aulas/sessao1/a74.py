"""
Closure e funções que retornam funções
"""


def criar_saudacao(saudacao: str, nome: str):
    def saudar():
        return f'{saudacao} {nome}'
    return saudar


ola = criar_saudacao('Olá', 'João')
print(ola())
