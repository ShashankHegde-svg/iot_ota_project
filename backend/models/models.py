from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from database import Base


class Device(Base):
    __tablename__ = "devices"

    device_id = Column(String, primary_key=True)
    firmware_version = Column(String, default="v1.0")
    battery_level = Column(Integer, default=100)
    network_quality = Column(Integer, default=5)
    status = Column(String, default="idle")
    last_seen = Column(DateTime, default=func.now())


class Firmware(Base):
    __tablename__ = "firmware"

    firmware_id = Column(Integer, primary_key=True, autoincrement=True)
    version = Column(String, unique=True, nullable=False)
    file_path = Column(String)
    created_at = Column(DateTime, default=func.now())


class Campaign(Base):
    __tablename__ = "campaigns"

    campaign_id = Column(Integer, primary_key=True, autoincrement=True)
    firmware_id = Column(Integer, ForeignKey("firmware.firmware_id"))
    batch_size = Column(Integer, default=10)
    status = Column(String, default="pending")
    started_at = Column(DateTime, default=func.now())


class UpdateLog(Base):
    __tablename__ = "update_logs"

    log_id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String, ForeignKey("devices.device_id"))
    campaign_id = Column(Integer, ForeignKey("campaigns.campaign_id"))
    status = Column(String)
    progress = Column(Integer, default=0)
    reason = Column(String)
    updated_at = Column(DateTime, default=func.now())