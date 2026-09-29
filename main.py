import os

from math import isfinite

from flask import Flask, flash, redirect, render_template, request, url_for
from db import db
from models import Produto

app = Flask("__name__")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dados.db"
# A chave mantém as mensagens flash na sessão; sem configuração, muda a cada execução.
app.config["SECRET_KEY"] = "123456"
db.init_app(app)


def dados_produto():
    # Cadastro e edição compartilham a conversão e a validação dos campos.
    nome = request.form.get("nomeForm", "").strip()
    try:
        preco = float(request.form.get("precoForm", ""))
        quantidade = int(request.form.get("quantidadeForm", ""))
    except ValueError:
        raise ValueError("Informe um preço válido e uma quantidade inteira.")
    if not nome or len(nome) > 100:
        raise ValueError("Informe um nome com até 100 caracteres.")
    # Também rejeita valores especiais de float, como infinito e NaN.
    if not isfinite(preco) or preco < 0 or quantidade < 0:
        raise ValueError("Preço e quantidade devem ser maiores ou iguais a zero.")
    return dict(
        nome=nome, preco=preco, quantidade=quantidade, ativo="ativoForm" in request.form
    )


@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/produto", methods=["GET", "POST"])
def cad_produto():
    if request.method == "POST":
        try:
            dados = dados_produto()
        except ValueError as erro:
            flash(str(erro), "erro")
            return render_template("produto.html", produto=None), 400
        novo_produto = Produto(**dados)
        db.session.add(novo_produto)
        db.session.commit()
        flash(f"Produto {novo_produto.nome} cadastrado com sucesso", "sucesso")
        # O redirecionamento evita repetir o cadastro ao atualizar a página.
        return redirect(url_for("listar_produtos"))
    return render_template("produto.html", produto=None)


@app.route("/produtos")
def listar_produtos():
    produtos = db.session.query(Produto).order_by(Produto.id.desc()).all()
    return render_template("produtos.html", produtos=produtos)


@app.route("/produto/<int:produto_id>/editar", methods=["GET", "POST"])
def edi_produto(produto_id):
    produto = db.get_or_404(Produto, produto_id)
    if request.method == "POST":
        try:
            dados = dados_produto()
        except ValueError as erro:
            flash(str(erro), "erro")
            return render_template("produto.html", produto=produto), 400
        produto.nome = dados["nome"]
        produto.preco = dados["preco"]
        produto.quantidade = dados["quantidade"]
        produto.ativo = dados["ativo"]
        db.session.commit()
        flash(f"Produto {produto.nome} atualizado com sucesso", "sucesso")
        return redirect(url_for("listar_produtos"))
    return render_template("produto.html", produto=produto)


@app.route("/produto/<int:produto_id>/excluir", methods=["POST"])
def excluir_produto(produto_id):
    produto = db.get_or_404(Produto, produto_id)
    nome = produto.nome
    db.session.delete(produto)
    db.session.commit()
    flash(f"Produto {nome} excluído com sucesso", "sucesso")
    return redirect(url_for("listar_produtos"))


if __name__ == "__main__":
    # Cria as tabelas que ainda não existem, sem recriar as já presentes.
    with app.app_context():
        db.create_all()
    app.run(debug=True)
