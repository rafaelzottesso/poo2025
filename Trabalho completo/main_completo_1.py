import sys
import os
from classes import Estudante, TipoProtocolo, Protocolo
import tkinter as tk
from tkinter import messagebox, ttk

class SistemaProtocolos:
    def __init__(self):
        """Construtor da classe - inicializa a aplicação"""
        # Configurações e constantes
        self.FONT_TITULO = ("Arial", 18)
        self.FONT_TEXTO = ("Arial", 13)
        
        # Variáveis de controle
        self.estudantes_dict = {}
        self.tipos_protocolo_dict = {}
        self.protocolo_editando = None
        
        # Inicialização da interface
        self.criar_janela_principal()
        self.criar_menu()
        self.criar_frames()
        self.iniciar_aplicacao()
    
    def criar_janela_principal(self):
        """Cria e configura a janela principal"""
        self.janela = tk.Tk()
        self.janela.title("Menu bar exemplo")
        self.janela.geometry("600x600")
    
    def criar_menu(self):
        """Cria a barra de menu da aplicação"""
        # Criação da barra principal de menu
        self.menubar = tk.Menu(self.janela)
        
        # Criação de um menu para a barra de menu
        menu_arquivo = tk.Menu(self.menubar, tearoff=False)
        menu_arquivo.add_command(label="Início", command=self.mostrar_inicio)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.janela.quit)
        self.menubar.add_cascade(label="Arquivo", menu=menu_arquivo)
        
        # Cria um novo menu com submenus
        menu_cadastro = tk.Menu(self.menubar, tearoff=False)
        menu_cadastro.add_command(label="Estudante", command=self.mostrar_cadastro_estudante)
        menu_cadastro.add_command(label="Tipo de protocolo", command=self.mostrar_cadastro_tipo_protocolo)
        menu_cadastro.add_separator()
        menu_cadastro.add_command(label="Protocolo", command=self.mostrar_cadastro_protocolo)
        self.menubar.add_cascade(label="Cadastro", menu=menu_cadastro)
        
        # Cria um outro menu com submenus
        menu_sobre = tk.Menu(self.menubar, tearoff=False)
        menu_sobre.add_command(label="Sobre Nós", command=self.mostrar_sobre)
        menu_sobre.add_separator()
        menu_sobre.add_command(label="Versão", command=lambda: messagebox.showinfo("Versão Atual", "Versão 1.0"))
        self.menubar.add_cascade(label="Sobre", menu=menu_sobre)
    
    def criar_frames(self):
        """Cria todos os frames da aplicação"""
        self.criar_frame_inicio()
        self.criar_frame_sobre()
        self.criar_frame_estudantes()
        self.criar_frame_tipo_protocolo()
        self.criar_frame_protocolos()
        
        # Posiciona todos os frames na mesma posição
        self.frame_inicio.grid(row=0, column=0, sticky="nesw")
        self.frame_sobre.grid(row=0, column=0, sticky="nesw")
        self.frame_cad_estudante.grid(row=0, column=0, sticky="nesw")
        self.frame_cad_tipo_protocolo.grid(row=0, column=0, sticky="nesw")
        self.frame_cad_protocolo.grid(row=0, column=0, sticky="nesw")
    
    def criar_frame_inicio(self):
        """Cria o frame da tela inicial"""
        self.frame_inicio = tk.Frame(self.janela)
        lb_ola = tk.Label(self.frame_inicio, text="Bem-vindo ao sistema", font=self.FONT_TITULO)
        lb_ola.pack(pady=30)
    
    def criar_frame_sobre(self):
        """Cria o frame da tela sobre"""
        self.frame_sobre = tk.Frame(self.janela)
        lb_alunos = tk.Label(self.frame_sobre, text="Desenvolvido por:", font=self.FONT_TITULO)
        lb_alunos.pack(pady=20)
        
        equipe = """
Felipe
Vitor
Rafael
"""
        lb_equipe = tk.Label(self.frame_sobre, text=equipe, font=self.FONT_TEXTO)
        lb_equipe.pack(pady=10)
    
    def criar_frame_estudantes(self):
        """Cria o frame de cadastro de estudantes"""
        self.frame_cad_estudante = tk.Frame(self.janela, padx=20, pady=10)
        
        # Título
        lb_titulo = tk.Label(self.frame_cad_estudante, text="Cadastro de Estudantes", font=self.FONT_TITULO)
        lb_titulo.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Nome
        lb_nome = tk.Label(self.frame_cad_estudante, text="Nome:", font=self.FONT_TEXTO)
        lb_nome.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome = tk.Entry(self.frame_cad_estudante, width=30)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)
        
        # Matrícula
        lb_matricula = tk.Label(self.frame_cad_estudante, text="Matrícula:", font=self.FONT_TEXTO)
        lb_matricula.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_matricula = tk.Entry(self.frame_cad_estudante, width=30)
        self.entry_matricula.grid(row=2, column=1, padx=5, pady=5)
        
        # Curso
        lb_curso = tk.Label(self.frame_cad_estudante, text="Curso:", font=self.FONT_TEXTO)
        lb_curso.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_curso = tk.Entry(self.frame_cad_estudante, width=30)
        self.entry_curso.grid(row=3, column=1, padx=5, pady=5)
        
        # Listbox para exibir estudantes
        self.listbox_estudantes = tk.Listbox(self.frame_cad_estudante, width=50, height=8)
        self.listbox_estudantes.grid(row=4, column=0, columnspan=2, pady=10)
        self.listbox_estudantes.bind('<<ListboxSelect>>', self.preencher_campos_estudante)
        
        # Botões
        btn_cadastrar = tk.Button(self.frame_cad_estudante, text="Cadastrar", command=self.cadastrar_estudante)
        btn_cadastrar.grid(row=5, column=0, pady=5, sticky="ew")
        btn_editar = tk.Button(self.frame_cad_estudante, text="Editar", command=self.editar_estudante)
        btn_editar.grid(row=5, column=1, pady=5, sticky="ew")
        btn_excluir = tk.Button(self.frame_cad_estudante, text="Excluir", command=self.excluir_estudante)
        btn_excluir.grid(row=6, column=0, pady=5, sticky="ew")
        btn_listar = tk.Button(self.frame_cad_estudante, text="Listar", command=self.listar_estudantes)
        btn_listar.grid(row=6, column=1, pady=5, sticky="ew")
    
    def criar_frame_tipo_protocolo(self):
        """Cria o frame de cadastro de tipo de protocolo"""
        self.frame_cad_tipo_protocolo = tk.Frame(self.janela, padx=20, pady=10)
        
        # Título
        lb_titulo_tp = tk.Label(self.frame_cad_tipo_protocolo, text="Cadastro de Tipo de Protocolo", font=self.FONT_TITULO)
        lb_titulo_tp.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Nome
        lb_nome_tp = tk.Label(self.frame_cad_tipo_protocolo, text="Nome:", font=self.FONT_TEXTO)
        lb_nome_tp.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome_tp = tk.Entry(self.frame_cad_tipo_protocolo, width=30)
        self.entry_nome_tp.grid(row=1, column=1, padx=5, pady=5)
        
        # Listbox para exibir tipos de protocolo
        self.listbox_tp = tk.Listbox(self.frame_cad_tipo_protocolo, width=50, height=8)
        self.listbox_tp.grid(row=2, column=0, columnspan=2, pady=10)
        self.listbox_tp.bind('<<ListboxSelect>>', self.preencher_campos_tp)
        
        # Botões
        btn_cadastrar_tp = tk.Button(self.frame_cad_tipo_protocolo, text="Cadastrar", command=self.cadastrar_tipo_protocolo)
        btn_cadastrar_tp.grid(row=3, column=0, pady=5, sticky="ew")
        btn_editar_tp = tk.Button(self.frame_cad_tipo_protocolo, text="Editar", command=self.editar_tipo_protocolo)
        btn_editar_tp.grid(row=3, column=1, pady=5, sticky="ew")
        btn_excluir_tp = tk.Button(self.frame_cad_tipo_protocolo, text="Excluir", command=self.excluir_tipo_protocolo)
        btn_excluir_tp.grid(row=4, column=0, pady=5, sticky="ew")
        btn_listar_tp = tk.Button(self.frame_cad_tipo_protocolo, text="Listar", command=self.listar_tipo_protocolo)
        btn_listar_tp.grid(row=4, column=1, pady=5, sticky="ew")
    
    def criar_frame_protocolos(self):
        """Cria o frame de cadastro de protocolos"""
        self.frame_cad_protocolo = tk.Frame(self.janela, padx=20, pady=10)
        
        # Título
        lb_titulo_protocolo = tk.Label(self.frame_cad_protocolo, text="Cadastro de Protocolos", font=self.FONT_TITULO)
        lb_titulo_protocolo.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Estudante (Combobox)
        lb_estudante = tk.Label(self.frame_cad_protocolo, text="Estudante:", font=self.FONT_TEXTO)
        lb_estudante.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.combo_estudante = ttk.Combobox(self.frame_cad_protocolo, width=40, state="readonly")
        self.combo_estudante.grid(row=1, column=1, padx=5, pady=5)
        
        # Tipo de Protocolo (Combobox)
        lb_tipo_protocolo = tk.Label(self.frame_cad_protocolo, text="Tipo de Protocolo:", font=self.FONT_TEXTO)
        lb_tipo_protocolo.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.combo_tipo_protocolo = ttk.Combobox(self.frame_cad_protocolo, width=40, state="readonly")
        self.combo_tipo_protocolo.grid(row=2, column=1, padx=5, pady=5)
        
        # Justificativa (Text)
        lb_justificativa = tk.Label(self.frame_cad_protocolo, text="Justificativa:", font=self.FONT_TEXTO)
        lb_justificativa.grid(row=3, column=0, sticky="ne", padx=5, pady=5)
        self.text_justificativa = tk.Text(self.frame_cad_protocolo, width=40, height=5)
        self.text_justificativa.grid(row=3, column=1, padx=5, pady=5)
        
        # Listbox para exibir protocolos
        self.listbox_protocolos = tk.Listbox(self.frame_cad_protocolo, width=70, height=8)
        self.listbox_protocolos.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Botões
        btn_cadastrar_protocolo = tk.Button(self.frame_cad_protocolo, text="Cadastrar", command=self.cadastrar_protocolo)
        btn_cadastrar_protocolo.grid(row=5, column=0, pady=5, sticky="ew")
        btn_carregar_protocolo = tk.Button(self.frame_cad_protocolo, text="Carregar p/ Edição", command=self.carregar_protocolo_para_edicao)
        btn_carregar_protocolo.grid(row=5, column=1, pady=5, sticky="ew")
        btn_editar_protocolo = tk.Button(self.frame_cad_protocolo, text="Salvar Edição", command=self.editar_protocolo)
        btn_editar_protocolo.grid(row=6, column=0, pady=5, sticky="ew")
        btn_excluir_protocolo = tk.Button(self.frame_cad_protocolo, text="Excluir", command=self.excluir_protocolo)
        btn_excluir_protocolo.grid(row=6, column=1, pady=5, sticky="ew")
        btn_listar_protocolo = tk.Button(self.frame_cad_protocolo, text="Atualizar Lista", command=self.listar_protocolos)
        btn_listar_protocolo.grid(row=7, column=0, pady=5, sticky="ew")
        btn_limpar_protocolo = tk.Button(self.frame_cad_protocolo, text="Novo/Limpar", command=self.limpar_campos_protocolo)
        btn_limpar_protocolo.grid(row=7, column=1, pady=5, sticky="ew")
        btn_status_protocolo = tk.Button(self.frame_cad_protocolo, text="Ver Status", command=self.mostrar_status_protocolo)
        btn_status_protocolo.grid(row=8, column=0, columnspan=2, pady=5, sticky="ew")
    
    # Métodos de navegação
    def mostrar_inicio(self):
        """Exibe a tela inicial"""
        self.frame_inicio.tkraise()
    
    def mostrar_sobre(self):
        """Exibe a tela sobre"""
        self.frame_sobre.tkraise()
    
    def mostrar_cadastro_estudante(self):
        """Exibe a tela de cadastro de estudantes"""
        self.listar_estudantes()
        self.frame_cad_estudante.tkraise()
    
    def mostrar_cadastro_tipo_protocolo(self):
        """Exibe a tela de cadastro de tipo de protocolo"""
        self.listar_tipo_protocolo()
        self.frame_cad_tipo_protocolo.tkraise()
    
    def mostrar_cadastro_protocolo(self):
        """Exibe a tela de cadastro de protocolo"""
        self.carregar_combobox_estudantes()
        self.carregar_combobox_tipos_protocolo()
        self.listar_protocolos()
        self.frame_cad_protocolo.tkraise()
    
    # Métodos para manipular estudantes
    def listar_estudantes(self):
        """Lista todos os estudantes na interface"""
        self.listbox_estudantes.delete(0, tk.END)
        for estudante in Estudante.select():
            self.listbox_estudantes.insert(tk.END, f"{estudante.id} - {estudante.nome} - {estudante.matricula} - {estudante.curso}")
    
    def cadastrar_estudante(self):
        """Cadastra um novo estudante"""
        nome = self.entry_nome.get().strip()
        matricula = self.entry_matricula.get().strip()
        curso = self.entry_curso.get().strip() or "Técnico em Informática"
        
        if not nome or not matricula:
            messagebox.showwarning("Atenção", "Nome e matrícula são obrigatórios!")
            return
        
        try:
            Estudante.create(nome=nome, matricula=matricula, curso=curso)
            messagebox.showinfo("Sucesso", "Estudante cadastrado!")
            self.listar_estudantes()
            self.entry_nome.delete(0, tk.END)
            self.entry_matricula.delete(0, tk.END)
            self.entry_curso.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")
    
    def excluir_estudante(self):
        """Remove um estudante"""
        selecionado = self.listbox_estudantes.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um estudante para excluir.")
            return
        
        item = self.listbox_estudantes.get(selecionado[0])
        estudante_id = item.split(" - ")[0]
        
        try:
            estudante = Estudante.get_by_id(estudante_id)
            estudante.delete_instance()
            messagebox.showinfo("Sucesso", "Estudante excluído!")
            self.listar_estudantes()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {e}")
    
    def editar_estudante(self):
        """Edita um estudante existente"""
        selecionado = self.listbox_estudantes.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um estudante para editar.")
            return
        
        item = self.listbox_estudantes.get(selecionado[0])
        estudante_id = item.split(" - ")[0]
        
        try:
            estudante = Estudante.get_by_id(estudante_id)
            novo_nome = self.entry_nome.get().strip()
            nova_matricula = self.entry_matricula.get().strip()
            novo_curso = self.entry_curso.get().strip() or "Técnico em Informática"
            
            if not novo_nome or not nova_matricula:
                messagebox.showwarning("Atenção", "Nome e matrícula são obrigatórios!")
                return
            
            estudante.nome = novo_nome
            estudante.matricula = nova_matricula
            estudante.curso = novo_curso
            estudante.save()
            messagebox.showinfo("Sucesso", "Estudante editado!")
            self.listar_estudantes()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao editar: {e}")
    
    def preencher_campos_estudante(self, event):
        """Preenche os campos ao selecionar um estudante"""
        selecionado = self.listbox_estudantes.curselection()
        if not selecionado:
            return
        
        item = self.listbox_estudantes.get(selecionado[0])
        partes = item.split(" - ")
        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, partes[1])
        self.entry_matricula.delete(0, tk.END)
        self.entry_matricula.insert(0, partes[2])
        self.entry_curso.delete(0, tk.END)
        self.entry_curso.insert(0, partes[3])
    
    # Métodos para manipular tipos de protocolo
    def listar_tipo_protocolo(self):
        """Lista todos os tipos de protocolo na interface"""
        self.listbox_tp.delete(0, tk.END)
        for tp in TipoProtocolo.select():
            self.listbox_tp.insert(tk.END, f"{tp.id} - {tp.nome}")
    
    def cadastrar_tipo_protocolo(self):
        """Cadastra um novo tipo de protocolo"""
        nome = self.entry_nome_tp.get().strip()
        if not nome:
            messagebox.showwarning("Atenção", "Nome é obrigatório!")
            return
        
        try:
            TipoProtocolo.create(nome=nome)
            messagebox.showinfo("Sucesso", "Tipo de Protocolo cadastrado!")
            self.listar_tipo_protocolo()
            self.entry_nome_tp.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")
    
    def excluir_tipo_protocolo(self):
        """Remove um tipo de protocolo"""
        selecionado = self.listbox_tp.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um tipo para excluir.")
            return
        
        item = self.listbox_tp.get(selecionado[0])
        tp_id = item.split(" - ")[0]
        
        try:
            tp = TipoProtocolo.get_by_id(tp_id)
            tp.delete_instance()
            messagebox.showinfo("Sucesso", "Tipo de Protocolo excluído!")
            self.listar_tipo_protocolo()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {e}")
    
    def editar_tipo_protocolo(self):
        """Edita um tipo de protocolo existente"""
        selecionado = self.listbox_tp.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um tipo para editar.")
            return
        
        item = self.listbox_tp.get(selecionado[0])
        tp_id = item.split(" - ")[0]
        
        try:
            tp = TipoProtocolo.get_by_id(tp_id)
            novo_nome = self.entry_nome_tp.get().strip()
            if not novo_nome:
                messagebox.showwarning("Atenção", "Nome é obrigatório!")
                return
            
            tp.nome = novo_nome
            tp.save()
            messagebox.showinfo("Sucesso", "Tipo de Protocolo editado!")
            self.listar_tipo_protocolo()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao editar: {e}")
    
    def preencher_campos_tp(self, event):
        """Preenche os campos ao selecionar um tipo de protocolo"""
        selecionado = self.listbox_tp.curselection()
        if not selecionado:
            return
        
        item = self.listbox_tp.get(selecionado[0])
        partes = item.split(" - ")
        self.entry_nome_tp.delete(0, tk.END)
        self.entry_nome_tp.insert(0, partes[1])
    
    # Métodos para carregar os comboboxes
    def carregar_combobox_estudantes(self):
        """Carrega os dados dos estudantes no combobox"""
        estudantes = list(Estudante.select())
        estudantes_lista = [f"{est.nome} - {est.matricula}" for est in estudantes]
        self.combo_estudante['values'] = estudantes_lista
        self.estudantes_dict = {f"{est.nome} - {est.matricula}": est.id for est in estudantes}
    
    def carregar_combobox_tipos_protocolo(self):
        """Carrega os dados dos tipos de protocolo no combobox"""
        tipos = list(TipoProtocolo.select())
        tipos_lista = [tp.nome for tp in tipos]
        self.combo_tipo_protocolo['values'] = tipos_lista
        self.tipos_protocolo_dict = {tp.nome: tp.id for tp in tipos}
    
    # Métodos para manipular protocolos
    def listar_protocolos(self):
        """Lista todos os protocolos na interface"""
        self.listbox_protocolos.delete(0, tk.END)
        for protocolo in Protocolo.select().join(Estudante).switch(Protocolo).join(TipoProtocolo):
            data_formatada = protocolo.data_hora.strftime("%d/%m/%Y %H:%M")
            self.listbox_protocolos.insert(tk.END, 
                f"{protocolo.id} - {protocolo.estudante.nome} - {protocolo.tipo.nome} - {data_formatada}")
    
    def cadastrar_protocolo(self):
        """Cadastra um novo protocolo"""
        estudante_selecionado = self.combo_estudante.get()
        tipo_selecionado = self.combo_tipo_protocolo.get()
        justificativa = self.text_justificativa.get("1.0", tk.END).strip()
        
        if not estudante_selecionado or not tipo_selecionado or not justificativa:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
            return
        
        try:
            estudante_id = self.estudantes_dict[estudante_selecionado]
            tipo_id = self.tipos_protocolo_dict[tipo_selecionado]
            
            Protocolo.create(
                estudante=estudante_id,
                tipo=tipo_id,
                justificativa=justificativa
            )
            messagebox.showinfo("Sucesso", "Novo protocolo cadastrado!")
            self.listar_protocolos()
            self.limpar_campos_protocolo()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")
    
    def excluir_protocolo(self):
        """Remove um protocolo"""
        selecionado = self.listbox_protocolos.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um protocolo para excluir.")
            return
        
        item = self.listbox_protocolos.get(selecionado[0])
        protocolo_id = item.split(" - ")[0]
        
        try:
            protocolo = Protocolo.get_by_id(protocolo_id)
            protocolo.delete_instance()
            messagebox.showinfo("Sucesso", "Protocolo excluído!")
            self.listar_protocolos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {e}")
    
    def editar_protocolo(self):
        """Edita um protocolo existente"""
        if self.protocolo_editando is None:
            messagebox.showwarning("Atenção", "Selecione um protocolo na lista para editar.")
            return
        
        estudante_selecionado = self.combo_estudante.get()
        tipo_selecionado = self.combo_tipo_protocolo.get()
        justificativa = self.text_justificativa.get("1.0", tk.END).strip()
        
        if not estudante_selecionado or not tipo_selecionado or not justificativa:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
            return
        
        try:
            estudante_id = self.estudantes_dict[estudante_selecionado]
            tipo_id = self.tipos_protocolo_dict[tipo_selecionado]
            
            self.protocolo_editando.estudante = estudante_id
            self.protocolo_editando.tipo = tipo_id
            self.protocolo_editando.justificativa = justificativa
            self.protocolo_editando.save()
            
            messagebox.showinfo("Sucesso", "Protocolo editado!")
            self.listar_protocolos()
            self.limpar_campos_protocolo()
            self.protocolo_editando = None
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao editar: {e}")
    
    def limpar_campos_protocolo(self):
        """Limpa os campos do formulário de protocolos"""
        self.combo_estudante.set("")
        self.combo_tipo_protocolo.set("")
        self.text_justificativa.delete("1.0", tk.END)
        self.protocolo_editando = None
    
    def carregar_protocolo_para_edicao(self):
        """Carrega um protocolo selecionado para edição"""
        selecionado = self.listbox_protocolos.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um protocolo na lista para carregar para edição.")
            return
        
        item = self.listbox_protocolos.get(selecionado[0])
        protocolo_id = item.split(" - ")[0]
        
        try:
            protocolo = Protocolo.get_by_id(protocolo_id)
            self.protocolo_editando = protocolo
            
            # Selecionar o estudante no combobox
            estudante_texto = f"{protocolo.estudante.nome} - {protocolo.estudante.matricula}"
            self.combo_estudante.set(estudante_texto)
            
            # Selecionar o tipo no combobox
            self.combo_tipo_protocolo.set(protocolo.tipo.nome)
            
            # Preencher a justificativa
            self.text_justificativa.delete("1.0", tk.END)
            self.text_justificativa.insert("1.0", protocolo.justificativa)
            
            messagebox.showinfo("Sucesso", f"Protocolo ID {protocolo_id} carregado para edição!")
        except Exception as e:
            self.protocolo_editando = None
            messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")
    
    def mostrar_status_protocolo(self):
        """Mostra o status atual do protocolo (editando ou novo)"""
        if self.protocolo_editando:
            messagebox.showinfo("Status", f"Editando protocolo ID: {self.protocolo_editando.id}\n"
                                         f"Estudante: {self.protocolo_editando.estudante.nome}\n"
                                         f"Tipo: {self.protocolo_editando.tipo.nome}")
        else:
            messagebox.showinfo("Status", "Modo: Cadastro de novo protocolo\n"
                                         "Selecione um protocolo e clique em 'Carregar p/ Edição' para editar.")
    
    def iniciar_aplicacao(self):
        """Inicia a aplicação"""
        self.frame_inicio.tkraise()
        self.janela.config(menu=self.menubar)
        self.janela.mainloop()

# Execução da aplicação
if __name__ == "__main__":
    sistema = SistemaProtocolos()
