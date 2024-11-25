from flask_sqlalchemy import SQLAlchemy

# Inicializando o objeto SQLAlchemy
db = SQLAlchemy()

def init_app(app):
    db.init_app(app)  # Inicializa a instância db com a aplicação Flask
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados (se necessário)


    
