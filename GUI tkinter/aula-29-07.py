import tkinter as tk
from tkinter import messagebox

# Definir duas constantes com uma formatação padrão pra poder reutilizar no programa
FONTE_PADRAO = ("Arial", 20)
FONTE_NEGRITO = ("Arial", 20, "bold")

# Site com a roda de cores em hexadecimal
# https://www.canva.com/colors/color-wheel/
COR_VERDE = "#06600e"


# Função para executar ao clicar em um botão
def printar():
    # Busca o texto preenchido no campo nome (Entry nome)
    nome = e_nome.get()

    # Tenta converter o valor do campo idade para inteiro
    try:
        idade = e_idade.get()
        idade = int(idade)
    # Se der erro, exibe um alerta e sai da função (retorna sem nada)
    except:
        messagebox.showerror("Erro", "Idade inválida")
        return

    # Se o comprimento do nome for maior que zero, o usuário digitou alguma coisa
    if(len(nome) > 0):

        # Exibe uma mensagem em uma caixa com título e mensagem
        messagebox.showinfo("Ola",f"Bem vindo {nome}")
        
        # Altera o texto de um rótulo
        l_resultado.config(text=f"Você tem {idade} anos")

    else:
        # Exibe uma caixa de erro com título e mensagem
        messagebox.showerror("Atenção", "Informe seu nome")
    
# Cria a janela com tamanho 500 x 500
janela = tk.Tk()
janela.geometry("500x500")

# Cria um rótulo
l_nome = tk.Label(janela,text="Nome:",font=FONTE_NEGRITO)
l_nome.pack(pady=5)

# Cria um campo de entrada de dados
e_nome = tk.Entry(janela, width=20, font=FONTE_PADRAO)
e_nome.pack(pady=5)

# Cria um rótulo
l_idade = tk.Label(janela,text="Idade: ", font=FONTE_NEGRITO, fg=COR_VERDE,bg="#ffffff")
l_idade.pack(pady=5)

# Cria um campo de entrada de dados
e_idade = tk.Entry(janela,width=20, font=FONTE_PADRAO)
e_idade.pack(pady=5)

# Cria um botão que ao clicar executa a função "printar"
b_ola = tk.Button(janela,text="Ola", font=FONTE_PADRAO, width=20, command=printar)
b_ola.pack(pady=5)

# Cria um rótulo vazio para ter seu texto preenchido lá na função "printar"
l_resultado = tk.Label(janela,text="", font=FONTE_NEGRITO,fg="#06600e")
l_resultado.pack(pady=5)

# Executa o programa e cria a janela
janela.mainloop()