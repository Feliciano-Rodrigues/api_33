from flask import Blueprint, request, jsonify
from service.financeiro_service import FinanceiroService
from repository.financeiro_repository import FinanceiroRepository

financeiro_bp = Blueprint('financeiro_controller', __name__)

financeiro_service = FinanceiroService(FinanceiroRepository())

@financeiro_bp.route('/financeiros', methods=['POST'])
def criar_financeiro():
    dados = request.json
    financeiro_service.criar_financeiro(dados)
    return jsonify({"mensagem": "Financeiro criado com sucesso"}), 201

@financeiro_bp.route('/financeiros/<int:id_financeiro>', methods=['GET'])
def obter_financeiro(id_financeiro):
    financeiro = financeiro_service.obter_financeiro(id_financeiro)
    if financeiro:
        return jsonify({
            "id_financeiro": financeiro.id_financeiro,
            "id_consulta": financeiro.id_consulta,
            "id_exame": financeiro.id_exame,
            "id_internamento": financeiro.id_internamento,
            "valor_total": financeiro.valor_total,
            "data_pagamento": financeiro.data_pagamento,
            "forma_pagamento": financeiro.forma_pagamento
        })
    return jsonify({"erro": "Financeiro não encontrado"}), 404

@financeiro_bp.route('/financeiros', methods=['GET'])
def listar_financeiros():
    financeiros = financeiro_service.listar_financeiros()
    return jsonify([{
        "id_financeiro": financeiro.id_financeiro,
        "id_consulta": financeiro.id_consulta,
        "id_exame": financeiro.id_exame,
        "id_internamento": financeiro.id_internamento,
        "valor_total": financeiro.valor_total,
        "data_pagamento": financeiro.data_pagamento,
        "forma_pagamento": financeiro.forma_pagamento
    } for financeiro in financeiros])

@financeiro_bp.route('/financeiros/<int:id_financeiro>', methods=['PUT'])
def atualizar_financeiro(id_financeiro):
    dados = request.json
    financeiro_service.atualizar_financeiro(id_financeiro, dados)
    return jsonify({"mensagem": "Financeiro atualizado com sucesso"})

@financeiro_bp.route('/financeiros/<int:id_financeiro>', methods=['DELETE'])
def remover_financeiro(id_financeiro):
    financeiro_service.remover_financeiro(id_financeiro)
    return jsonify({"mensagem": "Financeiro removido com sucesso"})
