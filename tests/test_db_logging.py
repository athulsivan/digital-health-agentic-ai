from src.coach_agent.db import init_db, log_event, get_connection


def test_log_event():
    init_db()
    log_event("test_user", "test_event", '{"ok": true}')

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM events")
    count = cur.fetchone()[0]
    conn.close()

    assert count >= 1
