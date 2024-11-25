from entity.exame import Exame


class ExameRepository:
    def __init__(self, session):
        self.session = session

    def add(self, exame):
        """Adiciona um novo exame."""
        self.session.add(exame)
        self.session.commit()

    def get_by_id(self, id_exame):
        """Obtém um exame pelo ID."""
        return self.session.query(Exame).filter_by(id_exame=id_exame).first()

    def list_all(self):
        """Lista todos os exames."""
        return self.session.query(Exame).all()

    def update(self, id_exame, dados):
        """Atualiza os dados de um exame existente."""
        exame = self.get_by_id(id_exame)
        if exame:
            for key, value in dados.items():
                setattr(exame, key, value)
            self.session.commit()
            return exame
        return None

    def delete(self, id_exame):
        """Remove um exame pelo ID."""
        exame = self.get_by_id(id_exame)
        if exame:
            self.session.delete(exame)
            self.session.commit()
            return True
        return False
