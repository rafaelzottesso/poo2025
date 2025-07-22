import datetime
print("Tratamento de exceções")

try:
    x = int(input("digite um numero inteiro: "))
    r = 10/x
except ZeroDivisionError as erro: 
    with open("Log.txt", "a") as arquivo:
        data = datetime.datetime.now()
        arquivo.write(f"{data} - {erro}\n")
        arquivo.close()
except ValueError as erro:
    with open("Log.txt", "a") as arquivo:
        data = datetime.datetime.now()
        arquivo.write(f"{data} - {erro}\n")
        arquivo.close()

#print(f"O dobro de {x} é: {x * 2}")