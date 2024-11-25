from entity.medicamento import Medicamento
from db import db
class MedicamentoRepository:
    @staticmethod
    def salvar(medicamento):
        db.session.add(medicamento)
        db.session.commit()

    @staticmethod
    def buscar_todos():
        return Medicamento.query.all()

    @staticmethod
    def buscar_por_id(id_medicamento):
        return Medicamento.query.get(id_medicamento)

    @staticmethod
    def excluir(medicamento):
        db.session.delete(medicamento)
        db.session.commit()
