from flask import Blueprint, request, jsonify
from service.agenda_service import AgendaService
from repository.agenda_repository import AgendaRepository

agenda_bp = Blueprint('agenda_controller', __name__)

agenda_service = AgendaService(AgendaRepository())

@agenda_bp.route('/agendas', methods=['POST'])
def criar_agenda():
    dados = request.json
    agenda_service.criar_agenda(dados)
    return jsonify({"mensagem": "Agenda criada com sucesso"}), 201

@agenda_bp.route('/agendas/<int:id_agenda>', methods=['GET'])
def obter_agenda(id_agenda):
    agenda = agenda_service.obter_agenda(id_agenda)
    if agenda:
        return jsonify({
            "id_agenda": agenda.id_agenda,
            "id_consulta": agenda.id_consulta,
            "id_cirurgia": agenda.id_cirurgia,
            "id_veterinario": agenda.id_veterinario,
            "disponibilidade": agenda.disponibilidade,
            "tipo": agenda.tipo,
            "data": agenda.data,
            "hora": agenda.hora
        })
    return jsonify({"erro": "Agenda não encontrada"}), 404

@agenda_bp.route('/agendas', methods=['GET'])
def listar_agendas():
    agendas = agenda_service.listar_agendas()
    return jsonify([{
        "id_agenda": agenda.id_agenda,
        "id_consulta": agenda.id_consulta,
        "id_cirurgia": agenda.id_cirurgia,
        "id_veterinario": agenda.id_veterinario,
        "disponibilidade": agenda.disponibilidade,
        "tipo": agenda.tipo,
        "data": agenda.data,
        "hora": agenda.hora
    } for agenda in agendas])

@agenda_bp.route('/agendas/<int:id_agenda>', methods=['PUT'])
def atualizar_agenda(id_agenda):
    dados = request.json
    agenda_service.atualizar_agenda(id_agenda, dados)
    return jsonify({"mensagem": "Agenda atualizada com sucesso"})

@agenda_bp.route('/agendas/<int:id_agenda>', methods=['DELETE'])
def remover_agenda(id_agenda):
    agenda_service.remover_agenda(id_agenda)
    return jsonify({"mensagem": "Agenda removida com sucesso"})
