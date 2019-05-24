n1 = float(input("digite a nota da primeira prova "))
n2 = float(input("digite a nota da segunda prova "))

m = (n1+n2)/2

if m < 5.0:
    print("sua nota foi {} e você está REPROVADO".format(m))
elif 5.0 < m < 6.9:
    print("sua nota foi {} e você está de RECUPERAÇÃO".format(m))
elif m > 7.0:
    print("sua nota foi {} e você está APROVADO".format(m))