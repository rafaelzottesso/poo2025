import tkinter as tk

# Cria a janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Calculadora")

# Define o tamanho da janela (largura x altura)
janela.geometry("400x600")


"""
Exemplo de rótulos (label)
"""

 # Cria um rótulo simples com texto
label1 = tk.Label(janela, text="Exemplo de rótulo")
label1.pack() # Adiciona o rótulo à janela

# Cria um rótulo com fonte personalizada
label2 = tk.Label(janela, text="Rótulo com fonte personalizada", font=("Arial", 16, "bold"))
label2.pack() # Adiciona o rótulo à janela

# Cria um rótulo com cor de fundo e texto
label3 = tk.Label(janela, text="Rótulo com cor de fundo", bg="lightblue", fg="darkblue")
label3.pack() # Adiciona o rótulo à janela

# Rótulo com cores exadecimal
label4 = tk.Label(janela, text="Rótulo com cores hexadecimal", bg="#ffffff", fg="#006400")
# Adiciona um espacamento no eixo y
label4.pack(pady=10)


"""
Exemplo de botões (button)
"""

# Widget button
botao1 = tk.Button(janela, text="Botão 1")
botao1.pack(pady=5)

def mensagem():
    print("Exemplo de mensagem ao clicar no botão")

# Botão com comando
botao2 = tk.Button(janela, text="Botão 2", command=mensagem)
botao2.pack(pady=5) # Adiciona o botão à janela

# Botão com formatação de cor e fonte
botao3 = tk.Button(janela, text="Botão 3", bg="lightgreen", fg="black", font=("Arial", 12))
botao3.pack(pady=5) # Adiciona o botão à janela

# Botão com altura e largura personalizadas
botao4 = tk.Button(janela, text="Botão 4", width=20, height=2)
botao4.pack(pady=5) # Adiciona o botão à janela


"""
Exemplo de entrada de texto por meio de campos (entry)
"""

# Campo de entrada de texto e largura definida
entrada1 = tk.Entry(janela, width=20)
entrada1.pack(pady=5) # Adiciona o campo de entrada à janela

# Campo de entrada com texto inicial
entrada2 = tk.Entry(janela, width=20)
entrada2.insert(0, "Texto inicial") # Insere texto inicial no campo
entrada2.pack(pady=5) # Adiciona o campo de entrada à janela

# Campo de entrada com fonte personalizada
entrada3 = tk.Entry(janela, width=20, font=("Arial", 14))
entrada3.pack(pady=5) # Adiciona o campo de entrada à janela

"""
Exemplo de manipulação de eventos com botões e campos de entrada
"""
def exibir_texto():
    texto = entrada3.get()  # Obtém o texto do campo de entrada
    print(f"Texto digitado: {texto}")  # Exibe o texto no console

botao5 = tk.Button(janela, text="Exibir Texto", command=exibir_texto)
botao5.pack(pady=5)  # Adiciona o botão à janela

# Exibe o texto em um rótulo ao clicar no botão
def exibir_em_rotulo():
    texto = entrada3.get()  # Obtém o texto do campo de entrada
    texto_atual = label4.cget("text")  # Obtém o texto atual do rótulo
    label4.config(text=f"{texto_atual} + {texto}")  # Atualiza o rótulo com o texto

botao6 = tk.Button(janela, text="Exibir em Rótulo", command=exibir_em_rotulo)
botao6.pack(pady=5)  # Adiciona o botão à janela


"""
Exemplo de caixas de diálogo (messagebox)
"""

# Criar um alerta simples (info, erro e warning)
from tkinter import messagebox
def alerta():
    messagebox.showinfo("Alerta", "Este é um alerta simples!")
    messagebox.showerror("Erro", "Este é um alerta de erro!")
    messagebox.showwarning("Aviso", "Este é um alerta de aviso!")

# Botão para exibir o alerta
botao_alerta = tk.Button(janela, text="Exibir Alerta", command=alerta)
botao_alerta.pack(pady=5)  # Adiciona o botão à janela

# askyesno()
def confirmar():
    resposta = messagebox.askyesno("Confirmação", "Você tem certeza?")
    if resposta:
        messagebox.showinfo("Confirmação", "Você confirmou!")
    else:
        messagebox.showwarning("Confirmação", "Você cancelou!")

botao_confirmar = tk.Button(janela, text="Confirmar", command=confirmar)
botao_confirmar.pack(pady=5)  # Adiciona o botão à janela


janela.mainloop() # Exibe a janela até ser fechada