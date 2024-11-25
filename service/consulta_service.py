from sqlalchemy.orm import Session
from entity.paciente import Paciente
from entity.veterinario import Veterinario
from repository.consulta_repository import ConsultaRepository

class ConsultaService:
    
    @staticmethod
    def create_consulta(db, consulta_data):
        veterinario_id = consulta_data.get("veterinario_id")
        paciente_id = consulta_data.get("paciente_id")

        # Validação no service
        veterinario = Veterinario.query.get(veterinario_id)
        if not veterinario:
            raise ValueError(f"Veterinário com ID {veterinario_id} não encontrado")

        paciente = Paciente.query.get(paciente_id)
        if not paciente:
            raise ValueError(f"Paciente com ID {paciente_id} não encontrado")

        return ConsultaRepository.create_consulta(db, consulta_data)
        if not consulta:
            raise ValueError("Consulta não encontrada.")
        return consulta

    @staticmethod
    def get_all_consultas(db: Session):
        # Chama o repositório para obter todas as consultas
        return ConsultaRepository.get_all_consultas(db)

    @staticmethod
    def update_consulta(db: Session, consulta_id: int, updates: dict):
        # Chama o repositório para atualizar a consulta
        consulta = ConsultaRepository.update_consulta(db, consulta_id, updates)
        if not consulta:
            raise ValueError("Consulta não encontrada para atualização.")
        return consulta

    @staticmethod
    def delete_consulta(db: Session, consulta_id: int):
        # Chama o repositório para deletar a consulta
        consulta = ConsultaRepository.delete_consulta(db, consulta_id)
        if not consulta:
            raise ValueError("Consulta não encontrada para exclusão.")
        return consulta
    
    @staticmethod
    def get_consulta_by_id(db: Session, consulta_id: int):
        consulta = ConsultaRepository.get_consulta_by_id(db, consulta_id)
        if not consulta:
            raise ValueError("Consulta não encontrada.")
        return consulta
