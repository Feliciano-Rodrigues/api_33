import jwt  # Certifique-se de que PyJWT está instalado
import datetime
from repository.funcionario_repository import FuncionarioRepository
from entity.funcionario import Funcionario

SECRET_KEY = 'minha_chave_secreta'

class FuncionarioService:

    @staticmethod
    def login(email, senha):
        funcionario = FuncionarioRepository.buscar_por_email(email)
        if funcionario and senha:
            if funcionario.verificar_senha(senha):
                return funcionario
        return None

    @staticmethod
    def adicionar(nome, email, senha, cargo):
        funcionario = Funcionario(nome=nome, email=email, cargo=cargo)
        funcionario.set_senha(senha)
        FuncionarioRepository.adicionar(funcionario)
        return funcionario

    @staticmethod
    def buscar_por_email(email):
        return FuncionarioRepository.buscar_por_email(email)

    @staticmethod
    def buscar_por_id(funcionario_id):  # Método adicionado
        return FuncionarioRepository.buscar_por_id(funcionario_id)

    @staticmethod
    def gerar_token(funcionario):
        payload = {
            'id': funcionario.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token

    @staticmethod
    def gerar_token_recuperacao(funcionario):
        token = funcionario.gerar_token_recuperacao()
        FuncionarioRepository.atualizar(funcionario)
        return token

    @staticmethod
    def recuperar_senha(token, nova_senha):
        funcionario = FuncionarioRepository.buscar_por_token(token)
        if funcionario and nova_senha:
            funcionario.set_senha(nova_senha)
            funcionario.token_recuperacao_senha = None
            FuncionarioRepository.atualizar(funcionario)
            return funcionario
        return None

    @staticmethod
    def atualizar(funcionario_id, nome, email, senha=None, cargo=None):
        funcionario = Funcionario.query.get(funcionario_id)
        if funcionario:
            funcionario.nome = nome
            funcionario.email = email
            if senha:
                funcionario.set_senha(senha)
            if cargo:
                funcionario.cargo = cargo
            FuncionarioRepository.atualizar(funcionario)
            return funcionario
        return None

    @staticmethod
    def excluir(funcionario_id):
        funcionario = Funcionario.query.get(funcionario_id)
        if funcionario:
            FuncionarioRepository.excluir(funcionario)
            return True
        return False

