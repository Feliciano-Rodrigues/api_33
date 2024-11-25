from db import db
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Internamento(db.Model):
    __tablename__ = 'internamentos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'), nullable=False)  # Referenciando a coluna 'id' corretamente
    data_internamento = Column(Date, nullable=False)
    descricao = Column(String(255), nullable=True)

    paciente = relationship('Paciente', back_populates='internamentos')

    def __repr__(self):
        return f"<Internamento(data_internamento={self.data_internamento}, descricao={self.descricao})>"
