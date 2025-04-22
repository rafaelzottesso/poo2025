from classes import Estudante, TipoProtocolo

print("Cadastrando Tipo de Protocolo")

tipo = input("Tipo de protocolo: ")
obj1 = TipoProtocolo.create(nome=tipo)

print("Tipos de protocolo cadastrados...")

# Listar e ordenar por nome
lista = TipoProtocolo.select()
lista = lista.order_by(TipoProtocolo.nome)

for tipo in lista:
    print(tipo.nome)

print("Cadastrando um estudante...")
nome_completo = input("Nome: ")
ra = input("Matrícula: ")

est1 = Estudante.create(nome=nome_completo, matricula=ra)


# Selecionar todos os estudantes
print("\n\n")
print("----- Estudantes cadastrados -----")

# Obter uma lista de objetos do BD
lista = Estudante.select()
print("\nTotal de estudantes:", len(lista), "\n")

# Imprime na tela cada estudante
for objeto in lista:
    print(f"Nome: {objeto.nome} ({objeto.matricula})")

