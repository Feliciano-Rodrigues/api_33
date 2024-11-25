from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from db import db  # Corrigi a importação aqui
from entity.consulta import Consulta
from entity.veterinario import Veterinario
from service.consulta_service import ConsultaService

consulta_bp = Blueprint("consulta", __name__, url_prefix="/api/v1/consultas")

# Rota para criar uma nova consulta
@consulta_bp.route("/register", methods=["POST"])
def create_consulta():
    data = request.json
    try:
        consulta = ConsultaService.create_consulta(db.session, data)
        return jsonify({
            "id": consulta.id,
            "data": consulta.data,
            "descricao": consulta.descricao,
            "veterinario_id": consulta.veterinario_id,
            "paciente_id": consulta.paciente_id
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Rota para obter uma consulta específica pelo ID
@consulta_bp.route("/<int:consulta_id>", methods=["GET"])
def get_consulta(consulta_id):
    try:
        consulta = ConsultaService.get_consulta_by_id(db.session, consulta_id)
        if consulta:
            return jsonify({
                "id": consulta.id,
                "data": consulta.data,
                "descricao": consulta.descricao,
                "veterinario_id": consulta.veterinario_id,
                "paciente_id": consulta.paciente_id
            }), 200
        else:
            return jsonify({"error": "Consulta não encontrada"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


# Rota para obter todas as consultas
@consulta_bp.route("/consultas", methods=["GET"])
def get_all_consultas():
    try:
        consultas = ConsultaService.get_all_consultas(db.session)  # Passe db.session
        result = [
            {
                "id": consulta.id,
                "data": consulta.data,
                "descricao": consulta.descricao,
                "veterinario_id": consulta.veterinario_id,
                "paciente_id": consulta.paciente_id
            }
            for consulta in consultas
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rota para atualizar uma consulta pelo ID
@consulta_bp.route("/update/<int:consulta_id>", methods=["PUT"])
@consulta_bp.route("/update/<int:consulta_id>", methods=["PUT"])
def update_consulta(consulta_id):
    try:
        updates = request.json
        veterinario_id = updates.get("veterinario_id")

        # Verificar se a consulta existe
        consulta = Consulta.query.get(consulta_id)
        if not consulta:
            return jsonify({"error": "Consulta não encontrada"}), 404

        # Verificar se o veterinário existe
        veterinario = Veterinario.query.get(veterinario_id)
        if not veterinario:
            return jsonify({"error": "Veterinário não encontrado"}), 400

        # Atualizar consulta
        consulta.data = updates.get("data", consulta.data)
        consulta.veterinario_id = veterinario_id
        db.session.commit()

        return jsonify({
            "id": consulta.id,
            "data": consulta.data,
            "descricao": consulta.descricao,
            "veterinario_id": consulta.veterinario_id,
            "paciente_id": consulta.paciente_id
        }), 200

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Erro de integridade. Verifique os dados."}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Rota para deletar uma consulta pelo ID
@consulta_bp.route("/delete/<int:consulta_id>", methods=["DELETE"])
def delete_consulta(consulta_id):
    try:
        consulta = ConsultaService.delete_consulta(db.session, consulta_id)  # Passe db.session
        if consulta:
            return jsonify({"message": "Consulta deletada com sucesso."}), 200
        else:
            return jsonify({"error": "Consulta não encontrada"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
