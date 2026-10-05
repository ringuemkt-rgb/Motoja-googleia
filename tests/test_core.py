from xtz_agent.domain import FitmentInput
from xtz_agent.fitment import evaluate
from xtz_agent.router import route

def test_product_route():
    assert route("Esse carburador da Shopee serve?") == "PRODUCT_AUDIT"

def test_fitment_direct():
    result = evaluate(FitmentInput(
        part_name="test", mechanical=1, envelope=1, actuation=1,
        electrical=1, function=1, evidence=1
    ))
    assert result.score == 100
    assert result.verdict.value == "DIRECT_FIT"

def test_pinout_blocker_prevents_direct_fit():
    result = evaluate(FitmentInput(
        part_name="CDI", mechanical=1, envelope=1, actuation=1,
        electrical=.9, function=1, evidence=.9,
        blockers=["pinagem não confirmada"]
    ))
    assert result.verdict.value != "DIRECT_FIT"

def test_ratio_route():
    assert route("quero trocar pinhão e coroa") == "TRANSMISSION"
