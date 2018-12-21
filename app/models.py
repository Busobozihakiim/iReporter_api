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

    def edit_field(self, new_value, report_id, key='location'):
        """change the location of a record"""
        edits = self.one_record(report_id)
        edits[0][key] = new_value[key]
        return edits[0]['id']

    def delete_redflag(self, report_id):
        """delete a redflag record"""
        delete = self.one_record(report_id)
        self.records.remove(delete[0])
        return delete[0]['id']
