from sqlalchemy.orm import Session
from entity.veterinario import Veterinario
from db import db
class VeterinarioRepository:
    @staticmethod
    def create_veterinario(db: Session, veterinario_data: dict):
        veterinario = Veterinario(**veterinario_data)
        db.add(veterinario)
        db.commit()
        db.refresh(veterinario)
        return veterinario

    @staticmethod
    def get_veterinario_by_id(db: Session, veterinario_id: int):
        return db.query(Veterinario).filter(Veterinario.id == veterinario_id).first()

    @staticmethod
    def get_all_veterinarios(db: Session):
        return db.query(Veterinario).all()

    @staticmethod
    def update_veterinario(db: Session, veterinario_id: int, updates: dict):
        veterinario = db.query(Veterinario).filter(Veterinario.id == veterinario_id).first()
        if not veterinario:
            return None
        for key, value in updates.items():
            setattr(veterinario, key, value)
        db.commit()
        db.refresh(veterinario)
        return veterinario

    @staticmethod
    def delete_veterinario(db: Session, veterinario_id: int):
        veterinario = db.query(Veterinario).filter(Veterinario.id == veterinario_id).first()
        if not veterinario:
            return None
        db.delete(veterinario)
        db.commit()
        return veterinario