import json
import datetime

from src.lib.dynamo_connection import DynamoConnection
from src.lib.utils import DecimalEncoder

from src.lambdas.appointments.update_appointment.schema import UpdateAppointmentRequest

db = DynamoConnection()

def lambda_handler(event, context):
    try:
        id = event['pathParameters']['id']
        
        body = json.loads(event['body'])
        
        request = UpdateAppointmentRequest(**body)
        
        updates = request.model_dump(exclude_unset=True)
        
        for k, v in updates.items():
            if isinstance(v, (datetime.date, datetime.datetime)):
                updates[k] = v.isoformat()
        
        result = db.update_item(
            'sheduly_appointments',
            {'id': id},
            updates
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(result, cls=DecimalEncoder)
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