import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
# from flask_login import login_required
from flask_cors import CORS

switches = Blueprint('switches', 'switches')
switch = Blueprint('switch', 'switch')

@switches.route('/index', methods=['GET'])
# @login_required
def switches_index():
    result = models.Switch.select()
    print('results of switch select query')
    print(result)

    switch_dicts = [model_to_dict(switch) for switch in result]
    
    return jsonify({
        'data': switch_dicts,
        'message': f"Successfully found {len(switch_dicts)} switches",
        'status': 200
    }), 200

@switches.route('/', methods=['POST'])
def create_switches():
    payload = request.get_json()
    print(payload)
    new_switches = models.Switch.create(**payload)
    print(new_switches)
    switch_dict = model_to_dict(new_switches)
    return jsonify(
        data=switch_dict,
        message="Successfully created switch!",
        status=201
    ), 201
    return "you hit the create route -- check terminal"

@switches.route('/<id>', methods=['GET'])
def get_one_switch(id):
    switch = models.Switch.get_by_id(id)
    print(switch)
    return jsonify(
        data=model_to_dict(switch),
        message="Success!",
        status=200
    ), 200

@switches.route('/<id>', methods=['PUT'])
def update_switches(id):
    payload = request.get_json()
    print(payload)

    models.Switch.update(**payload).where(models.Switch.id == id).execute()

    return jsonify(
        data=model_to_dict(models.Switch.get_by_id(id)),
        message="resource updated successfully",
        status=200
    ), 200

@switches.route('/<id>',  methods=['DELETE'])
def delete_switch(id):
    delete_query = models.Switch.delete().where(models.Switch.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)
    return jsonify(
        data={},
        message=f"Successfully deleted {nums_of_rows_deleted} switch with id {id}",
        status=200
    ), 200