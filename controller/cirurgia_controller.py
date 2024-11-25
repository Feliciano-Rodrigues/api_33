from flask import Blueprint, request, jsonify
from service.cirurgia_service import CirurgiaService
from repository.cirurgia_repoditory import CirurgiaRepository

cirurgia_bp = Blueprint('cirurgia_controller', __name__)

cirurgia_service = CirurgiaService(CirurgiaRepository())

@cirurgia_bp.route('/cirurgias', methods=['POST'])
def criar_cirurgia():
    dados = request.json
    cirurgia_service.criar_cirurgia(dados)
    return jsonify({"mensagem": "Cirurgia criada com sucesso"}), 201

@cirurgia_bp.route('/cirurgias/<int:id_cirurgia>', methods=['GET'])
def obter_cirurgia(id_cirurgia):
    cirurgia = cirurgia_service.obter_cirurgia(id_cirurgia)
    if cirurgia:
        return jsonify({
            "id_cirurgia": cirurgia.id_cirurgia,
            "id_veterinario": cirurgia.id_veterinario,
            "id_paciente": cirurgia.id_paciente,
            "data_cirurgia": cirurgia.data_cirurgia,
            "hora_inicio": cirurgia.hora_inicio,
            "hora_fim": cirurgia.hora_fim,
            "tipo_cirurgia": cirurgia.tipo_cirurgia,
            "observacoes": cirurgia.observacoes,
            "id_auxiliar": cirurgia.id_auxiliar,
            "valor_cirurgia": cirurgia.valor_cirurgia
        })
    return jsonify({"erro": "Cirurgia não encontrada"}), 404

@cirurgia_bp.route('/cirurgias', methods=['GET'])
def listar_cirurgias():
    cirurgias = cirurgia_service.listar_cirurgias()
    return jsonify([{
        "id_cirurgia": cirurgia.id_cirurgia,
        "id_veterinario": cirurgia.id_veterinario,
        "id_paciente": cirurgia.id_paciente,
        "data_cirurgia": cirurgia.data_cirurgia,
        "hora_inicio": cirurgia.hora_inicio,
        "hora_fim": cirurgia.hora_fim,
        "tipo_cirurgia": cirurgia.tipo_cirurgia,
        "observacoes": cirurgia.observacoes,
        "id_auxiliar": cirurgia.id_auxiliar,
        "valor_cirurgia": cirurgia.valor_cirurgia
    } for cirurgia in cirurgias])

@cirurgia_bp.route('/cirurgias/<int:id_cirurgia>', methods=['PUT'])
def atualizar_cirurgia(id_cirurgia):
    dados = request.json
    cirurgia_service.atualizar_cirurgia(id_cirurgia, dados)
    return jsonify({"mensagem": "Cirurgia atualizada com sucesso"})

@cirurgia_bp.route('/cirurgias/<int:id_cirurgia>', methods=['DELETE'])
def remover_cirurgia(id_cirurgia):
    cirurgia_service.remover_cirurgia(id_cirurgia)
    return jsonify({"mensagem": "Cirurgia removida com sucesso"})
