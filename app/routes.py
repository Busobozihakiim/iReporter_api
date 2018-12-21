"""ROUTES FOR THE API"""
from flask import Flask, jsonify, request
from .models import Incidents
from .helper import edit_helper

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

    if len(report) < 5:
        return jsonify({"status":400, "error":"You are missing a field"}), 400

    for key, value in report.items():
        if value in ("", " "):
            return jsonify({"status":400,
                            "error":"You are missing value of '{}' in your input".format(key)}), 400

    report = records.add_record(report)
    return jsonify({"status":201,
                    "data":[{"id": report["id"], "message":"Created red-flag record"}]}), 201

@app.route('/api/v1/red_flags/<int:red_flag_id>', methods=['DELETE'])
def remove_record(red_flag_id):
    """deletes record"""
    try:
        deleted = records.delete_redflag(red_flag_id)
        return jsonify({"status":200,
                        "data":[{"id":deleted,
                                 "message":"red-flag record has been deleted"}]})
    except IndexError:
        return jsonify({"status":404,
                        "error":"The red flag of id {} does not exist".format(red_flag_id)}), 404

@app.route('/api/v1/red_flags/<int:red_flag_id>/<field>', methods=['PATCH'])
def edit_status(red_flag_id, field):
    """edits the field passed in the url by id"""
    try:
        return edit_helper(red_flag_id, request.get_json(), field)
    except KeyError:
        return jsonify({"status":404, "message":"route not available"}), 404
    