from db import db
class InternamentoRepository:
    def __init__(self):
        self.db = db

    def create(self, internamento):
        sql = '''INSERT INTO internamentos (id_paciente, id_veterinario, data_internacao, motivo, data_alta, valor_diaria, id_prescricao)
                 VALUES (?, ?, ?, ?, ?, ?, ?)'''
        self.db.session.execute(sql, (internamento.id_paciente, internamento.id_veterinario, internamento.data_internacao, internamento.motivo, internamento.data_alta, internamento.valor_diaria, internamento.id_prescricao))
        self.db.session.commit()

    def get_by_id(self, id_internamento):
        sql = '''SELECT * FROM internamentos WHERE id_internamento = ?'''
        return self.db.session.execute(sql, (id_internamento,)).fetchone()

    def get_all(self):
        sql = '''SELECT * FROM internamentos'''
        return self.db.session.execute(sql).fetchall()

    def update(self, id_internamento, internamento):
        sql = '''UPDATE internamentos SET id_paciente = ?, id_veterinario = ?, data_internacao = ?, motivo = ?, data_alta = ?, valor_diaria = ?, id_prescricao = ? WHERE id_internamento = ?'''
        self.db.session.execute(sql, (internamento.id_paciente, internamento.id_veterinario, internamento.data_internacao, internamento.motivo, internamento.data_alta, internamento.valor_diaria, internamento.id_prescricao, id_internamento))
        self.db.session.commit()

    def delete(self, id_internamento):
        sql = '''DELETE FROM internamentos WHERE id_internamento = ?'''
        self.db.session.execute(sql, (id_internamento,))
        self.db.session.commit()
