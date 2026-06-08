from .db import get_connection
def init_db():
    print("🔧 Initializing SQLite DB...")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workflows (
        workflow_id TEXT PRIMARY KEY,
        status TEXT,
        intent TEXT,
        steps TEXT DEFAULT '[]'
    )
    """)

    conn.commit()
    conn.close()

    print("✅ DB ready")