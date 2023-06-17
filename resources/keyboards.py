import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
# from flask_login import login_required
from flask_cors import CORS

keyboards = Blueprint("keyboards", "keyboards")
keyboard = Blueprint("keyboard", "keyboard")

@keyboards.route("/index", methods=["GET"])
# @login_required
def keyboards_index():
    result = models.Keyboard.select()
    print("results of keyboard select query")
    print(result)

    keyboard_dicts = [model_to_dict(keyboard) for keyboard in result]
    
    return jsonify({
        "data": keyboard_dicts,
        "message": f"Successfully found {len(keyboard_dicts)} keyboards",
        "status": 200
    }), 200

@keyboards.route("/", methods=["POST"])
def create_keyboards():
    payload = request.get_json()
    print(payload)
    new_keyboards = models.Keyboard.create(**payload)
    print(new_keyboards)
    keyboard_dict = model_to_dict(new_keyboards)
    return jsonify(
        data=keyboard_dict,
        message="Successfully created keyboard!",
        status=201
    ), 201
    return "you hit the create route -- check terminal"

@keyboards.route("/<id>", methods=["GET"])
def get_one_keyboard(id):
    keyboard = models.Keyboard.get_by_id(id)
    print(keyboard)
    return jsonify(
        data=model_to_dict(keyboard),
        message="Success!",
        status=200
    ), 200

@keyboards.route("/<id>", methods=["PUT"])
def update_keyboards(id):
    payload = request.get_json()
    print(payload)

    models.Keyboard.update(**payload).where(models.Keyboard.id == id).execute()

    return jsonify(
        data=model_to_dict(models.Keyboard.get_by_id(id)),
        message="resource updated successfully",
        status=200
    ), 200

@keyboards.route("/<id>",  methods=["DELETE"])
def delete_keyboard(id):
    delete_query = models.Keyboard.delete().where(models.Keyboard.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)
    return jsonify(
        data={},
        message=f"Successfully deleted {nums_of_rows_deleted} keyboard with id {id}",
        status=200
    ), 200