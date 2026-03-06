import threading
import time
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from device_script import TCUDevice


def start_device(device_id):

    device = TCUDevice(device_id)

    device.start()


if __name__ == "__main__":

    num_devices = int(sys.argv[1]) if len(sys.argv) > 1 else 30

    print(f"Starting {num_devices} simulated devices...")

    threads = []

    for i in range(1, num_devices + 1):

        device_id = f"car_{str(i).zfill(3)}"

        t = threading.Thread(
            target=start_device,
            args=(device_id,),
            daemon=True
        )

        threads.append(t)

        t.start()

        time.sleep(0.1)

    print("All devices running. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down devices...")