from db import db

class AdministradorRepository:
    def __init__(self):
        self.db = db

    def create(self, administrador):
        sql = '''INSERT INTO administradores (responsabilidade, data_contratacao)
                 VALUES (?, ?)'''
        self.db.session.execute(sql, (administrador.responsabilidade, administrador.data_contratacao))
        self.db.session.commit()

    def get_by_id(self, id_funcionario):
        sql = '''SELECT * FROM administradores WHERE id_funcionario = ?'''
        return self.db.session.execute(sql, (id_funcionario,)).fetchone()

    def get_all(self):
        sql = '''SELECT * FROM administradores'''
        return self.db.session.execute(sql).fetchall()

    def update(self, id_funcionario, administrador):
        sql = '''UPDATE administradores SET responsabilidade = ?, data_contratacao = ? WHERE id_funcionario = ?'''
        self.db.session.execute(sql, (administrador.responsabilidade, administrador.data_contratacao, id_funcionario))
        self.db.session.commit()

    def delete(self, id_funcionario):
        sql = '''DELETE FROM administradores WHERE id_funcionario = ?'''
        self.db.session.execute(sql, (id_funcionario,))
        self.db.session.commit()
