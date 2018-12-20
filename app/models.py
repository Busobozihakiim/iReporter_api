"""temporary data store"""
import datetime

RECORDS = []

def add_record(the_type, location, images, videos, comment):
    """create a red-flag or intervention record """
    record = {
        'id' : len(RECORDS) + 1,
        'createdOn' : datetime.date.today(),
        'type': the_type,
        'location':location,
        'status' : 'pending',
        'images':images,
        'videos':videos,
        'comment':comment,
        }
    RECORDS.append(record)
    return record
        