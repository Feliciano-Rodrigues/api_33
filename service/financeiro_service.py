from entity.financeiro import Financeiro


class FinanceiroService:
    def __init__(self, repository):
        self.repository = repository

    def criar_financeiro(self, dados):
        financeiro = Financeiro(
            id_financeiro=None,
            id_consulta=dados['id_consulta'],
            id_exame=dados['id_exame'],
            id_internamento=dados['id_internamento'],
            valor_total=dados['valor_total'],
            data_pagamento=dados['data_pagamento'],
            forma_pagamento=dados['forma_pagamento']
        )
        self.repository.create(financeiro)

    def obter_financeiro(self, id_financeiro):
        return self.repository.get_by_id(id_financeiro)

    def listar_financeiros(self):
        return self.repository.get_all()

    def atualizar_financeiro(self, id_financeiro, dados):
        financeiro = Financeiro(
            id_financeiro=id_financeiro,
            id_consulta=dados['id_consulta'],
            id_exame=dados['id_exame'],
            id_internamento=dados['id_internamento'],
            valor_total=dados['valor_total'],
            data_pagamento=dados['data_pagamento'],
            forma_pagamento=dados['forma_pagamento']
        )
        self.repository.update(id_financeiro, financeiro)

    def remover_financeiro(self, id_financeiro):
        self.repository.delete(id_financeiro)
