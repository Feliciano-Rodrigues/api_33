from db import db

class AuxiliarVeterinarioRepository:
    def __init__(self):
        self.db = db

    def create(self, auxiliar_veterinario):
        sql = '''INSERT INTO auxiliares_veterinarios (registro_profissional, setor_trabalho, data_contratacao)
                 VALUES (?, ?, ?)'''
        self.db.session.execute(sql, (auxiliar_veterinario.registro_profissional, auxiliar_veterinario.setor_trabalho, auxiliar_veterinario.data_contratacao))
        self.db.session.commit()

    def get_by_id(self, id_funcionario):
        sql = '''SELECT * FROM auxiliares_veterinarios WHERE id_funcionario = ?'''
        return self.db.session.execute(sql, (id_funcionario,)).fetchone()

    def get_all(self):
        sql = '''SELECT * FROM auxiliares_veterinarios'''
        return self.db.session.execute(sql).fetchall()

    def update(self, id_funcionario, auxiliar_veterinario):
        sql = '''UPDATE auxiliares_veterinarios SET registro_profissional = ?, setor_trabalho = ?, data_contratacao = ? WHERE id_funcionario = ?'''
        self.db.session.execute(sql, (auxiliar_veterinario.registro_profissional, auxiliar_veterinario.setor_trabalho, auxiliar_veterinario.data_contratacao, id_funcionario))
        self.db.session.commit()

    def delete(self, id_funcionario):
        sql = '''DELETE FROM auxiliares_veterinarios WHERE id_funcionario = ?'''
        self.db.session.execute(sql, (id_funcionario,))
        self.db.session.commit()
