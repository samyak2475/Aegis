from datetime import datetime

from src.models.event_model import AegisEvent


def test_valid_event():
    event = AegisEvent(
        event_id="evt_001",
        timestamp=datetime.now(),
        source="sales",
        event_type="revenue_drop",
        severity="high",
        data={
            "current_revenue": 84000,
            "previous_revenue": 121000,
            "percentage_change": -30.58
        }
    )

    assert event.event_id == "evt_001"
    assert event.source == "sales"
    assert event.event_type == "revenue_drop"
    assert event.severity == "high"