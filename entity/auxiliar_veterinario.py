from db import db
from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class AuxiliarVeterinario(db.Model):
    __tablename__ = 'auxiliares_veterinarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    registro_profissional = Column(String(100), nullable=False)
    setor_trabalho = Column(String(100), nullable=False)
    data_contratacao = Column(Date, nullable=False)
    cirurgia_id = Column(Integer, ForeignKey('cirurgias.id'), nullable=False)  # Chave estrangeira correta

    cirurgia = relationship('Cirurgia', back_populates='auxiliares_veterinarios')  # Relacionamento com Cirurgia

    def __repr__(self):
        return f"<AuxiliarVeterinario(nome={self.nome}, registro_profissional={self.registro_profissional})>"
