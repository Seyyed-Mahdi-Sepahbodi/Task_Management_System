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
