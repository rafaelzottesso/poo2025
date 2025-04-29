from classes import Estudante, TipoProtocolo, Protocolo
import os

while(True):
    os.system("cls")
    print("------------------------")
    print("---- Menu principal ----")
    print("------------------------")
    print("1. Estudante")
    print("2. Tipos de Protocolo")
    print("3. Protocolo")
    opc = int(input("Opção: "))
    print("------------------------\n")

    if(opc == 1):
        print("Menu de Estudantes")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        opc2 = int(input("Opção: "))        
        # Pula uma linha depois do input
        print("")

        if(opc2 == 1):
            print("Cadastrando um estudante...")
            nome_completo = input("Nome: ")
            ra = input("Matrícula: ")

            aluno = Estudante.create(nome=nome_completo, matricula=ra)            

            print(f"Estudante {aluno} cadastrado com sucesso!")

            # Só faz o input para ele não voltar automaticamente pra tela inicial e limpar com cls
            input("\n\nDigite ENTER para continuar...")

        if(opc2 == 2):

            # Selecionar todos os estudantes
            print("Estudantes cadastrados:")

            # Obter uma lista de objetos do BD
            lista = Estudante.select()
            print("\nTotal de estudantes:", len(lista), "\n")

            # Imprime na tela cada estudante
            for est in lista:
                print(f"ID: {est.id} - {est.nome} ({est.matricula})")

            # Só faz o input para ele não voltar automaticamente pra tela inicial e limpar com cls
            input("\n\nDigite ENTER para continuar...")


# print("Cadastrando Tipo de Protocolo")
# tipo = input("Tipo de protocolo: ")
# obj1 = TipoProtocolo.create(nome=tipo)

print("Tipos de protocolo cadastrados...")

# Listar e ordenar por nome
lista = TipoProtocolo.select()
lista = lista.order_by(TipoProtocolo.nome)

for tipo in lista:
    print(tipo.nome)
