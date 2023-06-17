import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
# from flask_login import login_required
from flask_cors import CORS

stabilizers = Blueprint('stabilizers', 'stabilizers')
stabilizer = Blueprint('stabilizer', 'stabilizer')

@stabilizers.route('/index', methods=['GET'])
# @login_required
def stabilizers_index():
    result = models.Stabilizer.select()
    print('results of stabilizer select query')
    print(result)

    stabilizer_dicts = [model_to_dict(stabilizer) for stabilizer in result]
    
    return jsonify({
        'data': stabilizer_dicts,
        'message': f"Successfully found {len(stabilizer_dicts)} stabilizers",
        'status': 200
    }), 200

@stabilizers.route('/', methods=['POST'])
def create_stabilizers():
    payload = request.get_json()
    print(payload)
    new_stabilizers = models.Stabilizer.create(**payload)
    print(new_stabilizers)
    stabilizer_dict = model_to_dict(new_stabilizers)
    return jsonify(
        data=stabilizer_dict,
        message="Successfully created stabilizer!",
        status=201
    ), 201
    return "you hit the create route -- check terminal"

@stabilizers.route('/<id>', methods=['GET'])
def get_one_stabilizer(id):
    stabilizer = models.Stabilizer.get_by_id(id)
    print(stabilizer)
    return jsonify(
        data=model_to_dict(stabilizer),
        message="Success!",
        status=200
    ), 200

@stabilizers.route('/<id>', methods=['PUT'])
def update_stabilizers(id):
    payload = request.get_json()
    print(payload)

    models.Stabilizer.update(**payload).where(models.Stabilizer.id == id).execute()

    return jsonify(
        data=model_to_dict(models.Stabilizer.get_by_id(id)),
        message="resource updated successfully",
        status=200
    ), 200

@stabilizers.route('/<id>',  methods=['DELETE'])
def delete_stabilizer(id):
    delete_query = models.Stabilizer.delete().where(models.Stabilizer.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)
    return jsonify(
        data={},
        message=f"Successfully deleted {nums_of_rows_deleted} stabilizer with id {id}",
        status=200
    ), 200