import sqlite3
from pathlib import Path

DB_PATH = Path("data/warehouse/app.db")
SCHEMA_PATH = Path("sql/schema.sql")


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()


def log_event(user_id: str, event_type: str, payload_json: str | None = None):
    conn = get_connection()
    conn.execute(
        "INSERT INTO events (user_id, event_type, payload_json) VALUES (?, ?, ?)",
        (user_id, event_type, payload_json),
    )
    conn.commit()
    conn.close()
