"""EDITS FIELDS OF A RECORD"""
from flask import jsonify
from .models import Incidents

records = Incidents()

def edit_helper(the_id, user_input, key):
    """validates input and makes a change to the red flag."""
    if len(user_input) == 0 or user_input['{}'.format(key)] in ("", " "):
        return jsonify({"status":400,
                        "error":"You have not entered the new {}".format(key)}), 400
    try:
        if records.all_records():
            new_value = records.edit_field(user_input, the_id, '{}'.format(key))
            return jsonify({"status":201,
                            "data":[{"id":new_value,
                                     "message":"Updated red-flag records {}".format(key)}]}), 201
        return jsonify({"status":404, "error":"You have no red flag records"}), 404
    except IndexError:
        return jsonify({"status":404,
                        "error":"The red flag of id {} does not exist".format(the_id)}), 404
