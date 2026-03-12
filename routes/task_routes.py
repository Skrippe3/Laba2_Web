from flask import Blueprint, request, jsonify
from app.services.task_service import TaskService

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    if page < 1 or limit < 1 or limit > 100:
        return jsonify({"message": "Invalid pagination params"}), 400

    result = TaskService.get_all(page, limit)
    return jsonify(result), 200

@task_bp.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id):
    task = TaskService.get_one(task_id)
    if not task:
        return jsonify({"message": "Task not found"}), 404
    return jsonify(task.to_dict()), 200

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data or "description" not in data:
        return jsonify({"message": "Invalid data"}), 400

    task = TaskService.create(data)
    return jsonify(task.to_dict()), 201

@task_bp.route("/tasks/<task_id>", methods=["PUT"])
def update_task_put(task_id):
    data = request.get_json()

    if not data or "title" not in data or "description" not in data or "status" not in data:
        return jsonify({"message": "Invalid data"}), 400

    task = TaskService.update_put(task_id, data)
    if not task:
        return jsonify({"message": "Task not found"}), 404

    return jsonify(task.to_dict()), 200

@task_bp.route("/tasks/<task_id>", methods=["PATCH"])
def update_task_patch(task_id):
    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid data"}), 400

    task = TaskService.update_patch(task_id, data)
    if not task:
        return jsonify({"message": "Task not found"}), 404

    return jsonify(task.to_dict()), 200

@task_bp.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = TaskService.soft_delete(task_id)
    if not task:
        return jsonify({"message": "Task not found"}), 404

    return "", 204