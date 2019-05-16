from datetime import date
n = int(input("digite o um ano qualquer, digite zero para olhar para o ano atual "))
if n == 0:
    n = date.today().year
if n%4==0 and n % 100 != 0 or n % 400 == 0:
    print("o ano {} é bissexto".format(n))
else:
    print("o ano {} não é bissexto".format(n))