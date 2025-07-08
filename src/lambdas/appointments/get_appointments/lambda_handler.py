import json

from src.lib.dynamo_connection import DynamoConnection
from src.lib.utils import DecimalEncoder, DynamoDBConverter

from src.lambdas.appointments.get_appointments.schema import Appointment

db = DynamoConnection()

def lambda_handler(event, context):
    try:
        items = db.get_all_items('sheduly_appointments')

        py_items = [DynamoDBConverter.from_dynamo_format(item) for item in items]

        appointments = [Appointment(**item) for item in py_items]
        
        appointments_dict = [appointment.model_dump() for appointment in appointments]

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(appointments_dict, cls=DecimalEncoder)
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