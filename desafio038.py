prim  = int(input("me diga um número "))
seg = int(input("me diga outro número "))
if prim > seg:
    print("{} é maior que {}".format(prim,seg))
elif seg > prim:
    print("{} é maior que {}".format(seg,prim))
elif seg == prim:
    print("{} é igual a {}".format(seg,prim))

