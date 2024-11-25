from repository.prescricao_repository import PrescricaoRepository
from entity.prescricao import Prescricao

class PrescricaoService:
    @staticmethod
    def criar(dados):
        prescricao = Prescricao(**dados)
        PrescricaoRepository.salvar(prescricao)
        return prescricao

    @staticmethod
    def listar_todas():
        return PrescricaoRepository.buscar_todos()

    @staticmethod
    def buscar_por_id(id_prescricao):
        return PrescricaoRepository.buscar_por_id(id_prescricao)

    @staticmethod
    def excluir(id_prescricao):
        prescricao = PrescricaoRepository.buscar_por_id(id_prescricao)
        if not prescricao:
            raise ValueError("Prescrição não encontrada")
        PrescricaoRepository.excluir(prescricao)
