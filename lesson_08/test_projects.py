"""Тесты для методов работы с проектами YouGile API."""
import uuid
import pytest
from lesson_08.yougile_api import YougileAPI


@pytest.fixture(scope="module")
def api_client():
    return YougileAPI()


@pytest.fixture(scope="function")
def project_cleanup(api_client):
    """Фикстура для автоматической очистки созданных проектов."""
    project_ids = []
    yield project_ids
    for pid in project_ids:
        try:
            api_client.delete_project(pid)
        except Exception:
            pass


def test_create_project_positive(api_client, project_cleanup):
    title = f"Test Project {uuid.uuid4()}"
    payload = {
        "title": title,
        "users": {api_client.user_id: "admin"}
    }
    response = api_client.create_project(payload)

    assert response.status_code in (200, 201), (
        f"Expected 200 or 201, got {response.status_code}: {response.text}"
    )
    data = response.json()

    # YouGile API при успешном создании возвращает ID проекта.
    # Проверяем наличие ID, это подтверждает успешное создание.
    assert "id" in data, f"Ожидали 'id' в ответе, но получили: {data}"

    project_cleanup.append(data["id"])


def test_create_project_negative(api_client):
    payload = {
        "title": "",
        "users": {api_client.user_id: "admin"}
    }
    response = api_client.create_project(payload)

    assert response.status_code >= 400, (
        f"Expected 4xx error, got {response.status_code}"
    )
    data = response.json()
    assert "error" in data or "message" in data


def test_get_project_positive(api_client, project_cleanup):
    title = f"Test Project Get {uuid.uuid4()}"
    create_payload = {
        "title": title,
        "users": {api_client.user_id: "admin"}
    }
    create_response = api_client.create_project(create_payload)
    project_id = create_response.json()["id"]
    project_cleanup.append(project_id)

    response = api_client.get_project(project_id)

    assert response.status_code == 200, (
        f"Expected 200, got {response.status_code}: {response.text}"
    )
    data = response.json()
    assert data.get("id") == project_id
    assert data.get("title") == title


def test_get_project_negative(api_client):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api_client.get_project(fake_id)

    assert response.status_code >= 400, (
        f"Expected 4xx error, got {response.status_code}"
    )
    data = response.json()
    assert "error" in data or "message" in data


def test_update_project_positive(api_client, project_cleanup):
    title = f"Test Project Update {uuid.uuid4()}"
    create_payload = {
        "title": title,
        "users": {api_client.user_id: "admin"}
    }
    create_response = api_client.create_project(create_payload)
    project_id = create_response.json()["id"]
    project_cleanup.append(project_id)

    new_title = f"Updated Project {uuid.uuid4()}"
    update_payload = {"title": new_title}
    response = api_client.update_project(project_id, update_payload)

    assert response.status_code in (200, 201), (
        f"Expected 200 or 201, got {response.status_code}: {response.text}"
    )

    get_response = api_client.get_project(project_id)
    assert get_response.status_code == 200
    assert get_response.json().get("title") == new_title


def test_update_project_negative(api_client):
    fake_id = "00000000-0000-0000-0000-000000000000"
    update_payload = {"title": f"Updated Project {uuid.uuid4()}"}
    response = api_client.update_project(fake_id, update_payload)

    assert response.status_code >= 400, (
        f"Expected 4xx error, got {response.status_code}"
    )
    data = response.json()
    assert "error" in data or "message" in data
