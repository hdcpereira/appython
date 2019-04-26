import math
catop =  float(input("digite o seu cateto oposto "))
catad = float(input("digite o seu cateto adjacente "))
hip = math.sqrt(pow(catop,2)+pow(catad,2))
print("se seu cateto oposto é {} e seu cateto adjacente é {}, então sua hipotenusa é {}".format(catop,catad,hip))