import sys
import os
from classes import Estudante, TipoProtocolo, Protocolo
import tkinter as tk
from tkinter import messagebox, ttk


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

# Função que mostra o frame de cadastro de tipo de protocolo
def cad_tipo_protocolo():
    # Inicializa a lista ao abrir a tela
    listar_tipo_protocolo()
    # Abre a tela de tipo de protocolo
    frame_cad_tipo_protocolo.tkraise()

# Função que mostra o frame de cadastro de protocolo
def cad_protocolo():
    # Carrega os dados nos comboboxes e inicializa a lista
    carregar_combobox_estudantes()
    carregar_combobox_tipos_protocolo()
    listar_protocolos()
    # Abre a tela de protocolo
    frame_cad_protocolo.tkraise()

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
menu_cadastro.add_command(label="Tipo de protocolo",command=cad_tipo_protocolo)
menu_cadastro.add_separator()
menu_cadastro.add_command(label="Protocolo",command=cad_protocolo)
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

# Frame de cadastro de tipo de protocolo
frame_cad_tipo_protocolo = tk.Frame(janela, padx=20, pady=10)

# Título
lb_titulo_tp = tk.Label(frame_cad_tipo_protocolo, text="Cadastro de Tipo de Protocolo", font=FONT_TITULO)
lb_titulo_tp.grid(row=0, column=0, columnspan=2, pady=10)

# Nome
lb_nome_tp = tk.Label(frame_cad_tipo_protocolo, text="Nome:", font=FONT_TEXTO)
lb_nome_tp.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_nome_tp = tk.Entry(frame_cad_tipo_protocolo, width=30)
entry_nome_tp.grid(row=1, column=1, padx=5, pady=5)

# Listbox para exibir tipos de protocolo
listbox_tp = tk.Listbox(frame_cad_tipo_protocolo, width=50, height=8)
listbox_tp.grid(row=2, column=0, columnspan=2, pady=10)

# Funções para manipular tipos de protocolo (inserir, editar, excluir, listar)
def listar_tipo_protocolo():
    listbox_tp.delete(0, tk.END)
    for tp in TipoProtocolo.select():
        listbox_tp.insert(tk.END, f"{tp.id} - {tp.nome}")

def cadastrar_tipo_protocolo():
    nome = entry_nome_tp.get().strip()
    if not nome:
        messagebox.showwarning("Atenção", "Nome é obrigatório!")
        return
    try:
        TipoProtocolo.create(nome=nome)
        messagebox.showinfo("Sucesso", "Tipo de Protocolo cadastrado!")
        listar_tipo_protocolo()
        entry_nome_tp.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

def excluir_tipo_protocolo():
    selecionado = listbox_tp.curselection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um tipo para excluir.")
        return
    item = listbox_tp.get(selecionado[0])
    tp_id = item.split(" - ")[0]
    try:
        tp = TipoProtocolo.get_by_id(tp_id)
        tp.delete_instance()
        messagebox.showinfo("Sucesso", "Tipo de Protocolo excluído!")
        listar_tipo_protocolo()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir: {e}")

def editar_tipo_protocolo():
    selecionado = listbox_tp.curselection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um tipo para editar.")
        return
    item = listbox_tp.get(selecionado[0])
    tp_id = item.split(" - ")[0]
    try:
        tp = TipoProtocolo.get_by_id(tp_id)
        novo_nome = entry_nome_tp.get().strip()
        if not novo_nome:
            messagebox.showwarning("Atenção", "Nome é obrigatório!")
            return
        tp.nome = novo_nome
        tp.save()
        messagebox.showinfo("Sucesso", "Tipo de Protocolo editado!")
        listar_tipo_protocolo()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao editar: {e}")

def preencher_campos_tp(event):
    selecionado = listbox_tp.curselection()
    if not selecionado:
        return
    item = listbox_tp.get(selecionado[0])
    partes = item.split(" - ")
    entry_nome_tp.delete(0, tk.END)
    entry_nome_tp.insert(0, partes[1])

listbox_tp.bind('<<ListboxSelect>>', preencher_campos_tp)

# Botões
btn_cadastrar_tp = tk.Button(frame_cad_tipo_protocolo, text="Cadastrar", command=cadastrar_tipo_protocolo)
btn_cadastrar_tp.grid(row=3, column=0, pady=5, sticky="ew")
btn_editar_tp = tk.Button(frame_cad_tipo_protocolo, text="Editar", command=editar_tipo_protocolo)
btn_editar_tp.grid(row=3, column=1, pady=5, sticky="ew")
btn_excluir_tp = tk.Button(frame_cad_tipo_protocolo, text="Excluir", command=excluir_tipo_protocolo)
btn_excluir_tp.grid(row=4, column=0, pady=5, sticky="ew")
btn_listar_tp = tk.Button(frame_cad_tipo_protocolo, text="Listar", command=listar_tipo_protocolo)
btn_listar_tp.grid(row=4, column=1, pady=5, sticky="ew")

