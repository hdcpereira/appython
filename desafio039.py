from datetime import date
yy1 = date.today().year
yy2 = int(input("digite o ano do seu nascimento "))

yy = yy1-yy2
yyy = 18 - yy
yyyy = yy -18
if yy == 18:
    print("você deve se alista agora, vc já tem 18 anos")
elif yy < 18:
    print("faltam {} anos pra vc se alistar".format(yyy))
elif yy >18:
    print("já passaram {} anos do seu alistamento".format(yyyy))

