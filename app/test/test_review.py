from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
BASE_URL = 'http://127.0.0.1:8000/api/reviews'
HEALTH_URL = 'http://127.0.0.1:8000'
data = {
    "author": "Lee Sammy",
    "comment": "Testing",
    "rating": 4
}


def test_api_health():
    response = client.get(HEALTH_URL)
    assert response.status_code == status.HTTP_200_OK


def test_get_reviews():
    response = client.get(f'{BASE_URL}')
    assert response.status_code == status.HTTP_200_OK


def test_get_reviews_by_movie():
    response = client.get(f'{BASE_URL}/3')
    assert response.status_code == status.HTTP_200_OK


def test_create_review():
    response = client.post(f'{BASE_URL}/3', json=data)
    review_id = response.json()['id']
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['id'] == review_id


def test_average_movie_rating():
    response = client.get(f'{BASE_URL}/average-rating/3')
    assert response.status_code == status.HTTP_200_OK


def test_delete_movie_reviews():
    response = client.delete(f'{BASE_URL}/delete-reviews/2')
    assert response.status_code == status.HTTP_204_NO_CONTENT
