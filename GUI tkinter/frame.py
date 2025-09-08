import tkinter as tk
from tkinter import messagebox

def adicionar_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite algo!")

def exibir_selecionado():
    selecionados = listbox.curselection()
    if selecionados:
        item = listbox.get(selecionados[0])
        messagebox.showinfo("Selecionado", item)
    else:
        messagebox.showerror("Erro", "Selecione um item!")

# Janela principal
janela = tk.Tk()
janela.title("Exemplo de Listbox")
janela.geometry("350x330")

# Criando um frame para organizar o campo de texto e botão
frame_1 = tk.Frame(janela, bg="lightblue", padx=10, pady=10)
# O fill "x" faz o frame expandir horizontalmente
# Outras opções são "y" (vertical) e "both" (ambos)
frame_1.pack(fill="x")

# Adiciona um título centralizado ao frame
label_titulo1 = tk.Label(frame_1, text="Adicionar Itens à Lista", bg="lightblue", font=("Arial", 14))
label_titulo1.grid(row=0, column=0, columnspan=3, pady=5)

# Label para o campo de texto
label_item = tk.Label(frame_1, text="Adicionar Item:", bg="lightblue")
label_item.grid(row=1, column=0, padx=5, pady=5)
# Entry para adicionar no frame azul criado
entry = tk.Entry(frame_1, width=20)
entry.grid(row=1, column=1, padx=5, pady=5)
# Adicionar botão dentro do frame
btn_adicionar = tk.Button(frame_1, text="Adicionar", command=adicionar_item)
btn_adicionar.grid(row=1, column=2, padx=5, pady=5)

# Criar outro frame para o listbox e botão
frame_2 = tk.Frame(janela, bg="lightgreen", padx=10, pady=10)
# O fill "both" faz o frame expandir em ambas as direções
# e o expand=True permite que ele cresça para preencher o espaço disponível
frame_2.pack(fill="both", expand=True)

# Adiciona um título ao frame
label_titulo2 = tk.Label(frame_2, text="Lista de Itens", bg="lightgreen", font=("Arial", 14))
label_titulo2.pack()

# Listbox com seleção única
listbox = tk.Listbox(frame_2, height=8, width=25, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Botão para exibir selecionado
btn_exibir = tk.Button(frame_2, text="Exibir Selecionado", command=exibir_selecionado)
btn_exibir.pack(pady=5)

# Adiciona itens iniciais
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")

janela.mainloop()
