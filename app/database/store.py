import sqlite3
import json

DB = "bank.db"

def save_workflow(workflow_id, intent, execution_result):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO workflows
    (workflow_id, intent, status, steps)
    VALUES (?, ?, ?, ?)
    """, (
        workflow_id,
        json.dumps(intent),
        execution_result["status"],
        json.dumps(execution_result["steps"])
    ))

    conn.commit()
    conn.close()