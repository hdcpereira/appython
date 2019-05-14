vel = int(input("qual a velocidade do carro? "))
t = vel - 80
if vel > 80:
    print("você está acima da velocidade, sua multa é R${:.2f} ".format(float(t*7)))
else:
    print("velocidade abaixo da limite")