# Frame de cadastro de protocolo
frame_cad_protocolo = tk.Frame(janela, padx=20, pady=10)

# Título
lb_titulo_protocolo = tk.Label(frame_cad_protocolo, text="Cadastro de Protocolos", font=FONT_TITULO)
lb_titulo_protocolo.grid(row=0, column=0, columnspan=2, pady=10)

# Estudante (Combobox)
lb_estudante = tk.Label(frame_cad_protocolo, text="Estudante:", font=FONT_TEXTO)
lb_estudante.grid(row=1, column=0, sticky="e", padx=5, pady=5)
combo_estudante = ttk.Combobox(frame_cad_protocolo, width=40, state="readonly")
combo_estudante.grid(row=1, column=1, padx=5, pady=5)

# Tipo de Protocolo (Combobox)
lb_tipo_protocolo = tk.Label(frame_cad_protocolo, text="Tipo de Protocolo:", font=FONT_TEXTO)
lb_tipo_protocolo.grid(row=2, column=0, sticky="e", padx=5, pady=5)
combo_tipo_protocolo = ttk.Combobox(frame_cad_protocolo, width=40, state="readonly")
combo_tipo_protocolo.grid(row=2, column=1, padx=5, pady=5)

# Justificativa (Text)
lb_justificativa = tk.Label(frame_cad_protocolo, text="Justificativa:", font=FONT_TEXTO)
lb_justificativa.grid(row=3, column=0, sticky="ne", padx=5, pady=5)
text_justificativa = tk.Text(frame_cad_protocolo, width=40, height=5)
text_justificativa.grid(row=3, column=1, padx=5, pady=5)

# Listbox para exibir protocolos
listbox_protocolos = tk.Listbox(frame_cad_protocolo, width=70, height=8)
listbox_protocolos.grid(row=4, column=0, columnspan=2, pady=10)

# Dicionários para mapear valores dos comboboxes
estudantes_dict = {}
tipos_protocolo_dict = {}

# Variável global para armazenar o protocolo sendo editado
protocolo_editando = None

# Funções para carregar os comboboxes
def carregar_combobox_estudantes():
    global estudantes_dict
    estudantes = list(Estudante.select())
    estudantes_lista = [f"{est.nome} - {est.matricula}" for est in estudantes]
    combo_estudante['values'] = estudantes_lista
    estudantes_dict = {f"{est.nome} - {est.matricula}": est.id for est in estudantes}

def carregar_combobox_tipos_protocolo():
    global tipos_protocolo_dict
    tipos = list(TipoProtocolo.select())
    tipos_lista = [tp.nome for tp in tipos]
    combo_tipo_protocolo['values'] = tipos_lista
    tipos_protocolo_dict = {tp.nome: tp.id for tp in tipos}

# Funções para manipular protocolos
def listar_protocolos():
    listbox_protocolos.delete(0, tk.END)
    for protocolo in Protocolo.select().join(Estudante).switch(Protocolo).join(TipoProtocolo):
        data_formatada = protocolo.data_hora.strftime("%d/%m/%Y %H:%M")
        listbox_protocolos.insert(tk.END, 
            f"{protocolo.id} - {protocolo.estudante.nome} - {protocolo.tipo.nome} - {data_formatada}")

def cadastrar_protocolo():
    global protocolo_editando
    
    estudante_selecionado = combo_estudante.get()
    tipo_selecionado = combo_tipo_protocolo.get()
    justificativa = text_justificativa.get("1.0", tk.END).strip()
    
    if not estudante_selecionado or not tipo_selecionado or not justificativa:
        messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
        return
    
    try:
        estudante_id = estudantes_dict[estudante_selecionado]
        tipo_id = tipos_protocolo_dict[tipo_selecionado]
        
        # Sempre criar novo protocolo nesta função
        Protocolo.create(
            estudante=estudante_id,
            tipo=tipo_id,
            justificativa=justificativa
        )
        
        messagebox.showinfo("Sucesso", "Novo protocolo cadastrado!")
        listar_protocolos()
        limpar_campos_protocolo()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

def excluir_protocolo():
    selecionado = listbox_protocolos.curselection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um protocolo para excluir.")
        return
    
    item = listbox_protocolos.get(selecionado[0])
    protocolo_id = item.split(" - ")[0]
    
    try:
        protocolo = Protocolo.get_by_id(protocolo_id)
        protocolo.delete_instance()
        messagebox.showinfo("Sucesso", "Protocolo excluído!")
        listar_protocolos()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir: {e}")

def editar_protocolo():
    global protocolo_editando
    
    if protocolo_editando is None:
        messagebox.showwarning("Atenção", "Selecione um protocolo na lista para editar.")
        return
    
    estudante_selecionado = combo_estudante.get()
    tipo_selecionado = combo_tipo_protocolo.get()
    justificativa = text_justificativa.get("1.0", tk.END).strip()
    
    if not estudante_selecionado or not tipo_selecionado or not justificativa:
        messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
        return
    
    try:
        estudante_id = estudantes_dict[estudante_selecionado]
        tipo_id = tipos_protocolo_dict[tipo_selecionado]
        
        protocolo_editando.estudante = estudante_id
        protocolo_editando.tipo = tipo_id
        protocolo_editando.justificativa = justificativa
        protocolo_editando.save()
        
        messagebox.showinfo("Sucesso", "Protocolo editado!")
        listar_protocolos()
        limpar_campos_protocolo()
        protocolo_editando = None  # Limpa a variável após editar
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao editar: {e}")

