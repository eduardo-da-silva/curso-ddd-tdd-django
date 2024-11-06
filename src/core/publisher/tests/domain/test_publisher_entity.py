from core.publisher.domain.entities import Publisher


class TestCreatePublisher:
    def test_create_valid_publisher(self):
        publisher = Publisher(name="Test Publisher")
        assert publisher.name == "Test Publisher"
        assert publisher.is_active is True