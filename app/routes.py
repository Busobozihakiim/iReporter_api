"""ROUTES FOR THE API"""
from flask import Flask, jsonify, request
from .models import Incidents

app = Flask(__name__)

records = Incidents()

@app.route('/api/v1/red_flags/<int:red_flag_id>')
def get_one_record(red_flag_id):
    """returns a single red-flag or intervention record"""
    try:
        if records.all_records():
            red_flag = records.one_record(red_flag_id)
            return jsonify({"status":200, "data":red_flag[0]})
        return jsonify({"status":200, "error":"No red flags made yet"})
    except IndexError:
        return jsonify({"status":200,
                        "error":"this red flag order of id {} doesnt exist".format(red_flag_id)})

@app.route('/api/v1/red_flags')
def gets_records():
    """returns all records"""
    if  records.all_records():
        return jsonify({"status":200, "data":records.all_records()})
    return jsonify({"status":404, "error":"You dont have any red flag records"}), 404

@app.route('/api/v1/red_flags', methods=['POST'])
def create_record():
    """creates a red-flag or intervention record"""
    report = request.get_json() or {}

    if not report:
        return jsonify({"status":400, "error":"You entered nothing"}), 400

    if len(report) < 5:
        return jsonify({"status":400, "error":"You are missing a field"}), 400

    for key, value in report.items():
        if value in (' ', ''):
            return jsonify({"status":400,
                            "error":"You are missing value of '{}' in your input".format(key)}), 400

    report = records.add_record(report)
    return jsonify({"status":201,
                    "data":[{"id": report["id"], "message":"Created red-flag record"}]}), 201

@app.route('/api/v1/red_flags/<int:red_flag_id>/location', methods=['PATCH'])
def edits_records_location(red_flag_id):
    """changes location of a record"""
    user_input = request.get_json()

    if not user_input:
        return jsonify({"status":400, "error":"You entered nothing"}), 400

    if user_input['location'] in (' ', ''):
        return jsonify({"status":400,
                        "error":"You have not entered the cordinates"}), 400

    try:
        if records.all_records():
            new_location = records.edit_field(user_input, red_flag_id, key='location')
            return jsonify({"status":201,
                            "data":[{"id":new_location,
                                     "message":"Updated red-flag records location"}]}), 201
        return jsonify({"status":404, "error":"You have no red flag records"}), 404
    except IndexError:
        return jsonify({"status":404,
                        "error":"The red flag of id {} does not exist".format(red_flag_id)}), 404

@app.route('/api/v1/red_flags/<int:red_flag_id>/comment', methods=['PATCH'])
def edits_records_comment(red_flag_id):
    """changes the comment in a record"""
    from_user = request.get_json()

    if not from_user:
        return jsonify({"status":400, "error":"You entered nothing"}), 400

    if from_user['comment'] in (' ', ''):
        return jsonify({"status":400,
                        "error":"You have not entered the new comment"}), 400
    try:
        if records.all_records():
            new_status = records.edit_field(from_user, red_flag_id, key='comment')
            return jsonify({"status":201,
                            "data":[{"id":new_status,
                                     "message":"Updated red-flag record’s comment"}]}), 201
        return jsonify({"status":404, "error":"You have no red flag records"}), 404
    except IndexError:
        return jsonify({"status":404,
                        "error":"The red flag of id {} does not exist".format(red_flag_id)}), 404

@app.route('/api/v1/red_flags/<int:red_flag_id>', methods=['DELETE'])
def remove_record(red_flag_id):
    """deletes record"""
    try:
        deleted = records.delete_redflag(red_flag_id)
        if deleted :
            return jsonify({"status":200,
                            "data":[{"id":deleted,
                                     "message":"red-flag record has been deleted"}]})
    except IndexError:
        return jsonify({"status":404,
                        "error":"The red flag of id {} does not exist".format(red_flag_id)}), 404

@app.route('/api/v1/red_flags/<int:red_flag_id>/status', methods=['PATCH'])
def edit_status(red_flag_id):
    """Admin edits records"""
    admin_input = request.get_json()

    if not admin_input:
        return jsonify({"status":400, "error":"You entered nothing"}), 400

    if admin_input['status'] in (' ', ''):
        return jsonify({"status":400,
                        "error":"You have not entered the new status"}), 400

    try:
        if records.all_records():
            new_status = records.edit_field(admin_input, red_flag_id, key='status')
            return jsonify({"status":201,
                            "data":[{"id":new_status,
                                     "message":"Updated red-flag record’s status"}]}), 201
        return jsonify({"status":404, "error":"You have no red flag records"}), 404
    except IndexError:
        return jsonify({"status":404,
                        "error":"The red flag of id {} does not exist".format(red_flag_id)}), 404

