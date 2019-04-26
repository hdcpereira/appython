h = int(input("qual a altura da sua parede? "))
l = int(input("qual a largura da sua parede? "))
a = h*l
t = a*(1/2)
print("se a altura da sua parede é {} e sua largura é {}, sua área é {} \n "
      "e a quantidade de tinta que você vai precisar é {} litros.".format(h, l, a, t))
