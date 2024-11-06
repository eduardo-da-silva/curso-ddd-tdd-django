import uuid

from dataclasses import dataclass, field
from uuid import UUID

@dataclass(kw_only=True)
class Publisher:
    id: UUID = field(default_factory=uuid.uuid4)
    name: str
    description: str = ""
    is_active: bool = True

    def __post_init__(self):
        if len(self.name) > 255:
            raise ValueError("O nome deve ser menor que 255 caracteres")