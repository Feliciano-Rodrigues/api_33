from entity.administrador import Administrador


class AdministradorService:
    def __init__(self, repository):
        self.repository = repository

    def criar_administrador(self, dados):
        administrador = Administrador(
            id_funcionario=None,
            responsabilidade=dados['responsabilidade'],
            data_contratacao=dados['data_contratacao']
        )
        self.repository.create(administrador)

    def obter_administrador(self, id_funcionario):
        return self.repository.get_by_id(id_funcionario)

    def listar_administradores(self):
        return self.repository.get_all()

    def atualizar_administrador(self, id_funcionario, dados):
        administrador = Administrador(
            id_funcionario=id_funcionario,
            responsabilidade=dados['responsabilidade'],
            data_contratacao=dados['data_contratacao']
        )
        self.repository.update(id_funcionario, administrador)

    def remover_administrador(self, id_funcionario):
        self.repository.delete(id_funcionario)
