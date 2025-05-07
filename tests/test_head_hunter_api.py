from unittest.mock import patch, Mock
from src.head_hunter_api import HeadHunterAPI
from unittest.mock import patch


@patch('src.head_hunter_api.requests.get')  # Adjust the import according to your module structure
def test_get_vacancies_success(mock_get):
    mock_hh_api = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"id": 1, "name": "Developer"}]}
    mock_get.return_value = mock_response

    vacancies = mock_hh_api.get_vacancies("developer", 10)
    assert len(vacancies) == 1
    assert vacancies[0][0]['name'] == "Developer"

@patch('src.head_hunter_api.requests.get')  # Adjust the import according to your module structure
def test_get_vacancies_no_results(mock_get):
    mock_hh_api = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": []}
    mock_get.return_value = mock_response

    vacancies = mock_hh_api.get_vacancies("nonexistent_keyword", 10)
    assert vacancies == [[]]
