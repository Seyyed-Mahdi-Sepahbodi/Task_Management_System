import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from core.models import Project, Task

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username="u1", password="Pass12345!")

@pytest.fixture
def user2(db):
    return User.objects.create_user(username="u2", password="Pass12345!")

@pytest.fixture
def auth_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def auth_client_user2(api_client, user2):
    api_client.force_authenticate(user=user2)
    return api_client

@pytest.fixture
def project(db, user):
    return Project.objects.create(owner=user, title="P1", description="D1")

@pytest.fixture
def project_user2(db, user2):
    return Project.objects.create(owner=user2, title="P2", description="D2")

@pytest.fixture
def task(db, project, user):
    return Task.objects.create(
        project=project,
        title="T1",
        description="TD",
        status="todo",
        priority=2,
        assignee=user,
    )
