from sqlalchemy.orm import Session
from repository.paciente_repository import PacienteRepository

class PacienteService:
    @staticmethod
    def create_paciente(db: Session, paciente_data: dict):
        if not paciente_data.get("cliente_id"):
            raise ValueError("Cliente associado é obrigatório.")
        return PacienteRepository.create_paciente(db, paciente_data)

    @staticmethod
    def get_paciente_by_id(db: Session, paciente_id: int):
        paciente = PacienteRepository.get_paciente_by_id(db, paciente_id)
        if not paciente:
            raise ValueError("Paciente não encontrado.")
        return paciente

    @staticmethod
    def get_all_pacientes(db: Session):
        return PacienteRepository.get_all_pacientes(db)

    @staticmethod
    def update_paciente(db: Session, paciente_id: int, updates: dict):
        paciente = PacienteRepository.update_paciente(db, paciente_id, updates)
        if not paciente:
            raise ValueError("Paciente não encontrado para atualização.")
        return paciente

    @staticmethod
    def delete_paciente(db: Session, paciente_id: int):
        paciente = PacienteRepository.delete_paciente(db, paciente_id)
        if not paciente:
            raise ValueError("Paciente não encontrado para exclusão.")
        return paciente