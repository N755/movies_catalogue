import sys
import pytest

sys.path.insert(0, "./movies_catalogue")
from unittest.mock import Mock
import pytest

from tmdb_client import get_single_movie, get_single_movie_cast, get_popular_movies


@pytest.fixture
def mock_response():
    response = Mock()
    response.json.return_value = {"test_key": "test_value"}
    response.status_code = 200
    return response


def test_get_single_movie(monkeypatch, mock_response):
    def mock_get(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.get", mock_get)
    result = get_single_movie(123)
    assert result == {"test_key": "test_value"}


def test_get_single_movie_cast(monkeypatch):
    mock_cast_list = [{"id": 1, "name": "Actor 1"}, {"id": 2, "name": "Actor 2"}]
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = {"cast": mock_cast_list}
    monkeypatch.setattr("requests.get", requests_mock)
    cast_list = get_single_movie_cast(123)
    assert cast_list == mock_cast_list


def test_get_popular_movies(monkeypatch, mock_response):
    def mock_get(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.get", mock_get)
    result = get_popular_movies("popular")
    assert result == {"test_key": "test_value"}
