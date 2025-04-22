from peewee import *
# Importar bibliotecas de data e hora para preencher automaticamente
from datetime import datetime, date 

meu_bd = SqliteDatabase("meus_dados.db")

class MinhaBase(Model):
    class Meta:
        database = meu_bd

class Estudante(MinhaBase):
    nome = CharField()
    matricula = CharField(unique=True)
    curso = CharField(default="Técnico em Informática")

class TipoProtocolo(MinhaBase):
    nome = CharField()

class Protocolo(MinhaBase):
    estudante = ForeignKeyField(Estudante)
    justificativa = CharField()
    data_hora = DateTimeField(default=datetime.now)
    tipo = ForeignKeyField(TipoProtocolo)

# Depois de criar todas as suas classes
# Vamos criar o banco de dados e as tabelas
meu_bd.connect()
meu_bd.create_tables([Estudante, TipoProtocolo, Protocolo])
