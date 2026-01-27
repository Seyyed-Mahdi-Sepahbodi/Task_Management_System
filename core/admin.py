from django.contrib import admin
from .models import Project, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "created_at")
    search_fields = ("title", "owner__username", "owner__email")
    list_filter = ("created_at",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "project", "status", "priority", "assignee", "due_date", "created_at")
    search_fields = ("title", "project__title", "assignee__username", "assignee_email")
    list_filter = ("status", "priority", "due_date", "created_at")
