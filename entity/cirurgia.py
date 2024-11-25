from db import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class Cirurgia(db.Model):
    __tablename__ = 'cirurgias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(255), nullable=True)
    data_cirurgia = Column(Date, nullable=False)

    auxiliares_veterinarios = relationship('AuxiliarVeterinario', back_populates='cirurgia')  # Relacionamento com AuxiliarVeterinario

    def __repr__(self):
        return f"<Cirurgia(data_cirurgia={self.data_cirurgia}, descricao={self.descricao})>"
