from dataclasses import dataclass
from uuid import UUID
from core.publisher.domain.entities import Publisher
from core.publisher.domain.interfaces import PublisherRepository

@dataclass
class CreatePublisherInput:
    name: str
    description: str = ""

@dataclass
class CreatePublisherOutput:
    id: UUID

class CreatePublisherUseCase:
    def __init__(self, repository: PublisherRepository):
        self.repository = repository

    def execute(self, request: CreatePublisherInput) -> CreatePublisherOutput:
        publisher = Publisher(name=request.name, description=request.description)
        created_publisher = self.repository.create(publisher)
        return CreatePublisherOutput(id=created_publisher.id)