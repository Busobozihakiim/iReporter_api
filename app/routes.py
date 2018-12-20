"""ROUTES FOR THE API"""
from flask import Flask, jsonify
from .models import RECORDS

app = Flask(__name__)
PREFIX = '/api/v1/red_flags'

@app.route(PREFIX +'/<int:red_flag_id>')
def get_one_record(red_flag_id):
    """returns a single red-flag or intervention record"""
    try:
        if RECORDS:
            order = [this_id for this_id in RECORDS if this_id['id'] == red_flag_id]
            return jsonify({"status":200, "data":order[0]})
        return jsonify({"status":200, "error":"No red flags made yet"})
    except IndexError:
        return jsonify({"status":200,
                        "error":"this red flag order of id {} doesnt exist".format(red_flag_id)})

@app.route(PREFIX)
def gets_records():
    """returns all records"""
    if RECORDS:
        return jsonify({"status":200, "data":RECORDS})
    return jsonify({"status":404, "error":"You dont have any delivery orders"}), 404

@app.route(PREFIX, methods=['POST'])
def create_record():
    """creates a red-flag or intervention record"""
    pass

@app.route(PREFIX + '/<int:red_flag_id>/location', methods=['PATCH'])
def edits_records_location():
    """changes location of a record"""
    pass

@app.route(PREFIX + '/<int:red_flag_id>/comment', methods=['PATCH'])
def edits_records_comment():
    """changes the comment in a record"""
    pass

@app.route(PREFIX + '/<int:red_flag_id>', methods=['DELETE'])
def remove_record():
    """deletes record"""
    pass

@app.route(PREFIX + '/<int:red_flag_id>', methods=['PATCH'])
def edit_status():
    """Admin edits records"""
    pass
