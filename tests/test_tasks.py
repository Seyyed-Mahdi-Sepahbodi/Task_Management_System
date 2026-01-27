import pytest
from rest_framework import status

@pytest.mark.django_db
def test_list_tasks_in_project(auth_client, project, task):
    resp = auth_client.get(f"/api/projects/{project.id}/tasks/")
    assert resp.status_code == status.HTTP_200_OK
    ids = [item["id"] for item in resp.data["results"]]
    assert task.id in ids

@pytest.mark.django_db
def test_create_task_in_project(auth_client, project):
    payload = {
        "title": "T2",
        "description": "d",
        "status": "todo",
        "priority": 3,
        "due_date": "2026-02-10",
        "assignee": None
    }
    resp = auth_client.post(f"/api/projects/{project.id}/tasks/", payload, format="json")
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.data["title"] == "T2"

@pytest.mark.django_db
def test_cannot_access_tasks_of_other_users_project(auth_client, project_user2):
    resp = auth_client.get(f"/api/projects/{project_user2.id}/tasks/")
    assert resp.status_code in (status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN)

@pytest.mark.django_db
def test_filter_tasks(auth_client, project, task):
    resp = auth_client.get(f"/api/projects/{project.id}/tasks/?status=todo")
    assert resp.status_code == status.HTTP_200_OK
    ids = [item["id"] for item in resp.data["results"]]
    assert task.id in ids
