from db import db

class Produto(db.Model):
    __tablename__ = 'PRODUTO'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    # O status é armazenado como 0 (inativo) ou 1 (ativo).
    ativo = db.Column(db.Integer, nullable=False, default=0)

