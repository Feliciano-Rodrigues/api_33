from flask import Blueprint, request, jsonify
from service.prescricao_service import PrescricaoService

prescricao_bp = Blueprint("prescricao", __name__, url_prefix="/api/v1/prescricoes")

@prescricao_bp.route("/", methods=["POST"])
def criar_prescricao():
    dados = request.json
    prescricao = PrescricaoService.criar(dados)
    return jsonify({"id_prescricao": prescricao.id_prescricao}), 201

@prescricao_bp.route("/", methods=["GET"])
def listar_prescricoes():
    prescricoes = PrescricaoService.listar_todas()
    return jsonify([{"id_prescricao": p.id_prescricao, "id_consulta": p.id_consulta} for p in prescricoes])

@prescricao_bp.route("/<int:id_prescricao>", methods=["DELETE"])
def excluir_prescricao(id_prescricao):
    PrescricaoService.excluir(id_prescricao)
    return jsonify({"message": "Prescrição excluída com sucesso"})
