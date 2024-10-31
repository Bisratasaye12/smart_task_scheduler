import boto3
import uuid

from app.utils.config import get_dynamodb_client


dynamodb = get_dynamodb_client()
table = dynamodb.Table('Tasks')

class TaskModel:
    @staticmethod
    def create_task(data):
        """Insert a new task item into DynamoDB."""
        task_id = str(uuid.uuid4())
        item = {
            "task_id": task_id,
            "user_id": data["user_id"], 
            "title": data.get("title", ""),
            "description": data.get("description", ""),
            "status": data.get("status", "pending"),
        }
        table.put_item(Item=item)
        return item

    @staticmethod
    def get_task(task_id):
        """Retrieve a task item from DynamoDB by task_id."""
        response = table.get_item(Key={"task_id": task_id})
        return response.get("Item")

    @staticmethod
    def update_task(task_id, data):
        """Update an existing task in DynamoDB."""
        update_expression = "SET"
        expression_attribute_names = {}
        expression_attribute_values = {}

        # Dynamically build the update expression, ignoring empty fields
        if "title" in data and data["title"]:
            expression_attribute_names["#t"] = "title"
            update_expression += " #t = :title,"
            expression_attribute_values[":title"] = data["title"]

        if "description" in data and data["description"]:
            expression_attribute_names["#d"] = "description"
            update_expression += " #d = :description,"
            expression_attribute_values[":description"] = data["description"]

        if "status" in data and data["status"]:
            expression_attribute_names["#s"] = "status"
            update_expression += " #s = :status,"
            expression_attribute_values[":status"] = data["status"]

        # Remove trailing comma
        update_expression = update_expression.rstrip(",")

        if update_expression == "SET":  # No fields to update
            return None

        # Perform the update
        table.update_item(
            Key={"task_id": task_id},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )
        
        return TaskModel.get_task(task_id)  # Return the updated task

    @staticmethod
    def delete_task(task_id):
        """Delete a task from DynamoDB by task_id."""
        table.delete_item(Key={"task_id": task_id})

    @staticmethod
    def get_all_tasks(user_id):
        """Retrieve all tasks for a given user ID."""
        try:
            response = table.scan(FilterExpression='user_id = :user_id', ExpressionAttributeValues={':user_id': user_id})
            return response.get('Items', [])
        except Exception as e:
            raise Exception(f"Failed to retrieve tasks: {str(e)}")
