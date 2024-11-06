from rest_framework import serializers

class CreatePublisherRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(required=False)


class CreatePublisherResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)

class ListItemPublisherOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)