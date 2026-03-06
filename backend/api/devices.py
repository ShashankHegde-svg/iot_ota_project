from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.models import Device

router = APIRouter()


@router.get("/")
def get_all_devices(db: Session = Depends(get_db)):
    return db.query(Device).all()


@router.get("/{device_id}")
def get_device(device_id: str, db: Session = Depends(get_db)):
    return db.query(Device).filter(Device.device_id == device_id).first()


@router.post("/retry/{device_id}")
def retry_device(device_id: str, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.device_id == device_id).first()

    if device:
        device.status = "idle"
        db.commit()

    return {"message": f"Device {device_id} queued for retry"}