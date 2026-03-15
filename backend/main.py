from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from api import devices, firmware, campaigns

import threading
from mqtt_client.subscriber import start_subscriber


# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="OTA Fleet Manager", version="1.0")

# Enable CORS (needed for Next.js frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(devices.router, prefix="/devices")
app.include_router(firmware.router, prefix="/firmware")
app.include_router(campaigns.router, prefix="/campaigns")


@app.get("/")
def root():
    return {"message": "OTA Backend Running"}


# Start MQTT subscriber when backend starts
@app.on_event("startup")
def start_mqtt():
    threading.Thread(
        target=start_subscriber,
        daemon=True
    ).start()