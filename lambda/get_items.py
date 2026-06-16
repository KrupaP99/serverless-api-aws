import json
import boto3
from boto3.dynamodb.conditions import Attr

def lambda_handler(event, context):
    try:
        db = boto3.resource('dynamodb')
        table = db.Table('Items')
        
        query_params = event.get('queryStringParameters')
        
        if query_params and 'category' in query_params:
            category = query_params['category']
            result = table.scan(
                FilterExpression=Attr('category').eq(category)
            )
        else:
            result = table.scan()
        
        items = sorted(result['Items'], key=lambda x: x.get('name', '').lower())
        
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }