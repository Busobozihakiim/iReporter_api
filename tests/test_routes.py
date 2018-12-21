"""TESTS ENDPOINTS"""
import json
import pytest
from app.routes import app
from .conftest import REPORT, EMPTY_FIELDS, MISSING_KEYS

@pytest.fixture(scope='module')
def _setup():
    """creates a test client"""
    client = app.test_client()
    yield client

def test_get_one_record_with_no_records(_setup):
    """test when no red flag report has been recorded"""
    response = _setup.get('/api/v1/red_flags/2')
    assert 'No red flags made yet' in  str(response.json)

def test_gets_records_when_null(_setup):
    """test when no incident report has been made"""
    response = _setup.get('/api/v1/red_flags')
    assert 'You dont have any red flag records' in str(response.json)

def test_change_redflags_location_with_no_records(_setup):
    """test change of location when no red flgs available"""
    response = _setup.patch('/api/v1/red_flags/1/location',
                            data=json.dumps({"location":"32.565, 26.356"}),
                            content_type='application/json')
    assert 'You have no red flag records' in str(response.json)

def test_change_redflags_comment_with_no_records(_setup):
    """test edit of a comment when no red flags are available"""
    response = _setup.patch('/api/v1/red_flags/1/comment',
                            data=json.dumps({"comment":"the new comment"}),
                            content_type='application/json')
    assert 'You have no red flag records' in str(response.json)

def test_edit_status_with_no_records(_setup):
    """Test status editing when no redflags are available """
    response = _setup.patch('/api/v1/red_flags/1/status',
                            data=json.dumps({"status":"resolved"}),
                            content_type='application/json')
    assert 'You have no red flag records' in str(response.data)

def test_create_record_with_missing_values(_setup):
    """test whether the user has submitted a post with missing values"""
    response = _setup.post('/api/v1/red_flags',
                           data=json.dumps(EMPTY_FIELDS),
                           content_type='application/json')
    assert b"You are missing value of 'type' in your input" in response.data

def test_create_record_with_missing_keys(_setup):
    """test whether the user is missing some fields"""
    response = _setup.post('/api/v1/red_flags',
                           data=json.dumps(MISSING_KEYS),
                           content_type='application/json')
    assert 'You are missing a field' in str(response.json)

def test_create_record(_setup):
    """Test to create a red flag record """
    response = _setup.post('/api/v1/red_flags',
                           data=json.dumps(REPORT),
                           content_type='application/json')
    assert 'Created red-flag record'in str(response.json)

def test_get_one_record(_setup):
    """test when a red-flag id exists"""
    response = _setup.get('/api/v1/red_flags/1')
    assert "comment': 'lorem ipsum doe'" in  str(response.json)

def test_get_one_record_with_missing_id(_setup):
    """test when red flags id doesnt exist"""
    response = _setup.get('/api/v1/red_flags/2')
    assert 'this red flag order of id 2 doesnt exist' in  str(response.json)

def test_gets_records(_setup):
    """test when records have been made"""
    response = _setup.get('/api/v1/red_flags')
    assert 'lorem ipsum doe' in str(response.json)

def test_edits_records_location_no_cordinates(_setup):
    """test change of location with no cordinates """
    response = _setup.patch('/api/v1/red_flags/2/location',
                            data=json.dumps({"location":""}),
                            content_type='application/json')
    assert 'You have not entered the cordinates' in str(response.json)

def test_change_redflags_location(_setup):
    """test change of location """
    response = _setup.patch('/api/v1/red_flags/1/location',
                            data=json.dumps({"location":"32.565, 26.356"}),
                            content_type='application/json')
    assert 'Updated red-flag records location' in str(response.json)

def test_edits_records_location_when_id_not_exists(_setup):
    """test change of location when the record is not available"""
    response = _setup.patch('/api/v1/red_flags/2/location',
                            data=json.dumps({"location":"32.565, 26.356"}),
                            content_type='application/json')
    assert 'The red flag of id 2 does not exist' in str(response.json)

def test_edits_records_comment_no_comment(_setup):
    """test change of comment with no new comment"""
    response = _setup.patch('/api/v1/red_flags/2/comment',
                            data=json.dumps({"comment":""}),
                            content_type='application/json')
    assert 'You have not entered the new comment' in str(response.json)

def test_change_redflags_comment(_setup):
    """test change of comment """
    response = _setup.patch('/api/v1/red_flags/1/comment',
                            data=json.dumps({"comment":"the new comment"}),
                            content_type='application/json')
    assert 'Updated red-flag record’s comment' in str(response.json)

def test_edits_records_comment_when_id_not_exists(_setup):
    """test change of comment when the record is not available"""
    response = _setup.patch('/api/v1/red_flags/2/comment',
                            data=json.dumps({"comment":"the new comment"}),
                            content_type='application/json')
    assert 'The red flag of id 2 does not exist' in str(response.json)

def test_remove_red_flag_record_when_id_doest_exist(_setup):
    """test remove of a record"""
    response = _setup.delete('/api/v1/red_flags/3')
    assert response.status_code == 404
    assert 'The red flag of id 3 does not exist' in str(response.json)

def test_change_redflags_status(_setup):
    """test change of status """
    response = _setup.patch('/api/v1/red_flags/1/status',
                            data=json.dumps({"status":"under investigation"}),
                            content_type='application/json')
    assert 'Updated red-flag record’s status' in str(response.json)

def test_edits_records_status_when_id_not_exists(_setup):
    """test change of status when the record is not available"""
    response = _setup.patch('/api/v1/red_flags/2/status',
                            data=json.dumps({"status":"rejected"}),
                            content_type='application/json')
    assert 'The red flag of id 2 does not exist' in str(response.json)

def test_edit_status_with_missing_value(_setup):
    """Test whether what the admin has submitted is empty """
    response = _setup.patch('/api/v1/red_flags/1/status',
                            data=json.dumps({"status":""}),
                            content_type='application/json')
    assert 'You have not entered the new status' in str(response.data)

def test_remove_red_flag_record(_setup):
    """test remove of a record"""
    response = _setup.delete('/api/v1/red_flags/1')
    assert 'red-flag record has been deleted' in str(response.json)
    