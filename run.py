from app import create_app, db
from app.auth.models import User
from sqlalchemy import exc



flask_app = create_app('prod') # vai criar a instância da aplicação flask com a configuração 'prod' para implantação
with flask_app.app_context():

    '''como a aplicação está escalável, a instância de aplicação flask pode utilizar diversas configurações. Deste 
    modo, o banco de dados criado vai depender do contexto da aplicação que será criado em create_app (neste caso, 
    será criado um banco de dados da configuração relativa a 'dev' '''
    db.create_all()
    try:
        if not User.query.filter_by(user_name='Harry').first():
            User.create_user(user='Harry', email='harry@potter.com', password='secret')
    except exc.IntegrityError:
            flask_app.run()