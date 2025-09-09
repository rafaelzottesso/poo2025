import tkinter as tk
from tkinter import messagebox

# Janela principal
janela = tk.Tk()
janela.title("Programa completo com Frame e Menu")
janela.geometry("400x400")

def exibir_frame1():
    frame_2.pack_forget()
    frame_1.pack(fill="both", expand=True)
    frame_1.tkraise()

def exibir_frame2():
    frame_1.pack_forget()
    frame_2.pack(fill="both", expand=True)
    frame_2.tkraise()


# Criar uma barra de menu principal
menubar = tk.Menu(janela, font=("Arial", 16))

# Criar o submenu "Arquivo"
menu_arquivo = tk.Menu(menubar, tearoff=False)  # tearoff=False remove linha pontilhada
# add_command adiciona itens ao menu com um rótulo e uma ação (command igual a um botão)
menu_arquivo.add_command(label="Cadastrar item", command=exibir_frame1)
menu_arquivo.add_command(label="Listar itens", command=exibir_frame2)
# Adiciona uma linha separadora entre os itens do menu
menu_arquivo.add_separator()
# submenu Sair que fecha a janela principal
menu_arquivo.add_command(label="Sair", command=janela.quit)

# Adiciona o submenu "Cadastros" à barra de menu principal
menubar.add_cascade(label="Cadastros", menu=menu_arquivo)


# Criar o submenu "Ajuda"
menu_ajuda = tk.Menu(menubar, tearoff=False)
menu_ajuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Tkinter Rocks!"))
# Adiciona o submenu "Ajuda" à barra de menu principal (ao lado direito)
menubar.add_cascade(label="Ajuda", menu=menu_ajuda)

# Configura a janela principal para usar a barra de menu criada
janela.config(menu=menubar)


# Criando um frame para organizar o campo de texto e botão
frame_1 = tk.Frame(janela, bg="lightblue", padx=10, pady=10)

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
btn_adicionar = tk.Button(frame_1, text="Adicionar", command=lambda: print("Adicionar item"))
btn_adicionar.grid(row=1, column=2, padx=5, pady=5)

# Criar outro frame para o listbox e botão
frame_2 = tk.Frame(janela, bg="lightgreen", padx=10, pady=10)

# Adiciona um título ao frame
label_titulo2 = tk.Label(frame_2, text="Lista de Itens", bg="lightgreen", font=("Arial", 14))
label_titulo2.pack()

# Listbox com seleção única
listbox = tk.Listbox(frame_2, height=8, width=25, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Botão para exibir selecionado
btn_exibir = tk.Button(frame_2, text="Exibir Selecionado", command=lambda: print("Exibir selecionado"))
btn_exibir.pack(pady=5)



janela.mainloop()
