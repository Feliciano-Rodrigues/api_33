from entity.internamento import Internamento


class InternamentoService:
    def __init__(self, repository):
        self.repository = repository

    def criar_internamento(self, dados):
        internamento = Internamento(
            id_internamento=None,
            id_paciente=dados['id_paciente'],
            id_veterinario=dados['id_veterinario'],
            data_internacao=dados['data_internacao'],
            motivo=dados['motivo'],
            data_alta=dados['data_alta'],
            valor_diaria=dados['valor_diaria'],
            id_prescricao=dados['id_prescricao']
        )
        self.repository.create(internamento)

    def obter_internamento(self, id_internamento):
        return self.repository.get_by_id(id_internamento)

    def listar_internamentos(self):
        return self.repository.get_all()

    def atualizar_internamento(self, id_internamento, dados):
        internamento = Internamento(
            id_internamento=id_internamento,
            id_paciente=dados['id_paciente'],
            id_veterinario=dados['id_veterinario'],
            data_internacao=dados['data_internacao'],
            motivo=dados['motivo'],
            data_alta=dados['data_alta'],
            valor_diaria=dados['valor_diaria'],
            id_prescricao=dados['id_prescricao']
        )
        self.repository.update(id_internamento, internamento)

    def remover_internamento(self, id_internamento):
        self.repository.delete(id_internamento)
