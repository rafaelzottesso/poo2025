import math

# Criação da classe calculadora
class Calculadora:

    # Método construtor com os atributos obrigatórios
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Métodos com parâmetros obrigatórios (a,b) e opcionais (c)
    def somar(self, a, b, c=0):
        return a + b + c
    
    # Métodos com parâmetros obrigatórios (a,b) e opcionais (c)
    def subtrair(self, a, b, c=0):
        return a - b - c
    
    # Métodos com parâmetros obrigatórios (a,b) e opcionais (c)
    def multiplicar(self, a, b, c=1):
        return a * b * c

    # Métodos com parâmetros obrigatórios (a,b)
    def dividir(self,a, b):
        if (b == 0):
            print("Impossível dividir por zero.")
            return 0
        
        return a / b
    
# Criação de classe com Herança para Calculadora 
class CalculadoraCientifica(Calculadora):
    
    # Construtor diferente para essa classe
    def __init__(self,marca,funcoes_cientificas):
        self.marca = marca
        self.fc = funcoes_cientificas
        self.modelo = ""
        self.ano = 0

    def  potencia(self, base, expoente):
        return base ** expoente

    def  raiz_quadrada(self, numero):
        return math.sqrt(numero)
    

# Criação de classe
class Conta:

    # Construtor que não obriga definir os atributos na hora de criação dos objetos
    def __init__(self):
        self.numero = 0
        self.titular = ""
        self.saldo = 0.0
        self.limite = 400.0

    # Criação de método especificando o tipo do parâmetro valor para float
    def depositar(self,valor:float):
        self.saldo += valor
        print(f"Valor R${valor} depositado. Saldo atual: R${self.saldo}") 

    # Criação de método especificando o tipo do parâmetro valor para float e o retorno para bool
    # Em java seria: public boolean sacar(double valor){...}
    def sacar(self, valor:float) -> bool:
        if(self.saldo + self.limite > valor):
            self.saldo -= valor
            print(f"Valor R${valor} Sacado. Saldo atual: R${self.saldo}")
            return True
        else:
            return False

    # Método sem parâmetro e com retorno float
    def consultarSaldo(self) -> float:
        return  self.saldo   
    
    # Método sem parâmetro e com retorno str
    def __str__(self) -> str: 
        return f"Titular: {self.titular} ({self.numero})" 
        
         
    
