import json
from pathlib import Path

def test_canonical_baseline():
    path = Path(__file__).parents[1] / "knowledge" / "oem_baseline_21DE.json"
    baseline = json.loads(path.read_text(encoding="utf-8"))
    assert baseline["identity"]["model_code"] == "21DE"
    assert baseline["wheels_tires"]["front"]["rim"] == "1.60-21"
    assert baseline["wheels_tires"]["rear"]["rim"] == "2.15-18"
    assert baseline["transmission"]["front_sprocket_teeth"] == 14
    assert baseline["transmission"]["rear_sprocket_teeth"] == 48
    assert baseline["transmission"]["chain_slack_mm"] == [40,55]
    assert baseline["carburetion"]["type"] == "BS25-35"
