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
root = tk.Tk()
root.title("Exemplo de Listbox")
root.geometry("300x300")

# Entry e Botão para adicionar (como em aula2907.py)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

tk.Button(root, text="Adicionar", command=adicionar_item).pack(pady=5)

# Listbox com seleção única
listbox = tk.Listbox(root, height=8, width=25, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Botão para exibir selecionado
tk.Button(root, text="Exibir Selecionado", command=exibir_selecionado).pack(pady=5)

# Adiciona itens iniciais
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")

root.mainloop()
