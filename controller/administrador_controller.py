from flask import Blueprint, request, jsonify
from service.administrador_service import AdministradorService
from repository.administrador_repository import AdministradorRepository

administrador_bp = Blueprint('administrador_controller', __name__)

administrador_service = AdministradorService(AdministradorRepository())

@administrador_bp.route('/administradores', methods=['POST'])
def criar_administrador():
    dados = request.json
    administrador_service.criar_administrador(dados)
    return jsonify({"mensagem": "Administrador criado com sucesso"}), 201

@administrador_bp.route('/administradores/<int:id_funcionario>', methods=['GET'])
def obter_administrador(id_funcionario):
    administrador = administrador_service.obter_administrador(id_funcionario)
    if administrador:
        return jsonify({
            "id_funcionario": administrador.id_funcionario,
            "responsabilidade": administrador.responsabilidade,
            "data_contratacao": administrador.data_contratacao
        })
    return jsonify({"erro": "Administrador não encontrado"}), 404

@administrador_bp.route('/administradores', methods=['GET'])
def listar_administradores():
    administradores = administrador_service.listar_administradores()
    return jsonify([{
        "id_funcionario": administrador.id_funcionario,
        "responsabilidade": administrador.responsabilidade,
        "data_contratacao": administrador.data_contratacao
    } for administrador in administradores])

@administrador_bp.route('/administradores/<int:id_funcionario>', methods=['PUT'])
def atualizar_administrador(id_funcionario):
    dados = request.json
    administrador_service.atualizar_administrador(id_funcionario, dados)
    return jsonify({"mensagem": "Administrador atualizado com sucesso"})

@administrador_bp.route('/administradores/<int:id_funcionario>', methods=['DELETE'])
def remover_administrador(id_funcionario):
    administrador_service.remover_administrador(id_funcionario)
    return jsonify({"mensagem": "Administrador removido com sucesso"})
