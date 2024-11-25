from flask import Blueprint, request, jsonify
from service.auxiliar_veterinario_service import AuxiliarVeterinarioService
from repository.auxiliar_veterinario_repository import AuxiliarVeterinarioRepository

auxiliar_veterinario_bp = Blueprint('auxiliar_veterinario_controller', __name__)

auxiliar_veterinario_service = AuxiliarVeterinarioService(AuxiliarVeterinarioRepository())

@auxiliar_veterinario_bp.route('/auxiliares-veterinarios', methods=['POST'])
def criar_auxiliar_veterinario():
    dados = request.json
    auxiliar_veterinario_service.criar_auxiliar_veterinario(dados)
    return jsonify({"mensagem": "Auxiliar veterinário criado com sucesso"}), 201

@auxiliar_veterinario_bp.route('/auxiliares-veterinarios/<int:id_funcionario>', methods=['GET'])
def obter_auxiliar_veterinario(id_funcionario):
    auxiliar_veterinario = auxiliar_veterinario_service.obter_auxiliar_veterinario(id_funcionario)
    if auxiliar_veterinario:
        return jsonify({
            "id_funcionario": auxiliar_veterinario.id_funcionario,
            "registro_profissional": auxiliar_veterinario.registro_profissional,
            "setor_trabalho": auxiliar_veterinario.setor_trabalho,
            "data_contratacao": auxiliar_veterinario.data_contratacao
        })
    return jsonify({"erro": "Auxiliar veterinário não encontrado"}), 404

@auxiliar_veterinario_bp.route('/auxiliares-veterinarios', methods=['GET'])
def listar_auxiliares_veterinarios():
    auxiliares_veterinarios = auxiliar_veterinario_service.listar_auxiliares_veterinarios()
    return jsonify([{
        "id_funcionario": auxiliar_veterinario.id_funcionario,
        "registro_profissional": auxiliar_veterinario.registro_profissional,
        "setor_trabalho": auxiliar_veterinario.setor_trabalho,
        "data_contratacao": auxiliar_veterinario.data_contratacao
    } for auxiliar_veterinario in auxiliares_veterinarios])

@auxiliar_veterinario_bp.route('/auxiliares-veterinarios/<int:id_funcionario>', methods=['PUT'])
def atualizar_auxiliar_veterinario(id_funcionario):
    dados = request.json
    auxiliar_veterinario_service.atualizar_auxiliar_veterinario(id_funcionario, dados)
    return jsonify({"mensagem": "Auxiliar veterinário atualizado com sucesso"})

@auxiliar_veterinario_bp.route('/auxiliares-veterinarios/<int:id_funcionario>', methods=['DELETE'])
def remover_auxiliar_veterinario(id_funcionario):
    auxiliar_veterinario_service.remover_auxiliar_veterinario(id_funcionario)
    return jsonify({"mensagem": "Auxiliar veterinário removido com sucesso"})
