# Controle de produtos

Um projeto pessoal de estudo para cadastrar e organizar produtos com Flask. Cada produto tem nome, preço, quantidade e um status de ativo ou inativo. A interface usa CSS puro, com um tema escuro e detalhes em verde neon.

## Objetivo

A ideia é praticar e conhecer Microframework Flask atrávés do desenvolvimento de uma aplicação web pequena do começo ao fim: criar rotas, receber dados de formulários, trabalhar com templates Jinja e salvar informações no banco usando SQLAlchemy.

## Funcionalidades

- Home com acesso ao cadastro e à listagem.
- Cadastro de produtos com validação dos campos.
- Listagem dos produtos, dos mais recentes para os mais antigos.
- Edição dos dados e do status de cada produto.
- Exclusão de produtos.
- Mensagens de confirmação com o nome do produto após cadastrar, editar ou excluir.
- Layout responsivo para desktop e celular.

## Tecnologias

- **Python e Flask:** aplicação e rotas.
- **SQLAlchemy, integrado pelo Flask-SQLAlchemy:** acesso ao banco e modelo de produto.
- **SQLite:** armazenamento local dos dados.
- **HTML/Jinja:** páginas e exibição dos dados.
- **CSS puro:** estilos, sem frameworks visuais.

## Estrutura básica

```text
controle_academico/
├── main.py                 # Aplicação, rotas e validação dos formulários
├── db.py                   # Instância do SQLAlchemy
├── models.py               # Modelo Produto
├── instance/
│   └── dados.db             # Banco SQLite, criado na primeira execução
├── templates/
│   ├── base.html           # Estrutura visual e mensagens compartilhadas
│   ├── index.html          # Home
│   ├── produto.html        # Formulário de cadastro e edição
│   └── produtos.html       # Listagem e ações de cada produto
├── static/
│   └── css/
│       └── style.css
└── README.md
```

## Como executar

Com o Python instalado, baixe ou clone o repositório e abra um terminal na pasta do projeto.

### 1. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative no Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Ou no Linux/macOS:

```bash
source .venv/bin/activate
```

### 2. Instale as dependências

```bash
python -m pip install Flask Flask-SQLAlchemy
```

O Flask-SQLAlchemy instala o SQLAlchemy como dependência. O suporte ao SQLite já faz parte do Python.

### 3. Inicie a aplicação

```bash
python main.py
```

Abra [http://127.0.0.1:5000](http://127.0.0.1:5000) no navegador. Ao iniciar por esse comando, a aplicação cria o banco e as tabelas que ainda não existem. Os dados ficam em `instance/dados.db`.

O projeto inicia com `debug=True`, para uso durante o desenvolvimento local. Para encerrar, pressione `Ctrl+C` no terminal.

As mensagens usam a sessão do Flask. O código aceita a variável de ambiente `SECRET_KEY`; se ela não estiver definida, gera uma chave temporária a cada execução. Não é necessário configurá-la para experimentar o projeto localmente.

## Como funciona o CRUD

CRUD é o conjunto das quatro operações básicas com os dados:

| Operação | No     projeto |
| --- | --- |
| **Create — criar** | O formulário em `/produto` cadastra um produto. |
| **Read — consultar** | A página `/produtos` mostra os produtos salvos. |
| **Update — atualizar** | O botão **Editar** abre o mesmo formulário com os dados do produto. |
| **Delete — excluir** | O botão **Excluir** envia um POST para remover o produto do banco. |

O cadastro e a edição compartilham a validação: o nome é obrigatório e pode ter até 100 caracteres; preço e quantidade não podem ser negativos, e a quantidade deve ser inteira. Depois de uma alteração concluída, a aplicação volta para a listagem e mostra uma mensagem, como “Produto Teclado atualizado com sucesso”.
