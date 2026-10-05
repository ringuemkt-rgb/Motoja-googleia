from enum import StrEnum
from typing import Any
from pydantic import BaseModel, Field

class Verdict(StrEnum):
    DIRECT_FIT = "DIRECT_FIT"
    ADAPTABLE = "ADAPTABLE"
    UNCONFIRMED = "UNCONFIRMED"
    INCOMPATIBLE = "INCOMPATIBLE"

class RouteRequest(BaseModel):
    text: str

class RatioRequest(BaseModel):
    front_teeth: int = Field(gt=0)
    rear_teeth: int = Field(gt=0)

class FitmentInput(BaseModel):
    part_name: str
    mechanical: float = Field(ge=0, le=1)
    envelope: float = Field(ge=0, le=1)
    actuation: float = Field(ge=0, le=1)
    electrical: float = Field(ge=0, le=1)
    function: float = Field(ge=0, le=1)
    evidence: float = Field(ge=0, le=1)
    blockers: list[str] = []
    notes: list[str] = []

class FitmentResult(BaseModel):
    part_name: str
    score: int
    verdict: Verdict
    blockers: list[str]
    notes: list[str]

class DiagnosticTest(BaseModel):
    name: str
    why: str
    safety: int = Field(ge=0, le=10)
    cost: int = Field(ge=0, le=10)
    invasiveness: int = Field(ge=0, le=10)
    discrimination: int = Field(ge=0, le=10)
    expected: dict[str, Any] = {}

class DiagnosticPlanRequest(BaseModel):
    symptom: str
    observations: list[str] = []

class AskRequest(BaseModel):
    question: str
    observations: list[str] = []
    product_context: dict[str, Any] | None = None
