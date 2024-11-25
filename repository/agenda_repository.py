from db import db

class AgendaRepository:
    def __init__(self):
        self.db = db

    def create(self, agenda):
        sql = '''INSERT INTO agendas (id_consulta, id_cirurgia, id_veterinario, disponibilidade, tipo, data, hora)
                 VALUES (?, ?, ?, ?, ?, ?, ?)'''
        self.db.session.execute(sql, (agenda.id_consulta, agenda.id_cirurgia, agenda.id_veterinario, agenda.disponibilidade, agenda.tipo, agenda.data, agenda.hora))
        self.db.session.commit()

    def get_by_id(self, id_agenda):
        sql = '''SELECT * FROM agendas WHERE id_agenda = ?'''
        return self.db.session.execute(sql, (id_agenda,)).fetchone()

    def get_all(self):
        sql = '''SELECT * FROM agendas'''
        return self.db.session.execute(sql).fetchall()

    def update(self, id_agenda, agenda):
        sql = '''UPDATE agendas SET id_consulta = ?, id_cirurgia = ?, id_veterinario = ?, disponibilidade = ?, tipo = ?, data = ?, hora = ? WHERE id_agenda = ?'''
        self.db.session.execute(sql, (agenda.id_consulta, agenda.id_cirurgia, agenda.id_veterinario, agenda.disponibilidade, agenda.tipo, agenda.data, agenda.hora, id_agenda))
        self.db.session.commit()

    def delete(self, id_agenda):
        sql = '''DELETE FROM agendas WHERE id_agenda = ?'''
        self.db.session.execute(sql, (id_agenda,))
        self.db.session.commit()
