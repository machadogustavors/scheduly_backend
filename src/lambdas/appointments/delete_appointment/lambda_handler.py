import json

from src.lib.dynamo_connection import DynamoConnection

db = DynamoConnection()

def lambda_handler(event, context):
    try:
        id = event['pathParameters']['id']
        
        result = db.delete_item('sheduly_appointments', {'id': id})
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': f'Service {id} deleted successfully'
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }