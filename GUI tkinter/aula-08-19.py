import tkinter as tk
from tkinter import messagebox

FONTE = ("Arial", 16)

def pegar_selecao():
    selecao = listbox.curselection()
    if selecao:  # se algum item estiver selecionado
        indice = selecao[0]     # Posição do item na Listbox
        texto = listbox.get(indice)  # Texto mostrado naquele item
        messagebox.showinfo("Aluno", f"Selecionado: {texto}")
        # Quebra uma string em uma lista
        # sempre que encontrar o caractere informado
        dados_aluno = texto.split('(')
        # substitui o caractere por outra coisa
        # Neste caso, troca ( por nada (vazio)
        id_aluno = dados_aluno[1].replace(')', '')
        messagebox.showinfo("ID do aluno", f"ID: {id_aluno}")
    else:
        print("Nenhum item selecionado")


janela = tk.Tk()

listbox = tk.Listbox(janela, width=30, height=10, font=FONTE)
listbox.pack()  # ou .grid(), dependendo do layout usado

# Suponha que tenha uma lista de produtos
produtos = ["Rafael (5)", "Lucas (123)", "Miguel (12)", "Lucas (45)"]

# Para inserir os itens na Listbox:
for produto in produtos:
    listbox.insert(tk.END, produto)

# Você pode chamar essa função por um botão:
botao = tk.Button(janela, text="Ver selecionado", command=pegar_selecao)
botao.pack()


janela.mainloop()
