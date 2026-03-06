import paho.mqtt.client as mqtt
import json

from database import SessionLocal
from models.models import Device, UpdateLog


def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())

    db = SessionLocal()

    device = db.query(Device).filter(
        Device.device_id == data["device_id"]
    ).first()

    if device:

        if data["status"] == "success":
            device.firmware_version = data.get(
                "firmware", device.firmware_version
            )

        db.commit()

        log = UpdateLog(
            device_id=data["device_id"],
            campaign_id=data.get("campaign_id"),
            status=data["status"],
            progress=data.get("progress", 0),
            reason=data.get("reason")
        )

        db.add(log)
        db.commit()

    db.close()


def start_subscriber():

    client = mqtt.Client()

    client.on_message = on_message

    client.connect("localhost", 1883)

    client.subscribe("fleet/status/+")

    client.loop_forever()