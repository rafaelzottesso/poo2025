# Criar uma classe chamada Animal
class Animal:
    
    # Fazer o método construtor e iniciar algumas variáveis (características)
    def __init__(self, p_especie, p_voa, p_pernas):
        self.especie = p_especie
        self.voa = p_voa
        self.pernas = p_pernas

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

    def rugir(self):
        return "Au au"

    # Outro método
    def morfar(self):
        print("Você precisa fazer o animal morfar.")
        print("Sobrescreva o método nas classes filhas...")

# Criando uma classe Borboleta que herda tudo de animal
# Tanto atributos quanto métodos
class Borboleta(Animal):

    # Fazendo a sobrescrita de método, assim o método morfar vai funcionar
    # desse jeito e não do jeito que foi feito lá na classe Animal (super classe de Borboleta)
    def morfar(self):
        print("Borboleta morfando...")
        # O super() é usado para acessar métodos da classe pai (Animal).
        # Neste caso, além de sobrescrever o método morfar, estamos executando o morfar() lá da classe animal
        # Assim, tudo que tem lá vai ser executado, além do que a gente incluir aqui no morfar()
        super().morfar()
        print("Finalizando")
        

# Cria uma nova classe com Herança para animal
class Gato(Animal):
    
    # Sobrescreve o método rugir
    def rugir(self):
        return "Miau"
    

# Cria uma nova classe de teste
class Teste:

    def __init__(self):
        pass

    """
    Possibilita utilizar parâmetros opcionais quando se da um
    valor padrão para eles. Exemplo:
    parametros_opcionais(10) -> a vale 10
    parametros_opcionais(10, 15) -> b vale 15
    parametros_opcionais(10, 15, 20) -> c vale 20
    """
    def parametros_opcionais(self, a, b=None, c=None):

        if(b):
            pass

        if(c):
            pass

    """
    Método que recebe quantos parâmetros forem necessários e serão tratados como uma lista (vetor)
    Pode ser nenhum ou 10, 20, 30, etc. Exemplo:
    parametros_infinitos()
    parametros_infinitos(9)
    parametros_infinitos(1, 5, 9, 10)
    """
    def parametros_infinitos(self, *numeros):
        soma = 0
        for n in numeros:
            soma = soma + n
        return soma
    
    """
    Possui parâmetros infinidos, porém devem ser nomeados e serão tratados como dicionários
    Um dicionário não tem índices, tem chave: {"nome" : "Rafael", "idade": 20}
    Exemplo de uso:
    parametros_infinitos_2(nome="Rafael")
    parametros_infinitos_2(nome="Rafael", idade=20, matricula="PVAI123")
    """
    def parametros_infinitos_2(self, **x):
        print("Coisas do dicionário:")
        for chave, valor in x.items():
            print(f"Chave - {chave}: {valor}")
    
