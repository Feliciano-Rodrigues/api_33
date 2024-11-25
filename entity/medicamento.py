from db import db

class Medicamento(db.Model):
    __tablename__ = "medicamentos"

    id_medicamento = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False)
    validade = db.Column(db.Date, nullable=False)
    cnpj_fornecedor = db.Column(db.String(14), nullable=False)
    valor_medicamento = db.Column(db.Float, nullable=False)

    # Relacionamento com Prescrição
    prescricoes = db.relationship('Prescricao', back_populates='medicamento', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Medicamento {self.nome}>"
