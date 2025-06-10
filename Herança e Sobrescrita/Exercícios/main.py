# Importação das classes criadas
from models import Calculadora, CalculadoraCientifica, Conta

# Usuário digitando valores
marca = input("Marca : ")
modelo = input("Modelo: ")
ano = int(input("Ano : "))

# Criação de um objeto do tipo Calculadora com os dados fornecidos pelo usuário
c = Calculadora(marca, modelo, ano)

# Entrada de dados do usuário
x1 = int(input("Digite um numero: "))
x2 = int(input("Digite outro numero: "))

# Utilização dos métodos do objeto criado
resp = c.somar(x1, x2) 
resp2 = c.subtrair(x1, x2)
resp3 = c.multiplicar(x1, x2)
resp4 = c.dividir(x1, x2)
# Exibindo na tela o retorno dos métodos utilizados
print(f"{x1} + {x2} = {resp}")
print(f"{x1} - {x2} = {resp2}")
print(f"{x1} X {x2} = {resp3}")
print(f"{x1} : {x2} = {resp4}")

# Criação de outro objeto, porém do tipo CalculadoraCientifica
cf = CalculadoraCientifica(marca, "potência e raiz")

# Entrada de dados do usuário
x1 = int(input("Digite um número: " ))

# Utilização dos métodos do objeto criado e exibição dos retornos
resp = cf.potencia(x1,3)
print(f"{x1} ** 3 = {resp}")

# Utilização dos métodos do objeto criado e exibição dos retornos
resp = cf.raiz_quadrada(x1)
print(f"a raiz quadrada de {x1} é {resp}")


# Criação de um objeto do tipo conta, sem atributos obrigatórios no __init__
conta = Conta()

# Definindo os atributos "na mão", mas poderiam ser informados pelo usuário
conta.titular = "Felipe"
conta.numero = 12
conta.saldo = 21.0

# Utilizando os métodos e seus retornos

conta.depositar (500.0)

operacao_realizada = conta.sacar(1000.0)
if(operacao_realizada == True):
    print("Saque realizado")
else:
    print("Saldo indisponivel")

