with open("Log.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        print(linha, end="")
    arquivo.close()
