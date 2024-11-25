from entity.agenda import Agenda


class AgendaService:
    def __init__(self, repository):
        self.repository = repository

    def criar_agenda(self, dados):
        agenda = Agenda(
            id_agenda=None,
            id_consulta=dados['id_consulta'],
            id_cirurgia=dados['id_cirurgia'],
            id_veterinario=dados['id_veterinario'],
            disponibilidade=dados['disponibilidade'],
            tipo=dados['tipo'],
            data=dados['data'],
            hora=dados['hora']
        )
        self.repository.create(agenda)

    def obter_agenda(self, id_agenda):
        return self.repository.get_by_id(id_agenda)

    def listar_agendas(self):
        return self.repository.get_all()

    def atualizar_agenda(self, id_agenda, dados):
        agenda = Agenda(
            id_agenda=id_agenda,
            id_consulta=dados['id_consulta'],
            id_cirurgia=dados['id_cirurgia'],
            id_veterinario=dados['id_veterinario'],
            disponibilidade=dados['disponibilidade'],
            tipo=dados['tipo'],
            data=dados['data'],
            hora=dados['hora']
        )
        self.repository.update(id_agenda, agenda)

    def remover_agenda(self, id_agenda):
        self.repository.delete(id_agenda)
