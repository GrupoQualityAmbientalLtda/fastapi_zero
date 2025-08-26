from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fastapi_zero.app import app


def test_root_retornar_e_ok_ola_mundo():
    client = TestClient(app)  # Arrange (Organização)

    response = client.get('/')  # ACT, fase de ação

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)
    assert response.json() == {'message': 'Olá Mundo!'}
