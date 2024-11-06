from abc import ABC, abstractmethod

from core.publisher.domain.entities import Publisher


class PublisherRepository(ABC):
    @abstractmethod
    def create(self, publisher: Publisher) -> Publisher:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Publisher]:
        raise NotImplementedError