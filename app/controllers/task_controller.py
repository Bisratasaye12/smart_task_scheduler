from flask import Blueprint, jsonify, request
from app.services.task_service import TaskService
from app.utils.auth_middleware import token_required

task_bp = Blueprint("task", __name__)

@task_bp.route("/tasks", methods=["POST"])
@token_required
def create_task(user_id):
    """Create a new task associated with the authenticated user."""
    data = request.json
    task = TaskService.create_task(data, user_id)
    return jsonify(task), 201

@task_bp.route("/tasks/<string:task_id>", methods=["PUT"])
@token_required
def update_task(task_id, user_id):
    """Update an existing task, checking user ownership."""
    data = request.json
    task = TaskService.update_task(task_id, data, user_id)
    return jsonify(task), 200

@task_bp.route("/tasks/<string:task_id>", methods=["DELETE"])
@token_required
def delete_task(task_id, user_id):
    """Delete a task if the user is the owner."""
    result = TaskService.delete_task(task_id, user_id)
    if result:
        return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"error": "Task not found or access denied"}), 404

@task_bp.route("/tasks/<string:task_id>", methods=["GET"])
@token_required
def get_task(task_id, user_id):
    """Retrieve a task if it belongs to the authenticated user."""
    task = TaskService.get_task(task_id, user_id)
    if task:
        return jsonify(task), 200
    return jsonify({"error": "Task not found or access denied"}), 404

@task_bp.route("/tasks", methods=["GET"])
@token_required
def get_all_tasks(user_id):
    """Retrieve all tasks for the authenticated user."""
    tasks = TaskService.get_all_tasks(user_id)
    return jsonify(tasks), 200