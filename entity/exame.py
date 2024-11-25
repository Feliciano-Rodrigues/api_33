from db import db
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Exame(db.Model):
    __tablename__ = 'exames'

    id = Column(Integer, primary_key=True, autoincrement=True)
    consulta_id = Column(Integer, ForeignKey('consultas.id'), nullable=False)  # Referenciando a coluna 'id'
    tipo_exame = Column(String(50), nullable=False)
    resultado = Column(String(255), nullable=False)
    data_exame = Column(Date, nullable=False)

    consulta = relationship('Consulta', back_populates='exames')

    def __repr__(self):
        return f"<Exame(tipo_exame={self.tipo_exame}, resultado={self.resultado}, data_exame={self.data_exame})>"
