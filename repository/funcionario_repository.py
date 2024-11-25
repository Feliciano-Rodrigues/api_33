from entity.funcionario import Funcionario
from db import db

class FuncionarioRepository:

    @staticmethod
    def adicionar(funcionario):
        db.session.add(funcionario)
        db.session.commit()

    @staticmethod
    def buscar_por_email(email):
        funcionario = Funcionario.query.filter_by(email=email).first()
        print(f"Funcionário encontrado: {funcionario}")  # Depuração
        return funcionario
    @staticmethod 
    def listar_todos(): 
        return Funcionario.query.all() #@staticmethod
    
    def buscar_por_id(funcionario_id):
        return Funcionario.query.get(funcionario_id)

    @staticmethod
    def atualizar(funcionario):
        # Atualiza os campos do funcionário diretamente, se necessário
        db.session.commit()  # Não é necessário o db.session.update(funcionario)

    @staticmethod
    def excluir(funcionario):
        db.session.delete(funcionario)
        db.session.commit()

    @staticmethod
    def buscar_por_token(token):
        funcionario = Funcionario.query.filter_by(token_recuperacao_senha=token).first()
        return funcionario

