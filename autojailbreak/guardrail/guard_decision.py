from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class GuardDecision:
    allowed: bool
    category: Optional[str] = None
    reason: Optional[str] = None
    raw: Optional[str] = None
