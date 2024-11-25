from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from db import db
from service.paciente_service import PacienteService

paciente_bp = Blueprint("paciente", __name__, url_prefix="/api/v1/pacientes")

@paciente_bp.route("/register", methods=["POST"])
def create_paciente():
    
    try:
        data = request.json
        paciente = PacienteService.create_paciente(db, data)
        return jsonify(paciente), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except IntegrityError:
        return jsonify({"error": "Erro de integridade. Verifique os dados enviados."}), 400
    finally:
        db.close()

@paciente_bp.route("/<int:id>", methods=["GET"])
def get_paciente(id):
    
    try:
        paciente = PacienteService.get_paciente_by_id(db, id)
        return jsonify(paciente)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    finally:
        db.close()

@paciente_bp.route("/", methods=["GET"])
def get_all_pacientes():
    
    try:
        pacientes = PacienteService.get_all_pacientes(db)
        return jsonify(pacientes)
    finally:
        db.close()

@paciente_bp.route("/update/<int:id>", methods=["PUT"])
def update_paciente(id):
    
    try:
        updates = request.json
        paciente = PacienteService.update_paciente(db, id, updates)
        return jsonify(paciente)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    finally:
        db.close()

@paciente_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_paciente(id):
    
    try:
        PacienteService.delete_paciente(db, id)
        return jsonify({"message": "Paciente removido com sucesso."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    finally:
        db.close()