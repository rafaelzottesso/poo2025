import sys
import os
from classes import Estudante
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

# Função que mostra o frame de cadastro de estudantes
def cad_estudante():
    # Inicializa a lista ao abrir a tela
    listar_estudantes()
    # Abre a tela de estudantes
    frame_cad_estudante.tkraise()

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
menu_cadastro.add_command(label="Estudante",command=cad_estudante)
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

# Frame de cadastro de estudantes
frame_cad_estudante = tk.Frame(janela, padx=20, pady=10)

# Título
lb_titulo = tk.Label(frame_cad_estudante, text="Cadastro de Estudantes", font=FONT_TITULO)
lb_titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Nome
lb_nome = tk.Label(frame_cad_estudante, text="Nome:", font=FONT_TEXTO)
lb_nome.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_nome = tk.Entry(frame_cad_estudante, width=30)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

# Matrícula
lb_matricula = tk.Label(frame_cad_estudante, text="Matrícula:", font=FONT_TEXTO)
lb_matricula.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_matricula = tk.Entry(frame_cad_estudante, width=30)
entry_matricula.grid(row=2, column=1, padx=5, pady=5)

# Curso
lb_curso = tk.Label(frame_cad_estudante, text="Curso:", font=FONT_TEXTO)
lb_curso.grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_curso = tk.Entry(frame_cad_estudante, width=30)
entry_curso.grid(row=3, column=1, padx=5, pady=5)

# Listbox para exibir estudantes
listbox_estudantes = tk.Listbox(frame_cad_estudante, width=50, height=8)
listbox_estudantes.grid(row=4, column=0, columnspan=2, pady=10)

# Funções para manipular estudantes (inserir, editar, excluir, listar)
def listar_estudantes():
    listbox_estudantes.delete(0, tk.END)
    for estudante in Estudante.select():
        listbox_estudantes.insert(tk.END, f"{estudante.id} - {estudante.nome} - {estudante.matricula} - {estudante.curso}")

def cadastrar_estudante():
    nome = entry_nome.get().strip()
    matricula = entry_matricula.get().strip()
    curso = entry_curso.get().strip() or "Técnico em Informática"
    if not nome or not matricula:
        messagebox.showwarning("Atenção", "Nome e matrícula são obrigatórios!")
        return
    try:
        Estudante.create(nome=nome, matricula=matricula, curso=curso)
        messagebox.showinfo("Sucesso", "Estudante cadastrado!")
        listar_estudantes()
        entry_nome.delete(0, tk.END)
        entry_matricula.delete(0, tk.END)
        entry_curso.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

def excluir_estudante():
    selecionado = listbox_estudantes.curselection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um estudante para excluir.")
        return
    item = listbox_estudantes.get(selecionado[0])
    estudante_id = item.split(" - ")[0]
    try:
        estudante = Estudante.get_by_id(estudante_id)
        estudante.delete_instance()
        messagebox.showinfo("Sucesso", "Estudante excluído!")
        listar_estudantes()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir: {e}")

def editar_estudante():
    selecionado = listbox_estudantes.curselection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um estudante para editar.")
        return
    item = listbox_estudantes.get(selecionado[0])
    estudante_id = item.split(" - ")[0]
    try:
        estudante = Estudante.get_by_id(estudante_id)
        novo_nome = entry_nome.get().strip()
        nova_matricula = entry_matricula.get().strip()
        novo_curso = entry_curso.get().strip() or "Técnico em Informática"
        if not novo_nome or not nova_matricula:
            messagebox.showwarning("Atenção", "Nome e matrícula são obrigatórios!")
            return
        estudante.nome = novo_nome
        estudante.matricula = nova_matricula
        estudante.curso = novo_curso
        estudante.save()
        messagebox.showinfo("Sucesso", "Estudante editado!")
        listar_estudantes()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao editar: {e}")

def preencher_campos(event):
    selecionado = listbox_estudantes.curselection()
    if not selecionado:
        return
    item = listbox_estudantes.get(selecionado[0])
    partes = item.split(" - ")
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, partes[1])
    entry_matricula.delete(0, tk.END)
    entry_matricula.insert(0, partes[2])
    entry_curso.delete(0, tk.END)
    entry_curso.insert(0, partes[3])

listbox_estudantes.bind('<<ListboxSelect>>', preencher_campos)

# Botões
btn_cadastrar = tk.Button(frame_cad_estudante, text="Cadastrar", command=cadastrar_estudante)
btn_cadastrar.grid(row=5, column=0, pady=5, sticky="ew")
btn_editar = tk.Button(frame_cad_estudante, text="Editar", command=editar_estudante)
btn_editar.grid(row=5, column=1, pady=5, sticky="ew")
btn_excluir = tk.Button(frame_cad_estudante, text="Excluir", command=excluir_estudante)
btn_excluir.grid(row=6, column=0, pady=5, sticky="ew")
btn_listar = tk.Button(frame_cad_estudante, text="Listar", command=listar_estudantes)
btn_listar.grid(row=6, column=1, pady=5, sticky="ew")

# Coloca os frames na janela principal
# Esses frames ficam todos sobrepostos na mesma posição
# porque o tkraise irá escolher quem será exibido a cada vez
# Todos ficam na mesma linha, coluna e com mesmo estilo de fixação

# Adiciona o frame de cadastro de estudante à janela
frame_inicio.grid(row=0,column=0,sticky="nesw")
frame_sobre.grid(row=0,column=0,sticky="nesw")
frame_cad_estudante.grid(row=0,column=0,sticky="nesw")


# Define qual frame vai aparecer ao iniciar o programa principal
frame_inicio.tkraise()

# Adiciona a barra de menu na janela principal do programa
janela.config(menu=menubar)

# Executa o programa na janela principal
janela.mainloop()