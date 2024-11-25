from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

# from entity.usuario import Usuario
from entity.cliente import Cliente
from entity.consulta import Consulta
from entity.funcionario import Funcionario
# Importe outras entidades conforme necessário

