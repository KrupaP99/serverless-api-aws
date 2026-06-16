import json
import boto3
import uuid

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        
        if 'name' not in body or 'price' not in body:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'name and price are required fields'})
            }
        
        if not body['name'] or not body['price']:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'name and price cannot be empty'})
            }
        
        body['id'] = str(uuid.uuid4())
        boto3.resource('dynamodb').Table('Items').put_item(Item=body)
        
        return {
            'statusCode': 201,
            'body': json.dumps(body)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }