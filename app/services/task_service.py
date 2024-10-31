# app/services/task_service.py

from app.models.task import TaskModel

class TaskService:
    @staticmethod
    def create_task(data, user_id):
        """Create a task and assign it to the authenticated user."""
        data["user_id"] = user_id
        new_task = TaskModel.create_task(data)
        return new_task

    @staticmethod
    def update_task(task_id, data, user_id):
        """Update a task only if it belongs to the authenticated user."""
        task = TaskModel.get_task(task_id)
        if task and task.get("user_id") == user_id:
            updated_task = TaskModel.update_task(task_id, data)
            return updated_task
        return None  # Unauthorized or task does not exist

    @staticmethod
    def delete_task(task_id, user_id):
        """Delete a task only if it belongs to the authenticated user."""
        task = TaskModel.get_task(task_id)
        if task and task.get("user_id") == user_id:
            TaskModel.delete_task(task_id)
            return True
        return False

    @staticmethod
    def get_task(task_id, user_id):
        """Retrieve a task if it belongs to the authenticated user."""
        task = TaskModel.get_task(task_id)
        if task and task.get("user_id") == user_id:
            return task
        return None
    
    @staticmethod
    def get_all_tasks(user_id):
        """Retrieve all tasks belonging to the authenticated user."""
        return TaskModel.get_all_tasks(user_id)
    
    
    
