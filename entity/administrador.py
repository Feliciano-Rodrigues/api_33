from db import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Administrador(db.Model):
    __tablename__ = 'administradores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    funcionario_id = Column(Integer, ForeignKey('funcionarios.id'), nullable=False)  # Chave estrangeira correta

    funcionario = relationship('Funcionario', back_populates='administradores')  # Relacionamento com Funcionario

    def __repr__(self):
        return f"<Administrador(nome={self.nome})>"
