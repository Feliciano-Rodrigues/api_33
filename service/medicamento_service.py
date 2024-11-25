from repository.medicamento_repository import MedicamentoRepository
from entity.medicamento import Medicamento

class MedicamentoService:
    @staticmethod
    def criar(dados):
        medicamento = Medicamento(**dados)
        MedicamentoRepository.salvar(medicamento)
        return medicamento

    @staticmethod
    def listar_todos():
        return MedicamentoRepository.buscar_todos()

    @staticmethod
    def buscar_por_id(id_medicamento):
        return MedicamentoRepository.buscar_por_id(id_medicamento)

    @staticmethod
    def excluir(id_medicamento):
        medicamento = MedicamentoRepository.buscar_por_id(id_medicamento)
        if not medicamento:
            raise ValueError("Medicamento não encontrado")
        MedicamentoRepository.excluir(medicamento)
