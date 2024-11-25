from entity.cirurgia import Cirurgia


class CirurgiaService:
    def __init__(self, repository):
        self.repository = repository

    def criar_cirurgia(self, dados):
        cirurgia = Cirurgia(
            id_cirurgia=None,
            id_veterinario=dados['id_veterinario'],
            id_paciente=dados['id_paciente'],
            data_cirurgia=dados['data_cirurgia'],
            hora_inicio=dados['hora_inicio'],
            hora_fim=dados['hora_fim'],
            tipo_cirurgia=dados['tipo_cirurgia'],
            observacoes=dados['observacoes'],
            id_auxiliar=dados['id_auxiliar'],
            valor_cirurgia=dados['valor_cirurgia']
        )
        self.repository.create(cirurgia)

    def obter_cirurgia(self, id_cirurgia):
        return self.repository.get_by_id(id_cirurgia)

    def listar_cirurgias(self):
        return self.repository.get_all()

    def atualizar_cirurgia(self, id_cirurgia, dados):
        cirurgia = Cirurgia(
            id_cirurgia=id_cirurgia,
            id_veterinario=dados['id_veterinario'],
            id_paciente=dados['id_paciente'],
            data_cirurgia=dados['data_cirurgia'],
            hora_inicio=dados['hora_inicio'],
            hora_fim=dados['hora_fim'],
            tipo_cirurgia=dados['tipo_cirurgia'],
            observacoes=dados['observacoes'],
            id_auxiliar=dados['id_auxiliar'],
            valor_cirurgia=dados['valor_cirurgia']
        )
        self.repository.update(id_cirurgia, cirurgia)

    def remover_cirurgia(self, id_cirurgia):
        self.repository.delete(id_cirurgia)
