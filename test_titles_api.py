import requests
import pytest


URL = "https://moviesdatabase.p.rapidapi.com/titles"
HEADERS = {
	"X-RapidAPI-Key": "0027390ea1msh969f223bc3135f7p1392aajsn24a59c70b4de"
}


def test_get_titles():
    # Act
    response = requests.get(URL, headers=HEADERS)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "page" in data
    assert "next" in data
    assert "entries" in data
    assert "results" in data
    assert len(data["results"]) == data["entries"]



@pytest.mark.parametrize("year", [1990, 2000, 2010, 2020, 9999])
def test_get_titles_by_release_year(year):
    # Arrange
    params = {"year": year}

    # Act
    response = requests.get(URL, headers=HEADERS, params=params)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "page" in data
    assert "next" in data
    assert "entries" in data
    assert "results" in data
    assert len(data["results"]) == data["entries"]
    if year == 9999:
        assert len(data["results"]) == 0
    else:
        for result in data["results"]:
            assert "id" in result
            assert "primaryImage" in result
            assert "titleType" in result
            assert "titleText" in result
            assert "releaseYear" in result
            assert "releaseDate" in result
            assert result["releaseYear"]["year"] == year


@pytest.mark.parametrize("limit", [1, 10, 50, -1, 0, 51])
def test_titles_endpoint_by_limit(limit):
    # Arrange
    params = {"limit": limit}

    # Act
    response = requests.get(URL, headers=HEADERS, params=params)

    # Assert
    assert response.status_code == 200
    data = response.json()
    if limit < 1:
        assert "error" in data
        assert data["error"] == "Limit too Low, limit has to be a greater than 0"
    elif limit > 50:
        assert "error" in data
        assert data["error"] == "Limit to High, limit has to be a lower than 51"
    else:
        assert "entries" in data
        assert data["entries"] == limit
        assert len(data["results"]) <= limit
