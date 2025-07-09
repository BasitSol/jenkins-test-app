# test_app.py
import pytest
from app import app # Import your Flask app instance

@pytest.fixture
def client():
    # This fixture sets up a test client for your Flask app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    # Test the '/' route
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_another_route_example(client):
    # Example of another test, assuming you add another route
    # For now, this might fail or be skipped if the route doesn't exist
    # response = client.get('/nonexistent')
    # assert response.status_code == 404 # Expecting 404 for non-existent route
    pass # Placeholder to make this test pass for now if no other routes
