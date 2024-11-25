# C:\api_estudo3\entity\cliente.py

from db import db  # Certifique-se de que 'db' está sendo importado corretamente

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(15), nullable=False)

    pacientes = db.relationship('Paciente', back_populates='cliente')

    def __repr__(self):
        return f'<Cliente {self.nome}>'
