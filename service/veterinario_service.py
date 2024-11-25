from sqlalchemy.orm import Session
from repository.veterinario_repository import VeterinarioRepository

class VeterinarioService:
    @staticmethod
    def create_veterinario(db: Session, veterinario_data: dict):
        if not veterinario_data.get("crm"):
            raise ValueError("CRM é obrigatório.")
        if not veterinario_data.get("especialidade"):
            raise ValueError("Especialidade é obrigatória.")
        return VeterinarioRepository.create_veterinario(db, veterinario_data)

    @staticmethod
    def get_veterinario_by_id(db: Session, veterinario_id: int):
        veterinario = VeterinarioRepository.get_veterinario_by_id(db, veterinario_id)
        if not veterinario:
            raise ValueError("Veterinário não encontrado.")
        return veterinario

    @staticmethod
    def get_all_veterinarios(db: Session):
        return VeterinarioRepository.get_all_veterinarios(db)

    @staticmethod
    def update_veterinario(db: Session, veterinario_id: int, updates: dict):
        veterinario = VeterinarioRepository.update_veterinario(db, veterinario_id, updates)
        if not veterinario:
            raise ValueError("Veterinário não encontrado para atualização.")
        return veterinario

    @staticmethod
    def delete_veterinario(db: Session, veterinario_id: int):
        veterinario = VeterinarioRepository.delete_veterinario(db, veterinario_id)
        if not veterinario:
            raise ValueError("Veterinário não encontrado para exclusão.")
        return veterinario