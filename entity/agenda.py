from db import db
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Agenda(db.Model):
    __tablename__ = 'agendas'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Chave primária correta
    veterinario_id = Column(Integer, ForeignKey('veterinarios.id'), nullable=False)  # Referenciando a coluna 'id' corretamente
    data = Column(Date, nullable=False)
    horario = Column(String(20), nullable=False)
    descricao = Column(String(255), nullable=True)

    # Relacionamento com Veterinário
    veterinario = relationship('Veterinario', back_populates='agendas')

    def __repr__(self):
        return f"<Agenda(data={self.data}, horario={self.horario}, descricao={self.descricao})>"
