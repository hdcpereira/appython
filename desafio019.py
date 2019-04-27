import random
a1 = str(input("quem é o primeiro aluno? "))
a2 = str(input("quem é o segundo aluno? "))
a3 = str(input("quem é o terceiro aluno? "))
a4 = str(input("quem é o quarto aluno? "))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print("o aluno escolhido foi {}".format(escolhido))
