from rest_framework import serializers
from snippets.models import Tasks, Vehicle, POINT_TYPE_CHOICES


class VehicleSerializer(serializers.Serializer):
    machine_id = serializers.IntegerField(read_only=True)
    machine_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    machine_type = serializers.IntegerField()
    readiness = serializers.CharField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Vehicle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.machine_id = validated_data.get('machine_id', instance.machine_id)
        instance.machine_name = validated_data.get('machine_name', instance.machine_name)
        instance.machine_type = validated_data.get('machine_type', instance.machine_type)
        instance.readiness = validated_data.get('readiness', instance.readiness)
        instance.save()
        return instance


class TasksSerializer(serializers.Serializer):
    task_id = serializers.IntegerField(read_only=True)
    machine_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Tasks.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.task_id = validated_data.get('task_id', instance.task_id)
        instance.machine_id = validated_data.get('machine_id', instance.machine_id)
        instance.save()
        return instance
