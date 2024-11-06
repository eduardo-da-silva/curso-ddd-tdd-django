from dataclasses import dataclass
from uuid import UUID
from core.publisher.domain.entities import Publisher
from core.publisher.domain.interfaces import PublisherRepository

@dataclass
class ListItemPublisherOutput:
    id: UUID
    name: str
    description: str
    is_active: bool

class ListPublisherUseCase:
    def __init__(self, repository: PublisherRepository):
        self.repository = repository

    def execute(self) -> list[ListItemPublisherOutput]:
        publishers = self.repository.list()
        return [
            ListItemPublisherOutput(
                id=publisher.id,
                name=publisher.name,
                description=publisher.description,
                is_active=publisher.is_active
            ) for publisher in publishers
        ] 