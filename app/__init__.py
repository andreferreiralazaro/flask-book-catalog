## app/__init__.py ##

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

## Criando instâncias ##

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login' #deixa o login_manager saber o nome da função usada para logar
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()

def create_app(config_type):
# A instância do aplicativo flask deve ser criada a partir de uma função, pois não está no contexto global
## dev, test, or prod

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    # vai juntar C:\\Users\\Andre\\PycharmProjects\\book_catalog + config + arquivo.py

    app.config.from_pyfile(configuration)

    # vai carregar a configuração a partir de um arquivo .py que será passado para a função (dev, test, prod)

    db.init_app(app) # vai ligar o banco de dados com o flask app. Detalhe: vai criar as tabelas, mas o BD deve ser criado no postgres
    migrate.init_app(app,db)    # inicializando uma migração, caso haja uma criação de banco de dados anterior

    bootstrap.init_app(app)     # Inicializando o bootstrap

    ## Inicializando o login_manager e bcrypt ##

    login_manager.init_app(app)
    bcrypt.init_app(app)

#####################################################

    from app.catalog import main, models # este app não é a instância de aplicação flask, mas sim a pasta do pacote raiz
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)


    return app