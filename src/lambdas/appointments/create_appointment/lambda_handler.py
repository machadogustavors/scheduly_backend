import uuid
import json

from datetime import datetime

from src.lib.dynamo_connection import DynamoConnection
from src.lib.utils import DecimalEncoder, DynamoDBConverter

from src.lambdas.appointments.create_appointment.schema import CreateAppointmentRequest

db = DynamoConnection()

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        request = CreateAppointmentRequest(**body)

        item = request.model_dump()

        item.update({
            'id': str(uuid.uuid4()),
            'created_at': datetime.now()
        })

        dynamo_item = DynamoDBConverter.to_dynamo_format(item)
        
        result = db.create_item('sheduly_appointments', dynamo_item)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(item, cls=DecimalEncoder)
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