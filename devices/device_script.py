import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "localhost"
PORT = 1883


class TCUDevice:

    def __init__(self, device_id: str):

        self.device_id = device_id
        self.battery_level = random.randint(10, 100)
        self.network_quality = random.randint(1, 5)
        self.firmware = "v1.0"

        self.client = mqtt.Client(client_id=device_id)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        print(
            f"[{self.device_id}] Battery:{self.battery_level}% "
            f"Network:{self.network_quality}/5"
        )

    def on_connect(self, client, userdata, flags, rc):

        topic = f"fleet/update/{self.device_id}"

        self.client.subscribe(topic)

        print(
            f"[{self.device_id}] Connected. "
            f"Subscribed to {topic}"
        )

    def on_message(self, client, userdata, msg):

        data = json.loads(msg.payload.decode())

        print(
            f"[{self.device_id}] Received update command: {data}"
        )

        self.simulate_update(
            data.get("campaign_id"),
            data.get("firmware", "v2.0")
        )

    def publish_status(
        self,
        status,
        progress=0,
        reason=None,
        firmware=None,
        campaign_id=None
    ):

        payload = {
            "device_id": self.device_id,
            "status": status,
            "progress": progress,
            "campaign_id": campaign_id
        }

        if reason:
            payload["reason"] = reason

        if firmware:
            payload["firmware"] = firmware

        topic = f"fleet/status/{self.device_id}"

        self.client.publish(topic, json.dumps(payload))

    def simulate_update(self, campaign_id, target_fw):

        # Battery check
        if self.battery_level < 20:

            print(
                f"[{self.device_id}] FAILED battery too low"
            )

            self.publish_status(
                "failed",
                reason="low_battery",
                campaign_id=campaign_id
            )

            return

        # Network check
        if self.network_quality < 2:

            if random.random() < 0.7:

                print(
                    f"[{self.device_id}] FAILED poor network"
                )

                self.publish_status(
                    "failed",
                    reason="poor_network",
                    campaign_id=campaign_id
                )

                return

        # Download simulation
        for pct in [10, 20, 40, 60, 80, 100]:

            self.publish_status(
                "downloading",
                progress=pct,
                campaign_id=campaign_id
            )

            time.sleep(random.uniform(0.5, 1.5))

        # Installation simulation
        self.publish_status(
            "installing",
            progress=100,
            campaign_id=campaign_id
        )

        time.sleep(random.uniform(1, 2))

        if random.random() < 0.05:

            self.publish_status(
                "failed",
                reason="install_error",
                campaign_id=campaign_id
            )

            return

        self.firmware = target_fw

        print(
            f"[{self.device_id}] SUCCESS updated to {target_fw}"
        )

        self.publish_status(
            "success",
            progress=100,
            firmware=target_fw,
            campaign_id=campaign_id
        )

    def start(self):

        self.client.connect(BROKER, PORT)

        self.client.loop_forever()