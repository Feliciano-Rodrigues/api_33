from flask import Blueprint, request, jsonify
from service.medicamento_service import MedicamentoService

medicamento_bp = Blueprint("medicamento", __name__, url_prefix="/api/v1/medicamentos")

@medicamento_bp.route("/", methods=["POST"])
def criar_medicamento():
    dados = request.json
    medicamento = MedicamentoService.criar(dados)
    return jsonify({"id_medicamento": medicamento.id_medicamento}), 201

@medicamento_bp.route("/", methods=["GET"])
def listar_medicamentos():
    medicamentos = MedicamentoService.listar_todos()
    return jsonify([{"id_medicamento": m.id_medicamento, "nome": m.nome} for m in medicamentos])

@medicamento_bp.route("/<int:id_medicamento>", methods=["DELETE"])
def excluir_medicamento(id_medicamento):
    MedicamentoService.excluir(id_medicamento)
    return jsonify({"message": "Medicamento excluído com sucesso"})
