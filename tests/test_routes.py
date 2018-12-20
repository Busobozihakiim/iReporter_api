"""TESTS ENDPOINTS"""
import json
import pytest
from app.routes import app
from .conftest import REPORT, EMPTY_FIELDS, EMPTY_RECORD, MISSING_KEYS

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

def test_gets_records_when_null(_setup):
    """test when no incident report has been made"""
    response = _setup.get('/api/v1/red_flags')
    assert response.status_code == 404
    assert 'You dont have any red flag records' in str(response.json)

def test_change_redflags_location_with_no_records(_setup):
    """test change of location when no red flgs available"""
    response = _setup.patch('/api/v1/red_flags/1/location',
                            data=json.dumps({"location":"32.565, 26.356"}),
                            content_type='application/json')
    assert response.status_code == 404
    assert 'You have no red flag records' in str(response.json)

def test_create_record_with_no_data(_setup):
    """Test whether the user has submitted an empty post"""
    response = _setup.post('/api/v1/red_flags',
                           data=json.dumps(EMPTY_RECORD),
                           content_type='application/json')
    assert response.status_code == 400
    assert b'You entered nothing' in response.data

def test_create_record_with_missing_values(_setup):
    """test whether the user has submitted a post with missing values"""
    response = _setup.post('/api/v1/red_flags',
                           data=json.dumps(EMPTY_FIELDS),
                           content_type='application/json')
    assert response.status_code == 400
    assert b"You are missing value of 'type' in your input" in response.data

def test_create_record_with_missing_keys(_setup):
    """test whether the user is missing some fields"""
    response = _setup.post('/api/v1/red_flags',
                           data=json.dumps(MISSING_KEYS),
                           content_type='application/json')
    assert response.status_code == 400
    assert 'You are missing a field' in str(response.json)

def test_create_record(_setup):
    """Test to create a red flag record """
    response = _setup.post('/api/v1/red_flags',
                           data=json.dumps(REPORT),
                           content_type='application/json')
    assert response.status_code == 201
    assert 'Created red-flag record'in str(response.json)

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

def test_edits_records_location(_setup):
    """test change of location whe nothing has been posted"""
    response = _setup.patch('/api/v1/red_flags/2/location')
    assert response.status_code == 400
    assert 'You entered nothing' in str(response.json)

def test_edits_records_location_no_cordinates(_setup):
    """test change of location with no cordinates """
    response = _setup.patch('/api/v1/red_flags/2/location',
                            data=json.dumps({"location":""}),
                            content_type='application/json')
    assert response.status_code == 400
    assert 'You have not entered the cordinates' in str(response.json)

def test_change_redflags_location(_setup):
    """test change of location """
    response = _setup.patch('/api/v1/red_flags/1/location',
                            data=json.dumps({"location":"32.565, 26.356"}),
                            content_type='application/json')
    assert response.status_code == 201
    assert 'Updated red-flag record’s location' in str(response.json)

def test_edits_records_location_when_id_not_exists(_setup):
    """test change of location when the record is not available"""
    response = _setup.patch('/api/v1/red_flags/2/location',
                            data=json.dumps({"location":"32.565, 26.356"}),
                            content_type='application/json')
    assert response.status_code == 404
    assert 'The red flag of id 2 does not exist' in str(response.json)