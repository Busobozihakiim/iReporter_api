"""temporary data store"""
import datetime

RECORDS = []

class Incidents:
    """data manipulation methods"""
    def __init__(self):
        self.records = RECORDS

    def add_record(self, args):
        """create a red-flag or intervention record """
        record = {
            'id' : len(self.records) + 1,
            'createdOn' : datetime.date.today(),
            'type': args['type'],
            'location':args['location'],
            'status' : 'pending',
            'images':args['images'],
            'videos':args['videos'],
            'comment':args['comment'],
            }
        self.records.append(record)
        return record

    def all_records(self):
        """fetch all red flag records"""
        return self.records

    def one_record(self, report_id):
        """fetch a single record given an id"""
        record = [this_id for this_id in self.records if this_id['id'] == report_id]
        return record

    def edit_location(self, new_location, report_id):
        """change the location of a record"""
        location = self.one_record(report_id)
        location[0]['location'] = new_location['location']
        return location[0]['id']

    def edit_comment(self, new_comment, report_id):
        """change the comment of a record"""
        comment = self.one_record(report_id)
        comment[0]['location'] = new_comment['comment']
        return comment[0]['id']
