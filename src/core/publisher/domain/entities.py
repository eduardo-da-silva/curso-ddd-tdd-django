import uuid

from dataclasses import dataclass, field
from uuid import UUID

@dataclass(kw_only=True)
class Publisher:
    id: UUID = field(default_factory=uuid.uuid4)
    name: str
    description: str = ""
    is_active: bool = True