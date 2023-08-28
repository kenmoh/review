from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
BASE_URL = 'http://127.0.0.1:8000/api/reviews'
HEALTH_URL = 'http://127.0.0.1:8000'
data = {
    "review_by": "Lee Sammy",
    "review_body": "Testing",
    "rating": 4
}


def test_api_health():
    response = client.get(HEALTH_URL)
    assert response.status_code == status.HTTP_200_OK


def test_get_reviews():
    response = client.get(f'{BASE_URL}')
    assert response.status_code == status.HTTP_200_OK


def test_get_reviews_by_book():
    response = client.get(f'{BASE_URL}/4')
    assert response.status_code == status.HTTP_200_OK


def test_create_review():
    response = client.post(f'{BASE_URL}/5', json=data)
    review_id = response.json()['id']
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['id'] == review_id


def test_average_book_rating():
    response = client.get(f'{BASE_URL}/average-rating/5')
    print(response.json())
    assert response.status_code == status.HTTP_200_OK


