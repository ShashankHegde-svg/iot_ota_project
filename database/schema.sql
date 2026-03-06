CREATE TABLE devices(
    device_id VARCHAR(50) PRIMARY KEY,
    firmware_version VARCHAR(20) DEFAULT 'v1.0',
    battery_level INT DEFAULT 100,
    network_quality INT DEFAULT 5,
    status VARCHAR(30) DEFAULT 'idle',
    last_seen TIMESTAMP DEFAULT NOW()
);


CREATE TABLE firmware (
    firmware_id  SERIAL PRIMARY KEY,
    version      VARCHAR(20) UNIQUE NOT NULL,
    file_path    VARCHAR(255),
    created_at   TIMESTAMP DEFAULT NOW()
);

CREATE TABLE campaigns (
    campaign_id    SERIAL PRIMARY KEY,
    firmware_id    INT REFERENCES firmware(firmware_id),
    batch_size     INT DEFAULT 10,
    status         VARCHAR(30) DEFAULT 'pending',
    started_at     TIMESTAMP DEFAULT NOW()
);

CREATE TABLE update_logs (
    log_id       SERIAL PRIMARY KEY,
    device_id    VARCHAR(50) REFERENCES devices(device_id),
    campaign_id  INT REFERENCES campaigns(campaign_id),
    status       VARCHAR(30),
    progress     INT DEFAULT 0,
    reason       VARCHAR(100),
    updated_at   TIMESTAMP DEFAULT NOW()
);
