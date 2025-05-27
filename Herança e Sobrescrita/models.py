# Criar uma classe chamada Animal
class Animal:
    
    # Fazer o método construtor e iniciar algumas variáveis (características)
    def __init__(self):
        self.especie = "A definir"
        self.voa = False
        self.pernas = 0

    # Criar um método (comportamento) que acessa uma variável com o valor 
    # definido após a criação dos objetos
    def apresentar(self):
        print(f"Eu sou um(a) {self.especie} ")
    
    # Outro exemplo de método 
    def voar(self):
        if (self.voa == True):
            print("Estou voando.")
        else:
            print("Eu não posso voar.")

    # Outro método
    def morfar(self):
        print("Você precisa fazer o animal morfar.")
        print("Sobrescreva o método nas classes filhas...")

# Criando uma classe Borboleta que herda tudo de animal
# Tanto atributos quanto métodos
class Borboleta(Animal):

    # Fazendo a sobrescrita de método, assim o método morfar vai funcionar
    # desse jeito e não do jeito que foi feito lá na classe Animal
    def morfar(self):
        print("Borboleta morfando")
        # O super() é usado para acessar métodos da classe pai.
        # Neste caso, além de sobrescrever o método morfar, estamos
        # executando o morfar() lá da classe animal
        super().morfar()
        print("Finalizando")