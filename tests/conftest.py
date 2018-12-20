"""MOCK DATA FOR TESTING ENDPOINTS"""

EMPTY_RECORD = {}

REPORT = {
    'id' :1,
    'type': 'red-flag',
    'location':"5555,555",
    'status' : 'pending',
    'images':'images',
    'videos':'videos',
    'comment':'lorem ipsum doe'
    }

MISSING_KEYS = {
    'id' :1,
    'location':"5555,555",
    'status' : 'pending',
    'images':'images',
    'videos':'videos',
    'comment':'lorem ipsum doe'
    }

EMPTY_FIELDS = {
    'id' :1,
    'type': 'red-flag',
    'location':"5555,555",
    'status' : 'pending',
    'images':'images',
    'videos':'videos',
    'comment':'lorem ipsum doe'
    }
