from werkzeug.security import generate_password_hash, check_password_hash
from db import db
import uuid
from sqlalchemy.orm import relationship

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'  # Nome da tabela no singular
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    token_recuperacao_senha = db.Column(db.String(100), nullable=True)

    administradores = relationship('Administrador', back_populates='funcionario')  # Relacionamento com Administrador

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cargo": self.cargo
        }
    
    def __repr__(self):
        return f'<Funcionario {self.nome}>'

    def set_senha(self, senha):
        if not senha:
            raise ValueError("A senha não pode ser vazia ou nula")
        self.senha = generate_password_hash(senha)

    def verificar_senha(self, senha):
        if not senha:  # Verifique se a senha não é None
            return False
        return check_password_hash(self.senha, senha)

    def gerar_token_recuperacao(self):
        token = str(uuid.uuid4())
        self.token_recuperacao_senha = token
        return token
