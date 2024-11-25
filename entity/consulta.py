from sqlalchemy import ForeignKey
from db import db

class Consulta(db.Model):
    __tablename__ = 'consultas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # A coluna de chave primária correta
    data_consulta = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    veterinario_id = db.Column(db.Integer, db.ForeignKey('veterinarios.id'), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)

    # Relacionamentos
    veterinario = db.relationship('Veterinario', back_populates='consultas')
    paciente = db.relationship('Paciente', back_populates='consultas')
    exames = db.relationship('Exame', back_populates='consulta')
