city = str(input("qual o nome da sua cidade? "))

q = city.upper()
if(q[:5]=="SANTO"):
    print("sua cidade começa com Santo.")
else:
    print("sua cidade não começa com Santo.")