import re
import db
from entity.cliente import Cliente
from entity.paciente import Paciente
from repository.cliente_repository import ClienteRepository

class ClienteService:

    @staticmethod
    def adicionar(nome, email, telefone):
        # Validação do nome
        if not nome or len(nome) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")

        # Validação do email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email inválido.")

        # Validação do telefone
        if not re.match(r"^\d{10,11}$", telefone):
            raise ValueError("O telefone deve conter 10 ou 11 dígitos.")

        cliente = Cliente(nome=nome, email=email, telefone=telefone)
        ClienteRepository.adicionar(cliente)
        return cliente

    @staticmethod
    def buscar_por_id(cliente_id):
        cliente = ClienteRepository.buscar_por_id(cliente_id)
        if not cliente:
            raise ValueError("Cliente não encontrado.")
        return cliente

    @staticmethod
    def atualizar(cliente_id, nome=None, email=None, telefone=None):
        cliente = ClienteRepository.buscar_por_id(cliente_id)
        if not cliente:
            raise ValueError("Cliente não encontrado.")

        # Validação do nome
        if nome and len(nome) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")

        # Validação do email
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email inválido.")

        # Validação do telefone
        if telefone and not re.match(r"^\d{10,11}$", telefone):
            raise ValueError("O telefone deve conter 10 ou 11 dígitos.")

        if nome:
            cliente.nome = nome
        if email:
            cliente.email = email
        if telefone:
            cliente.telefone = telefone
        
        ClienteRepository.atualizar(cliente)
        return cliente

    @staticmethod
    def update_cliente_id(paciente_id, cliente_id):
        paciente = Paciente.query.get(paciente_id)
        if paciente is None:
            raise ValueError(f"Paciente com ID {paciente_id} não encontrado.")
        
        cliente = Cliente.query.get(cliente_id)
        if cliente is None:
            raise ValueError(f"Cliente com ID {cliente_id} não encontrado.")
        
        paciente.cliente_id = cliente_id
        db.session.commit()
        return paciente

    def excluir(cliente_id):
        cliente = ClienteRepository.buscar_por_id(cliente_id)
        if not cliente:
            return {"error": "Cliente não encontrado."}, 404
        
        # Verifica se o cliente possui pacientes associados
        pacientes = Paciente.query.filter_by(cliente_id=cliente_id).all()
        if pacientes:
            return {"error": "Não é possível excluir o cliente, pois ele tem pacientes associados."}, 400
        
        # Exclui o cliente após a validação
        try:
            ClienteRepository.excluir(cliente)
            return {"message": "Cliente excluído com sucesso."}, 200
        except Exception as e:
            return {"error": f"Erro ao excluir cliente: {str(e)}"}, 500
