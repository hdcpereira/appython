import math
alpha = float(input('digite um angulo '))

alphacos = math.cos(math.radians(alpha))
alphasin = math.sin(math.radians(alpha))
alphatan = math.tan(math.radians(alpha))
print('se seu angulo é {} então seu cosseno é {:.2f} seu seno é {:.2f} e sua tangente {:.2f}'.format(alpha, alphacos, alphasin, alphatan))