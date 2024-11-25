from db import db


class FinanceiroRepository:
    def __init__(self):
        self.db = db

    def create(self, financeiro):
        sql = '''INSERT INTO financeiros (id_consulta, id_exame, id_internamento, valor_total, data_pagamento, forma_pagamento)
                 VALUES (?, ?, ?, ?, ?, ?)'''
        self.db.session.execute(sql, (financeiro.id_consulta, financeiro.id_exame, financeiro.id_internamento, financeiro.valor_total, financeiro.data_pagamento, financeiro.forma_pagamento))
        self.db.session.commit()

    def get_by_id(self, id_financeiro):
        sql = '''SELECT * FROM financeiros WHERE id_financeiro = ?'''
        return self.db.session.execute(sql, (id_financeiro,)).fetchone()

    def get_all(self):
        sql = '''SELECT * FROM financeiros'''
        return self.db.session.execute(sql).fetchall()

    def update(self, id_financeiro, financeiro):
        sql = '''UPDATE financeiros SET id_consulta = ?, id_exame = ?, id_internamento = ?, valor_total = ?, data_pagamento = ?, forma_pagamento = ? WHERE id_financeiro = ?'''
        self.db.session.execute(sql, (financeiro.id_consulta, financeiro.id_exame, financeiro.id_internamento, financeiro.valor_total, financeiro.data_pagamento, financeiro.forma_pagamento, id_financeiro))
        self.db.session.commit()

    def delete(self, id_financeiro):
        sql = '''DELETE FROM financeiros WHERE id_financeiro = ?'''
        self.db.session.execute(sql, (id_financeiro,))
        self.db.session.commit()