def limpar_campos_protocolo():
    global protocolo_editando
    combo_estudante.set("")
    combo_tipo_protocolo.set("")
    text_justificativa.delete("1.0", tk.END)
    protocolo_editando = None  # Limpa a variável de edição

def carregar_protocolo_para_edicao():
    global protocolo_editando
    
    selecionado = listbox_protocolos.curselection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um protocolo na lista para carregar para edição.")
        return
    
    item = listbox_protocolos.get(selecionado[0])
    protocolo_id = item.split(" - ")[0]
    
    try:
        protocolo = Protocolo.get_by_id(protocolo_id)
        protocolo_editando = protocolo  # Armazena o protocolo sendo editado
        
        # Selecionar o estudante no combobox
        estudante_texto = f"{protocolo.estudante.nome} - {protocolo.estudante.matricula}"
        combo_estudante.set(estudante_texto)
        
        # Selecionar o tipo no combobox
        combo_tipo_protocolo.set(protocolo.tipo.nome)
        
        # Preencher a justificativa
        text_justificativa.delete("1.0", tk.END)
        text_justificativa.insert("1.0", protocolo.justificativa)
        
        messagebox.showinfo("Sucesso", f"Protocolo ID {protocolo_id} carregado para edição!")
        
    except Exception as e:
        protocolo_editando = None
        messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")

# Remover o bind automático que causava o problema
# listbox_protocolos.bind('<<ListboxSelect>>', preencher_campos_protocolo)

# Botões
btn_cadastrar_protocolo = tk.Button(frame_cad_protocolo, text="Cadastrar", command=cadastrar_protocolo)
btn_cadastrar_protocolo.grid(row=5, column=0, pady=5, sticky="ew")
btn_carregar_protocolo = tk.Button(frame_cad_protocolo, text="Carregar p/ Edição", command=carregar_protocolo_para_edicao)
btn_carregar_protocolo.grid(row=5, column=1, pady=5, sticky="ew")
btn_editar_protocolo = tk.Button(frame_cad_protocolo, text="Salvar Edição", command=editar_protocolo)
btn_editar_protocolo.grid(row=6, column=0, pady=5, sticky="ew")
btn_excluir_protocolo = tk.Button(frame_cad_protocolo, text="Excluir", command=excluir_protocolo)
btn_excluir_protocolo.grid(row=6, column=1, pady=5, sticky="ew")
btn_listar_protocolo = tk.Button(frame_cad_protocolo, text="Atualizar Lista", command=listar_protocolos)
btn_listar_protocolo.grid(row=7, column=0, pady=5, sticky="ew")
btn_limpar_protocolo = tk.Button(frame_cad_protocolo, text="Novo/Limpar", command=limpar_campos_protocolo)
btn_limpar_protocolo.grid(row=7, column=1, pady=5, sticky="ew")

# Função para mostrar status do que está sendo feito
def mostrar_status_protocolo():
    global protocolo_editando
    if protocolo_editando:
        messagebox.showinfo("Status", f"Editando protocolo ID: {protocolo_editando.id}\n"
                                    f"Estudante: {protocolo_editando.estudante.nome}\n"
                                    f"Tipo: {protocolo_editando.tipo.nome}")
    else:
        messagebox.showinfo("Status", "Modo: Cadastro de novo protocolo\n"
                                    "Selecione um protocolo e clique em 'Carregar p/ Edição' para editar.")

btn_status_protocolo = tk.Button(frame_cad_protocolo, text="Ver Status", command=mostrar_status_protocolo)
btn_status_protocolo.grid(row=8, column=0, columnspan=2, pady=5, sticky="ew")

# Coloca os frames na janela principal
# Esses frames ficam todos sobrepostos na mesma posição
# porque o tkraise irá escolher quem será exibido a cada vez
# Todos ficam na mesma linha, coluna e com mesmo estilo de fixação

# Adiciona o frame de cadastro de estudante à janela
frame_inicio.grid(row=0,column=0,sticky="nesw")
frame_sobre.grid(row=0,column=0,sticky="nesw")
frame_cad_estudante.grid(row=0,column=0,sticky="nesw")
frame_cad_tipo_protocolo.grid(row=0,column=0,sticky="nesw")
frame_cad_protocolo.grid(row=0,column=0,sticky="nesw")


# Define qual frame vai aparecer ao iniciar o programa principal
frame_inicio.tkraise()

# Adiciona a barra de menu na janela principal do programa
janela.config(menu=menubar)

# Executa o programa na janela principal
janela.mainloop()