from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from database import get_db
from models.models import Firmware
import shutil, os

router = APIRouter()

FIRMWARE_DIR = "./firmware/"


@router.get("/")
def list_firmware(db: Session = Depends(get_db)):
    return db.query(Firmware).all()


@router.post("/upload")
async def upload_firmware(version: str,
                          file: UploadFile = File(...),
                          db: Session = Depends(get_db)):

    os.makedirs(FIRMWARE_DIR, exist_ok=True)

    path = os.path.join(FIRMWARE_DIR, file.filename)

    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    fw = Firmware(version=version, file_path=path)

    db.add(fw)
    db.commit()
    db.refresh(fw)

    return fw