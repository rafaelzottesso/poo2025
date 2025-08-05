import tkinter as tk
from tkinter import messagebox

# Formatação pra reutilizar no programa
FONTE_PADRAO = ("Arial", 16)

# Variáveis com valor null (em Python é None)
valor1 = None
valor2 = None

def somar():
    # acessar valor1 e valor2 que estão no programa principal
    global valor1, valor2
    pass

def subtrair():
    pass

def multiplicar():
    pass

def dividir():
    pass

# Cria a janela com tamanho 500 x 500
janela = tk.Tk()
janela.geometry("305x500")

# Cria uma label para o resultado
lb_res = tk.Label(janela,text="4 + 5 =",font=FONTE_PADRAO, justify="right")
# Ela fica em 0,0, porém tem 4 colunas de largura (columnspan é igual mesclar células)
lb_res.grid(row=0,column=0,pady=5,padx=10, columnspan=4, sticky="e")

# Cria um campo para entrada de valores
e_num = tk.Entry(janela, width=23, font=FONTE_PADRAO, justify="right")
# Também ocupa uma linha e uma coluna, mas com 4 colunas de largura
e_num.grid(row=1,column=0, columnspan=4, pady=5,padx=10,sticky="ew")

# Cria o botão de +
btn_mais = tk.Button(janela, text="+", font=FONTE_PADRAO)
btn_mais.grid(row=2, column=0, pady=5,padx=5, sticky="we")

# Cria o botão de -
btn_menos = tk.Button(janela, text="-", font=FONTE_PADRAO)
btn_menos.grid(row=2, column=1, pady=5,padx=5, sticky="we")

# Cria o botão de *
btn_mais = tk.Button(janela, text="*", font=FONTE_PADRAO)
btn_mais.grid(row=2, column=2, pady=5,padx=5, sticky="we")

# Cria o botão de ÷
btn_menos = tk.Button(janela, text="÷", font=FONTE_PADRAO)
btn_menos.grid(row=2, column=3, pady=5,padx=5, sticky="we")

# Executa o programa e cria a janela
janela.mainloop()