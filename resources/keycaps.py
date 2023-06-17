import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
# from flask_login import login_required
from flask_cors import CORS

keycaps = Blueprint('keycaps', 'keycaps')
keycap = Blueprint('keycap', 'keycap')

@keycaps.route('/index', methods=['GET'])
# @login_required
def keycaps_index():
    result = models.Keycap.select()
    print('results of keycap select query')
    print(result)

    keycap_dicts = [model_to_dict(keycap) for keycap in result]
    
    return jsonify({
        'data': keycap_dicts,
        'message': f"Successfully found {len(keycap_dicts)} keycaps",
        'status': 200
    }), 200

@keycaps.route('/', methods=['POST'])
def create_keycaps():
    payload = request.get_json()
    print(payload)
    new_keycaps = models.Keycap.create(**payload)
    print(new_keycaps)
    keycap_dict = model_to_dict(new_keycaps)
    return jsonify(
        data=keycap_dict,
        message="Successfully created keycap!",
        status=201
    ), 201
    return "you hit the create route -- check terminal"

@keycaps.route('/<id>', methods=['GET'])
def get_one_keycap(id):
    keycap = models.Keycap.get_by_id(id)
    print(keycap)
    return jsonify(
        data=model_to_dict(keycap),
        message="Success!",
        status=200
    ), 200

@keycaps.route('/<id>', methods=['PUT'])
def update_keycaps(id):
    payload = request.get_json()
    print(payload)

    models.Keycap.update(**payload).where(models.Keycap.id == id).execute()

    return jsonify(
        data=model_to_dict(models.Keycap.get_by_id(id)),
        message="resource updated successfully",
        status=200
    ), 200

@keycaps.route('/<id>',  methods=['DELETE'])
def delete_keycap(id):
    delete_query = models.Keycap.delete().where(models.Keycap.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)
    return jsonify(
        data={},
        message=f"Successfully deleted {nums_of_rows_deleted} keycap with id {id}",
        status=200
    ), 200