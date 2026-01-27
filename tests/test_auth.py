import pytest
from rest_framework import status

@pytest.mark.django_db
def test_register(api_client):
    resp = api_client.post("/api/auth/register/", {
        "username": "newuser",
        "email": "new@x.com",
        "password": "StrongPass123!"
    }, format="json")
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.data["username"] == "newuser"

@pytest.mark.django_db
def test_login_returns_token(api_client, user):
    resp = api_client.post("/api/auth/login/", {
        "username": "u1",
        "password": "Pass12345!"
    }, format="json")
    assert resp.status_code == status.HTTP_200_OK
    assert "access" in resp.data
    assert "refresh" in resp.data

@pytest.mark.django_db
def test_refresh_token(api_client, user):
    login = api_client.post("/api/auth/login/", {
        "username": "u1",
        "password": "Pass12345!"
    }, format="json")
    refresh = login.data["refresh"]

    resp = api_client.post("/api/auth/token/refresh/", {"refresh": refresh}, format="json")
    assert resp.status_code == status.HTTP_200_OK
    assert "access" in resp.data
