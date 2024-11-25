from db import db
from entity.cliente import Cliente

class ClienteRepository:
    @staticmethod
    def adicionar(cliente):
        db.session.add(cliente)
        db.session.commit()

    @staticmethod
    def buscar_por_id(cliente_id):
        return Cliente.query.get(cliente_id)

    @staticmethod
    def atualizar(cliente):
        db.session.commit()

    @staticmethod
    def excluir(cliente):
        db.session.delete(cliente)
        db.session.commit()
