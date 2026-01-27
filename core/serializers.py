from rest_framework import serializers
from models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")

    class Meta:
        model = Project
        fields = ("id", "owner", "title", "description", "created_at")
        read_only_fields = ("id", "owner", "created_at")


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "project", "assignee", "title", "description", "status", "priority", "due_date", "created_at")
        read_only_fields = ("id", "created_at", "project")
