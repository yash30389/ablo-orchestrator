from fastapi import FastAPI, HTTPException, Header
from ablo.workflows.orchestrator import Orchestrator
from ablo.core.auth import AuthManager

app = FastAPI()
orchestrator = Orchestrator()
auth = AuthManager()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/orchestrate")
def orchestrate(payload: dict, tenant_id: str = Header(...), username: str = Header(...)):
    # 1️⃣ Check RBAC / tenant
    if not auth.check_permission(tenant_id, username, "execute_workflow"):
        raise HTTPException(status_code=403, detail="Forbidden")

    # 2️⃣ Extract intent
    intent = payload.get("intent")
    if not intent:
        raise HTTPException(status_code=400, detail="Intent is required")

    # 3️⃣ Run orchestrator
    return orchestrator.run(intent)
