from fastapi import FastAPI, HTTPException
from .domain import RouteRequest, RatioRequest, FitmentInput, DiagnosticPlanRequest, AskRequest
from .router import route
from .fitment import evaluate
from .diagnostics import build_plan
from .kb import KnowledgeBase
from .orchestrator import Orchestrator

app = FastAPI(title="XTZ125K Supreme Agent", version="0.1.0")
kb = KnowledgeBase()
agent = Orchestrator()

@app.get("/health")
def health():
    return {"status":"ok","vehicle":"XTZ125K 2014 / 21DE"}

@app.get("/v1/baseline")
def baseline():
    return kb.baseline

@app.get("/v1/parts/{part_number}")
def part(part_number: str):
    rows = kb.part(part_number)
    if not rows:
        raise HTTPException(404, "Part number not found in local canonical core")
    return rows

@app.post("/v1/route")
def route_endpoint(req: RouteRequest):
    return {"mode":route(req.text)}

@app.post("/v1/ratio")
def ratio(req: RatioRequest):
    oem = 48/14
    new = req.rear_teeth/req.front_teeth
    return {
        "ratio":round(new,4),
        "delta_vs_oem_percent":round((new/oem-1)*100,2),
        "interpretation":"positive = shorter/more wheel torque; negative = taller/lower cruise rpm",
    }

@app.post("/v1/fitment")
def fitment(req: FitmentInput):
    return evaluate(req)

@app.post("/v1/diagnostic-plan")
def diagnostic(req: DiagnosticPlanRequest):
    return {"symptom":req.symptom, "tests":build_plan(req)}

@app.post("/v1/ask")
async def ask(req: AskRequest):
    return await agent.ask(req.question, req.observations, req.product_context)
