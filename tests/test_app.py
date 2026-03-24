import pytest
import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_returns_json(client):
    response = client.get('/')
    data = response.get_json()
    assert data['service'] == 'devops-cicd-project'
    assert data['status'] == 'running'
    assert 'version' in data
    assert 'timestamp' in data

def test_health_returns_200(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_health_returns_healthy(client):
    response = client.get('/health')
    data = response.get_json()
    assert data['healthy'] == True

def test_metrics_returns_200(client):
    response = client.get('/metrics')
    assert response.status_code == 200

def test_metrics_returns_data(client):
    response = client.get('/metrics')
    data = response.get_json()
    assert 'service' in data
    assert 'version' in data
    assert 'environment' in data
