import tkinter as tk
from tkinter import messagebox

def exibir_dados():
    # Obtem o texto digitado no campo nome
    nome = entry_nome.get()
    # Verifica se o campo nome está vazio
    if(not nome):
        messagebox.showerror("Erro", "Por favor, preencha o nome.")
        return

    # Obtem o texto digitado no campo idade
    idade = entry_idade.get()
    # Verifica se o campo idade é um número
    if not idade.isdigit():
        messagebox.showerror("Erro", "Idade deve ser um número.")
        return
    
    # Exibe os dados em uma caixa de mensagem
    messagebox.showinfo("Dados", f"Nome: {nome}\nIdade: {idade}")


# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)


# Janela principal
janela = tk.Tk()
janela.title("Formulário com Grid")
janela.geometry("300x200")

# Cria uma label para o Nome
lb_nome = tk.Label(janela, text="Nome:")
# Posiciona a label na grade na posição (0, 0)
lb_nome.grid(row=0, column=0, sticky="w", padx=10, pady=5)

# Cria um campo de entrada para o Nome
entry_nome = tk.Entry(janela, width=20)
# Posiciona o campo de entrada na grade na posição (0, 1)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

# Cria labels e campos de entrada para Idade e posiciona na grade
lb_idade = tk.Label(janela, text="Idade:")
lb_idade.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_idade = tk.Entry(janela, width=20)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

# Cria um botão que chama a função exibir_dados ao ser clicado
btn_exibir = tk.Button(janela, text="Exibir", width=10, command=exibir_dados)
btn_exibir.grid(row=2, column=0, columnspan=2, pady=10)

# Cria um botão para limpar os campos
btn_limpar = tk.Button(janela, text="Limpar", width=10, command=limpar_campos)
btn_limpar.grid(row=3, column=0, columnspan=2, pady=0)

janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=2)


janela.mainloop()
