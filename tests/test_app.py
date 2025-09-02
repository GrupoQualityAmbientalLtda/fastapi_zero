from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from src.fastapi_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_retornar_e_ok_ola_mundo():
    client = TestClient(app)  # Arrange (Organização)

    response = client.get('/')  # ACT, fase de ação

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)
    assert response.json() == {'message': 'oi mundo'}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'LucasLopes',
            'email': 'lucas@email.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'lucas@email.com',
        'username': 'LucasLopes',
    }
