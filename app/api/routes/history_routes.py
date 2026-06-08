from fastapi import APIRouter
import sqlite3
import json

router = APIRouter()

DB = "bank.db"


@router.get("/workflows")
def get_all_workflows():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT workflow_id, intent, status, steps FROM workflows")
    rows = cur.fetchall()

    conn.close()

    return [
        {
            "workflow_id": r[0],
            "intent": json.loads(r[1]),
            "status": r[2],
            "steps": json.loads(r[3])
        }
        for r in rows
    ]


@router.get("/workflow/{workflow_id}")
def get_workflow(workflow_id: str):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "SELECT workflow_id, intent, status, steps FROM workflows WHERE workflow_id = ?",
        (workflow_id,)
    )

    row = cur.fetchone()
    conn.close()

    if not row:
        return {"error": "not found"}

    return {
        "workflow_id": row[0],
        "intent": json.loads(row[1]),
        "status": row[2],
        "steps": json.loads(row[3])
    }