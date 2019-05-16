x1 = int(input("digite o primeiro número "))
x2 = int(input("digite o segundo número "))
x3 = int(input("digite o terceiro número "))
#procurando o maior valor
maior = x1
if x2 > x1 and x2 > x3:
    maior = x2
if x3 > x1 and x3 > x2:
    maior = x3
#procurando o menor valor
menor  = x3
if x2 < x1 and x2 < x3:
    menor = x2
if x1 < x2 and x1 < x3:
    menor = x1
print("o seu maior número é {} e seu menor número é {}".format(maior, menor))
