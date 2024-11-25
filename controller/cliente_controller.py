from flask import Blueprint, request, jsonify
import db
from entity.cliente import Cliente
from service.cliente_service import ClienteService

cliente_bp = Blueprint('cliente', __name__)

# Adicionar Cliente
from flask import Blueprint, request, jsonify
from db import db  # Importando o db do arquivo db.py
from entity.cliente import Cliente  # Importando o modelo Cliente

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes', methods=['POST'])
def create_cliente():
    try:
        # Recebe os dados do cliente da requisição
        data = request.json
        cliente = Cliente(nome=data['nome'], email=data['email'], telefone=data['telefone'])

        # Adiciona o cliente ao banco de dados e realiza o commit
        db.session.add(cliente)
        db.session.commit()

        return jsonify({"message": "Cliente criado com sucesso!", "id": cliente.id}), 201
    except Exception as e:
        db.session.rollback()  # Faz rollback em caso de erro
        return jsonify({"error": str(e)}), 500

@cliente_bp.route('/clientes', methods=['GET'])
def get_all_clientes():
    clientes = Cliente.query.all()
    result = [
        {"id": cliente.id, "nome": cliente.nome, "email": cliente.email, "telefone": cliente.telefone}
        for cliente in clientes
    ]
    return jsonify(result), 200

@cliente_bp.route('/clientes/<int:id>', methods=['GET'])
def get_cliente_by_id(id):
    try:
        cliente = Cliente.query.get(id)  # Consulta o cliente pelo ID
        if cliente:
            return jsonify({
                "id": cliente.id,
                "nome": cliente.nome,
                "email": cliente.email,
                "telefone": cliente.telefone
            }), 200
        else:
            return jsonify({"error": "Cliente não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Atualizar Cliente
@cliente_bp.route('/clientes/update/<int:cliente_id>', methods=['PUT'])
@cliente_bp.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    try:
        # Recupera o cliente com o ID fornecido
        cliente = Cliente.query.get(id)
        if not cliente:
            return jsonify({"error": "Cliente não encontrado"}), 404

        # Atualiza os dados do cliente com os dados enviados no corpo da requisição
        cliente_data = request.json
        cliente.nome = cliente_data['nome']
        cliente.email = cliente_data['email']
        cliente.telefone = cliente_data['telefone']

        db.session.commit()  # Salva as mudanças no banco de dados

        return jsonify({
            "id": cliente.id,
            "nome": cliente.nome,
            "email": cliente.email,
            "telefone": cliente.telefone
        }), 200

    except Exception as e:
        db.session.rollback()  # Faz rollback em caso de erro
        return jsonify({"error": str(e)}), 400

# Excluir Cliente
@cliente_bp.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    try:
        # Recupera o cliente pelo ID
        cliente = Cliente.query.get(id)
        if not cliente:
            return jsonify({"error": "Cliente não encontrado"}), 404

        # Deleta o cliente
        db.session.delete(cliente)
        db.session.commit()  # Comita a exclusão no banco de dados

        return jsonify({"message": "Cliente excluído com sucesso"}), 200

    except Exception as e:
        db.session.rollback()  # Faz rollback em caso de erro
        return jsonify({"error": str(e)}), 400
