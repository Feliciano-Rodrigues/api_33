from flask import Blueprint, request, jsonify
from service.exame_service import ExameService
from repository.exame_repository import ExameRepository
from db import db

# Inicializando o Blueprint
exame_bp = Blueprint("exame_controller", __name__)

# Inicializando a sessão e os serviços
repository = ExameRepository(db.session)
service = ExameService(repository)

@exame_bp.route("/exames", methods=["POST"])
def criar_exame():
    """Cria um novo exame."""
    dados = request.json
    exame = service.criar_exame(dados)
    return jsonify({"id": exame.id_exame, "mensagem": "Exame criado com sucesso"}), 201

@exame_bp.route("/exames/<int:id_exame>", methods=["GET"])
def obter_exame(id_exame):
    """Obtém um exame pelo ID."""
    exame = service.obter_exame(id_exame)
    if exame:
        return jsonify({
            "id_exame": exame.id_exame,
            "id_consulta": exame.id_consulta,
            "tipo_exame": exame.tipo_exame,
            "data_exame": exame.data_exame,
            "resultado": exame.resultado,
            "valor_exame": exame.valor_exame
        })
    return jsonify({"erro": "Exame não encontrado"}), 404

@exame_bp.route("/exames", methods=["GET"])
def listar_exames():
    """Lista todos os exames."""
    exames = service.listar_exames()
    return jsonify([
        {
            "id_exame": exame.id_exame,
            "id_consulta": exame.id_consulta,
            "tipo_exame": exame.tipo_exame,
            "data_exame": exame.data_exame,
            "resultado": exame.resultado,
            "valor_exame": exame.valor_exame
        }
        for exame in exames
    ])

@exame_bp.route("/exames/<int:id_exame>", methods=["PUT"])
def atualizar_exame(id_exame):
    """Atualiza os dados de um exame."""
    dados = request.json
    exame = service.atualizar_exame(id_exame, dados)
    if exame:
        return jsonify({"mensagem": "Exame atualizado com sucesso"})
    return jsonify({"erro": "Exame não encontrado"}), 404

@exame_bp.route("/exames/<int:id_exame>", methods=["DELETE"])
def remover_exame(id_exame):
    """Remove um exame pelo ID."""
    if service.remover_exame(id_exame):
        return jsonify({"mensagem": "Exame removido com sucesso"})
    return jsonify({"erro": "Exame não encontrado"}), 404
