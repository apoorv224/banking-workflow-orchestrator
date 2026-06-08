from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard():

    return """
<!DOCTYPE html>
<html>
<head>
    <title>Elite Workflow Dashboard</title>

    <style>
        body { margin:0; font-family:Arial; background:#0b1220; color:white; }

        .grid {
            display:grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap:10px;
            padding:10px;
        }

        .card {
            background:#111827;
            padding:10px;
            border-radius:10px;
            height:95vh;
            overflow:auto;
        }

        button {
            padding:8px;
            border:none;
            border-radius:6px;
            cursor:pointer;
        }

        .primary { background:#22c55e; }
        .blue { background:#3b82f6; color:white; }
        .yellow { background:#f59e0b; }

        input {
            width:90%;
            padding:8px;
            margin-bottom:10px;
        }

        pre {
            background:black;
            padding:10px;
            font-size:12px;
        }

        .item {
            background:#1f2937;
            padding:8px;
            margin:5px 0;
            border-radius:6px;
            cursor:pointer;
        }

        .item:hover { background:#374151; }
    </style>
</head>

<body>

<h2 style="padding:10px;">🏦 ELITE BANKING ORCHESTRATOR</h2>

<div class="grid">

<!-- RUN -->
<div class="card">
    <h3>Run Workflow</h3>
    <input id="input" placeholder="apply for loan / open account" />
    <button class="primary" onclick="run()">Run</button>
    <pre id="run"></pre>
</div>

<!-- WORKFLOWS -->
<div class="card">
    <h3>Workflows</h3>
    <button class="blue" onclick="load()">Refresh</button>
    <div id="list"></div>
</div>

<!-- DETAILS -->
<div class="card">
    <h3>Details</h3>
    <div id="details"></div>

    <h3>Audit</h3>
    <button class="blue" onclick="audit()">Load</button>
    <pre id="audit"></pre>
</div>

</div>

<script>

let selected = null;

// -------- RUN --------
async function run(){
    const input = document.getElementById("input").value;

    const res = await fetch("/api/workflow/run", {
        method:"POST",
        headers:{ "Content-Type":"application/json" },
        body: JSON.stringify({ user_input: input })
    });

    const data = await res.json();
    document.getElementById("run").innerText = JSON.stringify(data,null,2);

    load();
}

// -------- LOAD WORKFLOWS --------
async function load(){
    const res = await fetch("/api/audit");
    const logs = await res.json();

    const list = document.getElementById("list");
    list.innerHTML = "";

    logs.forEach(l => {
        if(!l.data.workflow_id) return;

        const div = document.createElement("div");
        div.className = "item";

        div.innerHTML = `
            <b>${l.data.workflow_id}</b><br/>
            ${l.event_type}
        `;

        div.onclick = ()=> openWorkflow(l.data.workflow_id);
        list.appendChild(div);
    });
}

// -------- DETAILS --------
async function openWorkflow(id){
    selected = id;

    const res = await fetch("/api/workflow/" + id);
    const data = await res.json();

    let html = "<pre>" + JSON.stringify(data,null,2) + "</pre>";

    if(data.status === "WAITING_FOR_APPROVAL"){
        html += `<button class="yellow" onclick="approve()">APPROVE</button>`;
    }

    document.getElementById("details").innerHTML = html;
}

// -------- APPROVE --------
async function approve(){
    const res = await fetch("/api/workflow/" + selected + "/approve", {
        method:"POST"
    });

    const data = await res.json();
    document.getElementById("details").innerHTML =
        "<pre>"+JSON.stringify(data,null,2)+"</pre>";
}

// -------- AUDIT --------
async function audit(){
    const res = await fetch("/api/audit");
    const data = await res.json();

    document.getElementById("audit").innerText =
        JSON.stringify(data,null,2);
}

load();

</script>

</body>
</html>
"""