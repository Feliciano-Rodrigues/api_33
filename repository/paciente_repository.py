from sqlalchemy.orm import Session
from entity.paciente import Paciente
from db import db
class PacienteRepository:
    @staticmethod
    def create_paciente(db: Session, paciente_data: dict):
        paciente = Paciente(**paciente_data)
        db.add(paciente)
        db.commit()
        db.refresh(paciente)
        return paciente

    @staticmethod
    def get_paciente_by_id(db: Session, paciente_id: int):
        return db.query(Paciente).filter(Paciente.id == paciente_id).first()

    @staticmethod
    def get_all_pacientes(db: Session):
        return db.query(Paciente).all()

    @staticmethod
    def update_paciente(db: Session, paciente_id: int, updates: dict):
        paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
        if not paciente:
            return None
        for key, value in updates.items():
            setattr(paciente, key, value)
        db.commit()
        db.refresh(paciente)
        return paciente

    @staticmethod
    def delete_paciente(db: Session, paciente_id: int):
        paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
        if not paciente:
            return None
        db.delete(paciente)
        db.commit()
        return paciente