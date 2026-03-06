from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models.models import Campaign

router = APIRouter()


class CampaignCreate(BaseModel):
    firmware_id: int
    batch_size: int = 10


@router.post("/")
def create_campaign(payload: CampaignCreate,
                    db: Session = Depends(get_db)):

    campaign = Campaign(
        firmware_id=payload.firmware_id,
        batch_size=payload.batch_size,
        status="running"
    )

    db.add(campaign)
    db.commit()
    db.refresh(campaign)

    return campaign