r1 = float(input("primerio segmento "))
r2 = float(input("segundo segmento "))
r3 = float(input("terceiro segmento "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("então você pode formar um triangulo")
else:
    print("você não pode formar um triangulo caralho")