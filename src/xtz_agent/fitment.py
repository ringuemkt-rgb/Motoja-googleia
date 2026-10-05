from .domain import FitmentInput, FitmentResult, Verdict

WEIGHTS = {
    "mechanical": 35,
    "envelope": 10,
    "actuation": 10,
    "electrical": 20,
    "function": 10,
    "evidence": 15,
}

def evaluate(data: FitmentInput) -> FitmentResult:
    score = round(sum(getattr(data, key) * weight for key, weight in WEIGHTS.items()))
    severe = any(
        token in blocker.lower()
        for blocker in data.blockers
        for token in ("freio", "direção", "estrut", "combustível", "pinagem", "ac/dc", "interferência")
    )
    if severe:
        verdict = Verdict.INCOMPATIBLE if score < 70 else Verdict.UNCONFIRMED
    elif data.blockers:
        verdict = Verdict.UNCONFIRMED if score >= 50 else Verdict.INCOMPATIBLE
    elif score >= 90:
        verdict = Verdict.DIRECT_FIT
    elif score >= 70:
        verdict = Verdict.ADAPTABLE
    elif score >= 50:
        verdict = Verdict.UNCONFIRMED
    else:
        verdict = Verdict.INCOMPATIBLE
    return FitmentResult(
        part_name=data.part_name, score=score, verdict=verdict,
        blockers=data.blockers, notes=data.notes
    )
