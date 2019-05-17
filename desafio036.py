casa = int(input("qual o valor da casa? "))
sal = int(input("qual o seu salário? "))
temp = int(input("em quantos anos vc quer pagar a casa? "))
q = 0.30*sal
t = casa/(temp*12)
if q >= t:
    print("o seu emprestimo foi aprovado")
else:
    print("o seu emprestimo não foi aprovado")