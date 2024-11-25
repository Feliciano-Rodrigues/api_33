from db import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Veterinario(db.Model):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    crm = Column(String(20), unique=True, nullable=False)
    especialidade = Column(String(100), nullable=False)
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"), nullable=False)

    # Relacionamento com Consulta
    consultas = relationship('Consulta', back_populates='veterinario')

    # Relacionamento com Agenda
    agendas = relationship('Agenda', back_populates='veterinario')

    def __repr__(self):
        return f"<Veterinario(crm={self.crm}, especialidade={self.especialidade})>"
