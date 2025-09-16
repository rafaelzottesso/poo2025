import tkinter as tk
from tkinter import messagebox
# Importar as suas classes do peewee aqui
# from classes import X, Y, Z

# Formatação de fonte padrão para usar nos elementos da tela
FONT_TITULO=("Arial",18)
FONT_TEXTO=("Arial",13)


################################################################
############ Funções de navegação da barra de menu #############
################################################################

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

# Função que mostra o frame da tela da classe X
def mostrar_tela_x():
    frame_x.tkraise()

# Função que mostra o frame da tela da classe Y
def mostrar_tela_y():
    frame_y.tkraise()

# Função que mostra o frame da tela da classe Z
def mostrar_tela_z():
    frame_z.tkraise()


##############################################################
################# Frame da janela principal ##################
##############################################################

# Janela principal com tamanho e título
janela = tk.Tk()
janela.title("Menu bar exemplo")
# Configurar o tamanho de acordo com o conteúdo das suas telas
janela.geometry("600x600")


#############################################################
################# Criação da barra de menu ##################
#############################################################

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
# Os submenus vão ser suas classes do peewee
menu_cadastro=tk.Menu(menubar,tearoff=False)
menu_cadastro.add_command(label="X",command=mostrar_tela_x)
menu_cadastro.add_command(label="Y",command=mostrar_tela_y)
menu_cadastro.add_separator()
menu_cadastro.add_command(label="Z",command=mostrar_tela_z)
menubar.add_cascade(label="Cadastro",menu=menu_cadastro)

# Cria um outro menu com submenus
# Para apresentar sobre vocês e sobre o Software
menu_sobre = tk.Menu(menubar, tearoff=False)
menu_sobre.add_command(label="Sobre Nós", command=sobre)
menu_sobre.add_separator()
menu_sobre.add_command(label="Versão", command=lambda:messagebox.showinfo("Versão Atual", "Versão 1.0"))
menubar.add_cascade(label="Sobre", menu=menu_sobre)


##########################################################
################# Frame da tela inicial ##################
##########################################################

# Criação dos frames que serão mostrados na tela
# Um frame pode acoplar diversos elementos dentro dele
# Em vez de adicionar tudo na janela, separamos os conteúdos por frames
frame_inicio=tk.Frame(janela)
# Adicionamos um label nesse frame
lb_ola=tk.Label(frame_inicio, text="Bem-vindo ao sistema", font=FONT_TITULO)
lb_ola.pack(pady=30)


###################################################
################# Tela sobre nós ##################
###################################################

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

#######################################################
################# Tela para classe X ##################
#######################################################

frame_x = tk.Frame(janela)
lb_x = tk.Label(frame_x, text="Bem-vindo à tela da classe X", font=FONT_TITULO)
lb_x.pack(pady=30)

# Adicionar suas funções, labels, entry, button e listbox

#######################################################
################# Tela para classe Y ##################
#######################################################

frame_y = tk.Frame(janela)
lb_y = tk.Label(frame_y, text="Bem-vindo à tela da classe Y", font=FONT_TITULO)
lb_y.pack(pady=30)

# Adicionar suas funções, labels, entry, button e listbox

#######################################################
################# Tela para classe Z ##################
#######################################################

frame_z = tk.Frame(janela)
lb_z = tk.Label(frame_z, text="Bem-vindo à tela da classe Z", font=FONT_TITULO)
lb_z.pack(pady=30)

# Adicionar suas funções, labels, entry, button e listbox

###########################################################
################# Organização dos frames ##################
###########################################################

# Coloca os frames na janela principal
# Esses frames ficam todos sobrepostos na mesma posição
# porque o tkraise irá escolher quem será exibido a cada vez
# Todos ficam na mesma linha, coluna e com mesmo estilo de fixação
frame_inicio.grid(row=0,column=0,sticky="nesw")
frame_sobre.grid(row=0,column=0,sticky="nesw")
frame_x.grid(row=0,column=0,sticky="nesw")
frame_y.grid(row=0,column=0,sticky="nesw")
frame_z.grid(row=0,column=0,sticky="nesw")

# Define qual frame vai aparecer ao iniciar o programa principal
frame_inicio.tkraise()


###############################################################
########### Config da janela e "start" no programa ############
###############################################################

# Adiciona a barra de menu na janela principal do programa
janela.config(menu=menubar)

# Executa o programa na janela principal
janela.mainloop()