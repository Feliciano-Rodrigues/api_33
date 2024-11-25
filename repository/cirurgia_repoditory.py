from db import db

class CirurgiaRepository:
    def __init__(self):
        self.db = db

    def create(self, cirurgia):
        sql = '''INSERT INTO cirurgias (id_veterinario, id_paciente, data_cirurgia, hora_inicio, hora_fim, tipo_cirurgia, observacoes, id_auxiliar, valor_cirurgia)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        self.db.session.execute(sql, (cirurgia.id_veterinario, cirurgia.id_paciente, cirurgia.data_cirurgia, cirurgia.hora_inicio, cirurgia.hora_fim, cirurgia.tipo_cirurgia, cirurgia.observacoes, cirurgia.id_auxiliar, cirurgia.valor_cirurgia))
        self.db.session.commit()

    def get_by_id(self, id_cirurgia):
        sql = '''SELECT * FROM cirurgias WHERE id_cirurgia = ?'''
        return self.db.session.execute(sql, (id_cirurgia,)).fetchone()

    def get_all(self):
        sql = '''SELECT * FROM cirurgias'''
        return self.db.session.execute(sql).fetchall()

    def update(self, id_cirurgia, cirurgia):
        sql = '''UPDATE cirurgias SET id_veterinario = ?, id_paciente = ?, data_cirurgia = ?, hora_inicio = ?, hora_fim = ?, tipo_cirurgia = ?, observacoes = ?, id_auxiliar = ?, valor_cirurgia = ? WHERE id_cirurgia = ?'''
        self.db.session.execute(sql, (cirurgia.id_veterinario, cirurgia.id_paciente, cirurgia.data_cirurgia, cirurgia.hora_inicio, cirurgia.hora_fim, cirurgia.tipo_cirurgia, cirurgia.observacoes, cirurgia.id_auxiliar, cirurgia.valor_cirurgia, id_cirurgia))
        self.db.session.commit()

    def delete(self, id_cirurgia):
        sql = '''DELETE FROM cirurgias WHERE id_cirurgia = ?'''
        self.db.session.execute(sql, (id_cirurgia,))
        self.db.session.commit()
