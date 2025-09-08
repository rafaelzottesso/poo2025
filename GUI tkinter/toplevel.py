import tkinter as tk
from tkinter import messagebox

# Janela principal com tamanho e título
janela = tk.Tk()
janela.title("Menu bar exemplo")
janela.geometry("300x200")

# Criar uma barra de menu principal
menubar = tk.Menu(janela, font=("Arial", 16))

# Criar o submenu "Arquivo"
menu_arquivo = tk.Menu(menubar, tearoff=False)  # tearoff=False remove linha pontilhada
# add_command adiciona itens ao menu com um rótulo e uma ação (command igual a um botão)
menu_arquivo.add_command(label="Novo", command=lambda: print("Novo arquivo"))
menu_arquivo.add_command(label="Abrir…", command=lambda: print("Abrir arquivo"))
# Adiciona uma linha separadora entre os itens do menu
menu_arquivo.add_separator()
# submenu Sair que fecha a janela principal
menu_arquivo.add_command(label="Sair", command=janela.quit)

# Adiciona o submenu "Arquivo" à barra de menu principal
menubar.add_cascade(label="Arquivo", menu=menu_arquivo)


# Criar o submenu "Ajuda"
menu_ajuda = tk.Menu(menubar, tearoff=False)
menu_ajuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Tkinter Rocks!"))
# Adiciona o submenu "Ajuda" à barra de menu principal (ao lado direito)
menubar.add_cascade(label="Ajuda", menu=menu_ajuda)

# Configura a janela principal para usar a barra de menu criada
janela.config(menu=menubar)


janela.mainloop()
