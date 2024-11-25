from entity.prescricao import Prescricao
from db import db
class PrescricaoRepository:
    @staticmethod
    def salvar(prescricao):
        db.session.add(prescricao)
        db.session.commit()

    @staticmethod
    def buscar_todos():
        return Prescricao.query.all()

    @staticmethod
    def buscar_por_id(id_prescricao):
        return Prescricao.query.get(id_prescricao)

    @staticmethod
    def excluir(prescricao):
        db.session.delete(prescricao)
        db.session.commit()
