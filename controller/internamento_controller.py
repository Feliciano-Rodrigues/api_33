from flask import Blueprint, request, jsonify
from service.internamento_service import InternamentoService
from repository.internamento_repository import InternamentoRepository

internamento_bp = Blueprint('internamento_controller', __name__)

internamento_service = InternamentoService(InternamentoRepository())

@internamento_bp.route('/internamentos', methods=['POST'])
def criar_internamento():
    dados = request.json
    internamento_service.criar_internamento(dados)
    return jsonify({"mensagem": "Internamento criado com sucesso"}), 201

@internamento_bp.route('/internamentos/<int:id_internamento>', methods=['GET'])
def obter_internamento(id_internamento):
    internamento = internamento_service.obter_internamento(id_internamento)
    if internamento:
        return jsonify({
            "id_internamento": internamento.id_internamento,
            "id_paciente": internamento.id_paciente,
            "id_veterinario": internamento.id_veterinario,
            "data_internacao": internamento.data_internacao,
            "motivo": internamento.motivo,
            "data_alta": internamento.data_alta,
            "valor_diaria": internamento.valor_diaria,
            "id_prescricao": internamento.id_prescricao
        })
    return jsonify({"erro": "Internamento não encontrado"}), 404

@internamento_bp.route('/internamentos', methods=['GET'])
def listar_internamentos():
    internamentos = internamento_service.listar_internamentos()
    return jsonify([{
        "id_internamento": internamento.id_internamento,
        "id_paciente": internamento.id_paciente,
        "id_veterinario": internamento.id_veterinario,
        "data_internacao": internamento.data_internacao,
        "motivo": internamento.motivo,
        "data_alta": internamento.data_alta,
        "valor_diaria": internamento.valor_diaria,
        "id_prescricao": internamento.id_prescricao
    } for internamento in internamentos])

@internamento_bp.route('/internamentos/<int:id_internamento>', methods=['PUT'])
def atualizar_internamento(id_internamento):
    dados = request.json
    internamento_service.atualizar_internamento(id_internamento, dados)
    return jsonify({"mensagem": "Internamento atualizado com sucesso"})

@internamento_bp.route('/internamentos/<int:id_internamento>', methods=['DELETE'])
def remover_internamento(id_internamento):
    internamento_service.remover_internamento(id_internamento)
    return jsonify({"mensagem": "Internamento removido com sucesso"})
