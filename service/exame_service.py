from entity.exame import Exame


class ExameService:
    def __init__(self, repository):
        self.repository = repository

    def criar_exame(self, dados):
        """Cria um novo exame."""
        exame = Exame(**dados)
        self.repository.add(exame)
        return exame

    def obter_exame(self, id_exame):
        """Obtém um exame pelo ID."""
        return self.repository.get_by_id(id_exame)

    def listar_exames(self):
        """Lista todos os exames."""
        return self.repository.list_all()

    def atualizar_exame(self, id_exame, dados):
        """Atualiza os dados de um exame."""
        return self.repository.update(id_exame, dados)

    def remover_exame(self, id_exame):
        """Remove um exame pelo ID."""
        return self.repository.delete(id_exame)
