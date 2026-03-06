import paho.mqtt.client as mqtt
import json

BROKER = "localhost"
PORT = 1883


def send_update_command(device_id: str, campaign_id: int):

    client = mqtt.Client()
    client.connect(BROKER, PORT)

    topic = f"fleet/update/{device_id}"

    payload = json.dumps({
        "campaign_id": campaign_id,
        "firmware": "v2.0"
    })

    client.publish(topic, payload)

    client.disconnect()