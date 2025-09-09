import tkinter as tk
from tkinter import messagebox

# Formatação de fonte padrão para usar nos elementos da tela
FONT_TITULO=("Arial",18)
FONT_TEXTO=("Arial",13)

# Função de exemplo para o menu
def clicar():
    print("menu clicar")
    messagebox.showinfo("Info", "Essa é a mensagem")

# Função que mostra o frame da tela inicial
def inicio():
    # seu_frame.tkraise() exibe seu frame na frente dos outros
    frame_inicio.tkraise()

# Função que mostra o frame da tela sobre
def sobre():
    # seu_frame.tkraise() exibe seu frame na frente dos outros
    frame_sobre.tkraise()

# Janela principal com tamanho e título
janela = tk.Tk()
janela.title("Menu bar exemplo")
janela.geometry("600x600")

# Criação da barra principal de menu
menubar=tk.Menu(janela)

# Criação de um menu para a barra de menu
menu_arquivo=tk.Menu(menubar,tearoff=False)
# Adiciona opções nesse menu
menu_arquivo.add_command(label="Início",command=inicio)
# Adiciona uma linha separadora
menu_arquivo.add_separator()
# Adiciona a opção sair que fecha a janela principal
menu_arquivo.add_command(label="Sair",command=janela.quit)
# Coloca esse submenu na barra de menu "Arquivo"
menubar.add_cascade(label="Arquivo",menu=menu_arquivo)

# Cria um novo menu com submenus
menu_cadastro=tk.Menu(menubar,tearoff=False)
menu_cadastro.add_command(label="Estudante",command=clicar)
menu_cadastro.add_command(label="Tipo de protocolo",command=clicar)
menu_cadastro.add_separator()
menu_cadastro.add_command(label="Protocolo",command=clicar)
menubar.add_cascade(label="Cadastro",menu=menu_cadastro)

# Cria um outro menu com submenus
menu_sobre = tk.Menu(menubar, tearoff=False)
menu_sobre.add_command(label="Sobre Nós", command=sobre)
menu_sobre.add_separator()
menu_sobre.add_command(label="Versão", command=lambda:messagebox.showinfo("Versão Atual", "Versão 1.0"))
menubar.add_cascade(label="Sobre", menu=menu_sobre)

# Criação dos frames que serão mostrados na tela
# Um frame pode acoplar diversos elementos dentro dele
# Em vez de adicionar tudo na janela, separamos os conteúdos por frames
frame_inicio=tk.Frame(janela)
# Adicionamos um label nesse frame
lb_ola=tk.Label(frame_inicio, text="Bem-vindo ao sistema", font=FONT_TITULO)
lb_ola.pack(pady=30)

# Criação de outro frame para representar outra tela no sistema
frame_sobre=tk.Frame(janela)
lb_alunos=tk.Label(frame_sobre,text="Desenvolvido por:",font=FONT_TITULO)
lb_alunos.pack(pady=20)
# Cria um bloco de strings
equipe="""
Felipe
Vitor
Rafael
"""
# Adiciona essa string em um label no frame sobre
lb_equipe=tk.Label(frame_sobre,text=equipe,font=FONT_TEXTO)
lb_equipe.pack(pady=10)

# Coloca os frames na janela principal
# Esses frames ficam todos sobrepostos na mesma posição
# porque o tkraise irá escolher quem será exibido a cada vez
# Todos ficam na mesma linha, coluna e com mesmo estilo de fixação
frame_inicio.grid(row=0,column=0,sticky="nesw")
frame_sobre.grid(row=0,column=0,sticky="nesw")

# Define qual frame vai aparecer ao iniciar o programa principal
frame_inicio.tkraise()

# Adiciona a barra de menu na janela principal do programa
janela.config(menu=menubar)

# Executa o programa na janela principal
janela.mainloop()