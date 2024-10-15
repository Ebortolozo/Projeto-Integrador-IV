from peewee import Model, CharField, DateField, IntegerField, FloatField
from database.database import db

class Remedio(Model):
    nome = CharField()
    categoria = CharField()
    data_venda = DateField()
    quant_vendida = CharField()
    estoque_atual = IntegerField()
    preco = FloatField()
    data_ultima_compra = DateField()
    data_vencimento = DateField()
    media_venda_diaria = FloatField()

    class Meta:
        database = db