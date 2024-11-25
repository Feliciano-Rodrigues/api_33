from db import db
from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

class Financeiro(db.Model):
    __tablename__ = 'financeiros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    consulta_id = Column(Integer, ForeignKey('consultas.id'), nullable=False)  # Referenciando a coluna 'id' corretamente
    valor = Column(Float, nullable=False)
    data_pagamento = Column(Date, nullable=True)

    consulta = relationship('Consulta', back_populates='financeiros')

    def __repr__(self):
        return f"<Financeiro(valor={self.valor}, data_pagamento={self.data_pagamento})>"
