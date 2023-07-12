a: str = "A"
b: str = "B"
c: float = 1.1123123
formato: str = "a={} b={} c={}".format(a, b, c)
formato2: str = "a={2:.2f} b={0} c={1}".format(a, b, c)

formato3: str = "a={nome1} b={nome2} c={nome3}"

print(formato)
print(formato2)
print(formato3.format(nome1=a, nome2=b, nome3=c.__round__(2)))
