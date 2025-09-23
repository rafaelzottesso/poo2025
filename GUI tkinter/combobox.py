import tkinter as tk
from tkinter import messagebox, ttk
# Importa as classes do Peewee
from classes import Estudante, TipoProtocolo, Protocolo

# Método para salvar no banco de dados
def salvar_protocolo():
    try:
        # Pega o estudante selecionado no combobox
        estudante_selecionado = combobox_estudante.get() # get pega o texto e .current() a posição
        estudante_id = int(estudante_selecionado.split('(')[-1].strip(')'))
        estudante = Estudante.get_by_id(estudante_id)

        # Pega o tipo de protocolo selecionado no combobox
        tipo_selecionado = combobox_tipo.get() # get pega o texto e .current() a posição
        tipo_id = int(tipo_selecionado.split('(')[-1].strip(')'))
        tipo = TipoProtocolo.get_by_id(tipo_id)

        # Pega a justificativa do entry
        justificativa = entry_justificativa.get()

        # Cria um novo protocolo e salva no banco de dados
        novo_protocolo = Protocolo.create(
            estudante=estudante,
            tipo=tipo,
            justificativa=justificativa
        )
        messagebox.showinfo("Sucesso", f"Protocolo {novo_protocolo.id} salvo com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar protocolo: {e}")


# Botão para selecionar o estudante com ID 2 no combobox
def selecionar_estudante_id_2():
    # Faz um loop na lista de estudantes para encontrar o que tem ID 2
    for i in range(0, len(estudantes)):
        if estudantes[i].endswith("(2)"):
            combobox_estudante.current(i)
            break   

    # Faz um loop na lista de tipos de protocolo para encontrar o que tem ID 2
    for i in range(0, len(tipos_protocolo)):
        if tipos_protocolo[i].endswith("(2)"):
            combobox_tipo.current(i)
            break


# Cria a janela principal com título e tamanho
janela = tk.Tk()
janela.title("Exemplo de Combobox")
janela.geometry("450x300")

# Criar um label para estudante
label_estudante = tk.Label(janela, text="Estudante:")
label_estudante.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Criar um combobox para selecionar o estudante
# Já lista todos os estudantes cadastrados no banco de dados e transforma em uma lista de strings
# Que é o que o combobox espera
# lista_estudantes = ["Rafael - 3", "Maria - 1", "José - 2"]
# lista = Estudante.select()
# lista_estudantes = []
# for estudante in lista:
#     str_estudante = f"{estudante.nome} - {estudante.id}"
#     lista_estudantes.append(str_estudante)

estudantes = [f"{est.nome} ({est.id})" for est in Estudante.select()]
combobox_estudante = ttk.Combobox(janela, values=estudantes)
combobox_estudante.grid(row=0, column=1, padx=10, pady=10, sticky="we")

# Criar um label para tipo de protocolo
label_tipo = tk.Label(janela, text="Tipo de Protocolo:")
label_tipo.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Criar um combobox para selecionar o tipo de protocolo
tipos_protocolo = [f"{tipo.nome} ({tipo.id})" for tipo in TipoProtocolo.select()]
combobox_tipo = ttk.Combobox(janela, values=tipos_protocolo)
combobox_tipo.grid(row=1, column=1, padx=10, pady=10, sticky="we")

# Label para justificativa
label_justificativa = tk.Label(janela, text="Justificativa:")
label_justificativa.grid(row=2, column=0, padx=10, pady=10, sticky="e")

# Entry para a justificativa
entry_justificativa = tk.Entry(janela, width=25)
entry_justificativa.grid(row=2, column=1, padx=10, pady=10)


# Botões para "salvar"
button_salvar = tk.Button(janela, text="Salvar", command=salvar_protocolo)
button_salvar.grid(row=3, column=0, pady=20)

# Botão para selecionar o estudante com ID 2
button_selecionar_id_2 = tk.Button(janela, text="Estudante ID 2", command=selecionar_estudante_id_2)
button_selecionar_id_2.grid(row=3, column=1, pady=10)

# Roda a janela
janela.mainloop()