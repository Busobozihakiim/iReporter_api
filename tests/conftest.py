"""MOCK DATA FOR TESTING ENDPOINTS"""

EMPTY_RECORD = {}

REPORT = {
    'type': 'red-flag',
    'location':"5555,555",
    'images':'images',
    'videos':'videos',
    'comment':'lorem ipsum doe'
    }

MISSING_KEYS = {
    'location':"5555,555",
    'images':'images',
    'videos':'videos',
    'comment':'lorem ipsum doe'
    }

EMPTY_FIELDS = {
    'type': '',
    'location':"5555,555",
    'images':'images',
    'videos':'videos',
    'comment':'lorem ipsum doe'
    }
