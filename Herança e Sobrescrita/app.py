# Importa as classes criadas no arquivo models.py
from models import Animal, Borboleta, Gato, Teste

# Cria um objeto do tipo Animal
a1 = Animal()
# Define os atributos (características) do objeto criado
a1.especie = "Pássaro"
a1.voa = True
a1.pernas = 2
# Executa métodos do objeto criado
a1.apresentar()
a1.voar()
a1.morfar()
# Acessa atributos do objeto criado
print(f"A borboleta tem {a1.pernas} pernas")

print("\n\ncriando uma borboleta..")
# Cria um novo objeto, mas do tipo Borboleta e não Animal
b1 = Borboleta()
# Como Borboleta tem herança de Animal, tudo que tem 
# em animal agora também tem em Borboleta
# Assim, podemos definir os valores dos atributos
b1.especie = "borboleta"
b1.voa = True
b1.pernas = 6
# Executar os mesmos métodos
b1.apresentar()
b1.voar()
# Executa o morfar() que foi sobrescrito na classe Borboleta
b1.morfar()
# E acessar os mesmos atributos
print(f"A borboleta tem {b1.pernas} pernas")


# Cria um animal do tipo gato com dados fornecidos pelo usuário
esp = input("Espécie: ")
voa = bool(input("Voa (True/False): "))
pernas = int(input("Qtde de pernas: "))
# Cria o objeto
gato = Gato(esp, voa, pernas)
# Chama um método do objeto
print(gato.rugir())


# Cria um objeto do tipo teste
obj = Teste()
# Utiliza o método com parâmetros opcionais com 2 parâmetros só
obj.parametros_opcionais(10, 20)
# Método com quantos parâmetros desejar...
print(obj.parametros_infinitos(10,1,5,3,1))
# inclusive nenhum
print(obj.parametros_infinitos())
# Método com parâmetros nomeados
obj.parametros_infinitos_2(nome="Rafael", curso="INFO", disc="POO", alunos=32)
