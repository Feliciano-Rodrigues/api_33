from db import db
class Prescricao(db.Model):
    __tablename__ = 'prescricoes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_consulta = db.Column(db.Integer, db.ForeignKey('consultas.id'), nullable=False)  # Corrigido para 'consultas.id'
    medicamento = db.Column(db.String(255), nullable=False)
    posologia = db.Column(db.String(255), nullable=False)

    # Relacionamento com Consulta
    consulta = db.relationship('Consulta', back_populates='prescricoes')
