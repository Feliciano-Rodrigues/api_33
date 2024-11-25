from entity.auxiliar_veterinario import AuxiliarVeterinario


class AuxiliarVeterinarioService:
    def __init__(self, repository):
        self.repository = repository

    def criar_auxiliar_veterinario(self, dados):
        auxiliar_veterinario = AuxiliarVeterinario(
            id_funcionario=None,
            registro_profissional=dados['registro_profissional'],
            setor_trabalho=dados['setor_trabalho'],
            data_contratacao=dados['data_contratacao']
        )
        self.repository.create(auxiliar_veterinario)

    def obter_auxiliar_veterinario(self, id_funcionario):
        return self.repository.get_by_id(id_funcionario)

    def listar_auxiliares_veterinarios(self):
        return self.repository.get_all()

    def atualizar_auxiliar_veterinario(self, id_funcionario, dados):
        auxiliar_veterinario = AuxiliarVeterinario(
            id_funcionario=id_funcionario,
            registro_profissional=dados['registro_profissional'],
            setor_trabalho=dados['setor_trabalho'],
            data_contratacao=dados['data_contratacao']
        )
        self.repository.update(id_funcionario, auxiliar_veterinario)

    def remover_auxiliar_veterinario(self, id_funcionario):
        self.repository.delete(id_funcionario)
