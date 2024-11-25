from db import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Paciente(db.Model):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Chave primária correta
    nome = Column(String(100), nullable=False)
    especie = Column(String(30), nullable=False)
    raca = Column(String(50), nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)  # Chave estrangeira correta

    # Relacionamento com Cliente
    cliente = relationship("Cliente", back_populates="pacientes")
    # Relacionamento com Consulta
    consultas = relationship('Consulta', back_populates='paciente')
    # Relacionamento com Internamento
    internamentos = relationship('Internamento', back_populates='paciente')

    def __repr__(self):
        return f"<Paciente(nome={self.nome}, especie={self.especie}, raca={self.raca}, cliente_id={self.cliente_id})>"
