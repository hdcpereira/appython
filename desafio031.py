dist = float(input("qual a distância da sua viagem? "))
if dist <=200:
    print("então o preço da sua viagem será R${}".format(float(dist*0.50)))
else:
    print("então sua viagem custará R${}".format(float(dist*0.45)))