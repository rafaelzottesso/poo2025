from models import Animal, Gato

# esp = input("Espécie: ")
# voa = bool(input("Ele voa True/False: "))
# pernas = int(input("Qtde de pernas: "))
# cachorro = Animal(esp, voa, pernas)

cachorro = Animal("Vira lata", False, 4)
cachorro.apresentar()
print( cachorro.rugir() )


gato = Gato("Siamês", False, 4)
gato.apresentar()
print( gato.rugir() )