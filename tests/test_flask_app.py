import sys

sys.path.insert(0, "./movies_catalogue")
import pytest
from ..main import app
from unittest.mock import Mock
from .. import tmdb_client


@pytest.mark.parametrize(
    "list_type", ["popular", "now_playing", "top_rated", "upcoming"]
)
def test_homepage_list(monkeypatch, list_type):
    api_mock = Mock(return_value={"results": []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f"/?list_type={list_type}")
        assert response.status_code == 200
        api_mock.assert_called_once_with(f"movie/{list_type}")
