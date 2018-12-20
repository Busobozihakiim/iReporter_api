"""ROUTES FOR THE API"""
from flask import Flask, jsonify, request
from .models import RECORDS, add_record

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
    return jsonify({"status":404, "error":"You dont have any red flag records"}), 404

@app.route(PREFIX, methods=['POST'])
def create_record():
    """creates a red-flag or intervention record"""
    report = request.get_json() or {}
    #check for an empty post and missing fields
    if not report:
        return jsonify({"status":400, "error":"You entered nothing"}), 400

    if len(report) < 5:
        return jsonify({"status":400, "error":"You are missing a field"}), 400

    #check for empty values in post and return missing field
    for key, value in report.items():
        if value in (' ', ''):
            return jsonify({"status":400,
                            "error":"You are missing value of '{}' in your input".format(key)}), 400

    #create a red-flag or intervention report
    report = add_record(report['type'], report['location'], report['images'],
                        report['videos'], report['comment'])
    return jsonify({"status":201,
                    "data":[{"id": report["id"], "message":"Created red-flag record"}]}), 201

@app.route(PREFIX + '/<int:red_flag_id>/location', methods=['PATCH'])
def edits_records_location(red_flag_id):
    """changes location of a record"""
    new_location = request.get_json()

    if not new_location:
        return jsonify({"status":400, "error":"You entered nothing"}), 400

    if new_location['location'] in (' ', ''):
        return jsonify({"status":400,
                        "error":"You have not entered the cordinates"}), 400

    try:
        if RECORDS:
            location = [current for current in RECORDS if current['id'] == red_flag_id]
            location[0]['location'] = '{}'.format(new_location['location'])
            return jsonify({"status":201,
                            "data":[{"id": location[0]["id"],
                                     "message":"Updated red-flag record’s location"}]}), 201
        return jsonify({"status":404, "error":"You have no red flag records"}), 404
    except IndexError:
        return jsonify({"status":404,
                        "error":"The red flag of id {} does not exist".format(red_flag_id)}), 404

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
