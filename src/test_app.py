import pytest
from app import create_app
import json

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_snomed_code(client):
    id = '1176851000000113'
    response = client.get(f'/api/snomed_code/{id}')
    assert response.status_code == 200
    print(json.loads(response.data))
    # Add more assertions here if needed

def test_add_snomed_code(client):
    # Define the request body
    data = {
        'concept_id': '123',
        'description_id': '456',
        'description': 'Example Description'
    }

    # Make a POST request with the request body
    response = client.post('/api/snomed_code', json=data)
    assert response.status_code == 200
    print(json.loads(response.data)[0])
    # Add more assertions here if needed

def test_search_snomed_code(client):
    search_string = 'a,e'
    n = 2
    response = client.get(f'/api/snomed_code/search?search_string={search_string}&n={n}')
    assert response.status_code == 200
    print(json.loads(response.data)[0])
    # Add more assertions here if needed
