from sqlalchemy.orm import Session
from entity.consulta import Consulta
from db import db
class ConsultaRepository:
    @staticmethod
    def create_consulta(db: Session, consulta_data: dict):
        consulta = Consulta(**consulta_data)
        db.add(consulta)
        db.commit()
        db.refresh(consulta)
        return consulta

    @staticmethod
    def get_consulta_by_id(db: Session, consulta_id: int):
        return db.query(Consulta).filter(Consulta.id == consulta_id).first()

    @staticmethod
    def get_all_consultas(db: Session):
        return db.query(Consulta).all()

    @staticmethod
    def update_consulta(db: Session, consulta_id: int, updates: dict):
        consulta = db.query(Consulta).filter(Consulta.id == consulta_id).first()
        if not consulta:
            return None
        for key, value in updates.items():
            setattr(consulta, key, value)
        db.commit()
        db.refresh(consulta)
        return consulta

    @staticmethod
    def delete_consulta(db: Session, consulta_id: int):
        consulta = db.query(Consulta).filter(Consulta.id == consulta_id).first()
        if not consulta:
            return None
        db.delete(consulta)
        db.commit()
        return consulta