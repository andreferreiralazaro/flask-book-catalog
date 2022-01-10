## app/catalog/__init__.py ##

from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')


from app.catalog import routes

''' ao mesmo tempo que main é passado para o arquivo routes.py, este arquivo também importa routes como módulo.
trata-se de uma referência cruzada que pode causar erros chamados erros de referência circular
 esta referência cruzada existe porque os módulos dependem uns dos outros. Deste modo, a importação de routes deve vir
  abaixo, após a definição de main'''
