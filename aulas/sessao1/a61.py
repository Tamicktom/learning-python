

"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10.

Ex.: 746.824.890-70 (74682489070)
    10  9  8   7   6   5   4   3   2
*   7  4  6   8   2   4   8   9   0
    70 36 48  56  12  20  32  27  0
    
Somar todos os resultados:
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301
Multiplicar o resultado anteror por 10
301 * 10 = 3010
Obter o resto da divisão por 11
3010 % 11 = 7

Se o resultado anterior fr maior que 9:
    resultado é 0
contrário disso:
    resultado é o próprio valor
"""

cpfsValidos: list[str] = ["746.824.890-70",
                          "274.485.890-08",
                          "828.430.030-32",
                          "973.454.610-41",
                          "099.627.570-37",
                          "640.361.580-74",
                          "144.885.150-53"]

cpfsInvalidos: list[str] = ["111.111.111-11",
                            "222.222.222-22",
                            "333.333.333-33",
                            "444.444.444-44",
                            "555.555.555-55",
                            "666.666.666-66",
                            "777.777.777-77",
                            "888.888.888-88",
                            "999.999.999-99",
                            "000.000.000-00",
                            "123.456.789-10",
                            "321.123.456-00"]


def clearCPF(dirtyCPF: str):
    return dirtyCPF.replace(".", "").replace("-", "")


def sun9first(clearCPF: str):
    sun = 0
    for i in range(9):
        sun += int(clearCPF[i]) * (10 - i)
    return sun


def verifyIfDigitsAreEqual(clearCPF: str):
    first = clearCPF[0]
    for i in range(1, 11):
        if clearCPF[i] != first:
            return False
    return True


def validateCPFs(cpfs: list[str]) -> list[bool]:
    results: list[bool] = []
    for cpf in cpfs:
        clear = clearCPF(cpf)
        if verifyIfDigitsAreEqual(clear):
            results.append(False)
            continue
        sun = sun9first(clear)
        rest = 0 if sun * 10 % 11 > 9 else sun * 10 % 11
        results.append(rest == int(clear[9]))
    return results


print(validateCPFs(cpfsValidos))
print(validateCPFs(cpfsInvalidos))
