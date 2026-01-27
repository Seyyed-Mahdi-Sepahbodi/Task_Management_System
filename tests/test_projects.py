import pytest
from rest_framework import status

@pytest.mark.django_db
def test_list_projects_only_own(auth_client, project, project_user2):
    resp = auth_client.get("/api/projects/")
    assert resp.status_code == status.HTTP_200_OK

    ids = [item["id"] for item in resp.data["results"]]
    assert project.id in ids
    assert project_user2.id not in ids

@pytest.mark.django_db
def test_create_project(auth_client):
    resp = auth_client.post("/api/projects/", {"title": "NewP", "description": "x"}, format="json")
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.data["title"] == "NewP"

@pytest.mark.django_db
def test_cannot_retrieve_other_users_project(auth_client, project_user2):
    resp = auth_client.get(f"/api/projects/{project_user2.id}/")
    assert resp.status_code in (status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN)

@pytest.mark.django_db
def test_cannot_delete_other_users_project(auth_client, auth_client_user2, project_user2):
    # user1 تلاش می‌کنه پروژه user2 رو حذف کنه
    resp = auth_client.delete(f"/api/projects/{project_user2.id}/")
    assert resp.status_code in (status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN)

    # خود user2 باید بتونه
    resp2 = auth_client.user2.delete(f"/api/projects/{project_user2.id}/")
    assert resp2.status_code == status.HTTP_204_NO_CONTENT
