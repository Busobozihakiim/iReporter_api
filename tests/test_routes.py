"""TESTS ENDPOINTS"""
import pytest
from app.routes import app

@pytest.fixture(scope='module')
def _setup():
    """creates a test client"""
    client = app.test_client()
    yield client

def test_get_one_record_with_no_records(_setup):
    """test when no red flag report has been recorded"""
    response = _setup.get('/api/v1/red_flags/2')
    assert response.status_code == 200
    assert 'No red flags made yet' in  str(response.json)

def test_get_one_record(_setup):
    """test when a red-flag id exists"""
    response = _setup.get('/api/v1/red_flags/1')
    assert response.status_code == 200
    assert "comment': 'lorem ipsum doe'" in  str(response.json)

def test_get_one_record_with_missing_id(_setup):
    """test when red flags id doesnt exist"""
    response = _setup.get('/api/v1/red_flags/2')
    assert response.status_code == 200
    assert 'this red flag order of id 2 doesnt exist' in  str(response.json)

def test_gets_records(_setup):
    """test when records have been made"""
    response = _setup.get('/api/v1/red_flags')
    assert response.status_code == 200
    assert 'lorem ipsum doe' in str(response.json)

def test_gets_records_when_null(_setup):
    """test when no incident report has been made"""
    response = _setup.get('/api/v1/red_flags')
    assert response.status_code == 404
    assert 'You dont have any delivery orders' in str(response.json)
    