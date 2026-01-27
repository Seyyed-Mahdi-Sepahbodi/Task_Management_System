from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from models import Project, Task
from serializers import ProjectSerializer, TaskSerializer
from permissions import IsProjectOwnerOrReadOnly

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectOwnerOrReadOnly]
    search_fields = ["title"]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filterset_fields = ["status", "priority", "due_date"]
    ordering_fields = ["created_at", "due_date", "priority"]
    search_fields = ["title"]

    def get_project(self):
        project_id = self.kwargs.get("project_pk")
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            raise PermissionDenied("Project not found.")
        if project.owner != self.request.user:
            raise PermissionDenied("You do not have access to this project.")
        return project

    def get_queryset(self):
        project = self.get_project()
        return Task.objects.filter(project=project).order_by("-created_at")

    def perform_create(self, serializer):
        project = self.get_project()
        serializer.save(project=project)
