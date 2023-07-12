a: str = "A"
b: str = "B"
c: float = 1.1123123
formato: str = "a={} b={} c={}".format(a, b, c)
formato2: str = "a={2:.2f} b={0} c={1}".format(a, b, c)

formato3: str = "a={nome3:.2f} b={0} c={1}"

print(formato)
print(formato2)
print(formato3.format(1, 2, nome3=3.1415))
