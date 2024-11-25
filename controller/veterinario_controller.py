from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from db import db
from service.veterinario_service import VeterinarioService

veterinario_bp = Blueprint("veterinario", __name__, url_prefix="/api/v1/veterinarios")

@veterinario_bp.route("/register", methods=["POST"])
def create_veterinario():
    
    try:
        data = request.json
        veterinario = VeterinarioService.create_veterinario(db, data)
        return jsonify(veterinario), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except IntegrityError:
        return jsonify({"error": "Erro de integridade. Verifique os dados enviados."}), 400
    finally:
        db.close()

@veterinario_bp.route("/<int:id>", methods=["GET"])
def get_veterinario(id):
    
    try:
        veterinario = VeterinarioService.get_veterinario_by_id(db, id)
        return jsonify(veterinario)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    finally:
        db.close()

@veterinario_bp.route("/", methods=["GET"])
def get_all_veterinarios():
    
    try:
        veterinarios = VeterinarioService.get_all_veterinarios(db)
        return jsonify(veterinarios)
    finally:
        db.close()

@veterinario_bp.route("/update/<int:id>", methods=["PUT"])
def update_veterinario(id):
    
    try:
        updates = request.json
        veterinario = VeterinarioService.update_veterinario(db, id, updates)
        return jsonify(veterinario)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    finally:
        db.close()

@veterinario_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_veterinario(id):
    
    try:
        VeterinarioService.delete_veterinario(db, id)
        return jsonify({"message": "Veterinário removido com sucesso."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    finally:
        db.close()