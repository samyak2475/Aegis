from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class AegisEvent(BaseModel):
    """
    Canonical event representation used throughout Aegis.
    """

    event_id: str
    timestamp: datetime

    source: str
    event_type: str
    severity: str

    entity: Optional[Dict[str, Any]] = None
    data: Dict[str, Any] = Field(default_factory=dict)
    context: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None