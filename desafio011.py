h = float(input("qual a altura da sua parede? "))
l = float(input("qual a largura da sua parede? "))
a = h*l
t = a*(1/2)
print("se a altura da sua parede é {} e sua largura é {}, sua área é {}m2 \n "
      "e a quantidade de tinta que você vai precisar é {} litros.".format(h, l, a, t))
