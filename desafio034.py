sal = float(input("me diga seu salário que eu calcularei seu aumento "))

if sal<1250.00:
    print("então seu aumento será de 10% e seu salário será {}".format(sal*1.10))
if sal>=1250.00:
    print("então seu aumento será de 15% e seu salário será {}".format(sal*1.15))
