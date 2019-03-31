from rest_framework import serializers
from snippets.models import Snippet, Tasks, Vehicle, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


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
