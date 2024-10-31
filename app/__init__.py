from flask import Flask
from app.utils.config import get_dynamodb_client
from app.controllers.auth_controller import auth_bp
from app.controllers.task_controller import task_bp

dynamodb = get_dynamodb_client()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(task_bp, url_prefix='/api/v1')

    with app.app_context():
        initialize_tables()

    return app

def initialize_tables():
    tables_to_create = [
        {
            'name': 'Tasks',
            'key_schema': [
                {'AttributeName': 'task_id', 'KeyType': 'HASH'},
            ],
            'attribute_definitions': [
                {'AttributeName': 'task_id', 'AttributeType': 'S'},
            ],
        },
        {
            'name': 'Users',
            'key_schema': [
                {'AttributeName': 'username', 'KeyType': 'HASH'},
            ],
            'attribute_definitions': [
                {'AttributeName': 'username', 'AttributeType': 'S'},
            ],
        }
    ]
    
    existing_tables = [table.name for table in dynamodb.tables.all()]
    
    for table_info in tables_to_create:
        if table_info['name'] not in existing_tables:
            table = dynamodb.create_table(
                TableName=table_info['name'],
                KeySchema=table_info['key_schema'],
                AttributeDefinitions=table_info['attribute_definitions'],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            table.wait_until_exists()
            print(f"Created table '{table_info['name']}' successfully.")
        else:
            print(f"Table '{table_info['name']}' already exists.")
