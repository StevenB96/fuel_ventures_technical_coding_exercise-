import pytest
from app import create_app
import json
import random

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_snomed_code(client):
    ## Test successful retrieval.
    id = '822101011'
    response = client.get(f'/api/snomed_code/{id}')
    assert response.status_code == 200
    data = json.loads(response.get_json())
    assert isinstance(data, (dict))

    ## Test incorrect character failure.
    id = 'ABC'
    response = client.get(f'/api/snomed_code/{id}')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error'] == 'Description ID must be a number.'

    ## Test SNOMED code not found.
    id = 1
    response = client.get(f'/api/snomed_code/{id}')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error'] == "SNOMED code not found."

def test_add_snomed_code(client):
    ## Test successful addition.
    random_number = random.randint(0, 999999)
    formatted_number = str(random_number)
    # Define the request body
    data = {
        'concept_id': '123',
        'description_id': formatted_number,
        'description': 'Example Description'
    }
    # Make a POST request with the request body
    response = client.post('/api/snomed_code', json=data)
    assert response.status_code == 200
    data = json.loads(response.get_json())
    assert isinstance(data, (dict))

    ## Test incorrect character failure.
    # Define the request body
    data = {
        'concept_id': 'ABC',
        'description_id': '123',
        'description': 'Example Description'
    }
    # Make a POST request with the request body
    response = client.post('/api/snomed_code', json=data)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error'] == 'Concept ID must be a number.'

def test_search_snomed_code(client):
    ##Test valid search.
    search_string = 'a,e'
    n = 2
    response = client.get(f'/api/snomed_code/search?search_string={search_string}&n={n}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, (list))

    ##Test invalid N.
    search_string = 'a,e'
    n = 3
    response = client.get(f'/api/snomed_code/search?search_string={search_string}&n={n}')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error'] == 'N cannot be be larger than the number of required search terms.'
