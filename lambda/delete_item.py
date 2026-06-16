import json
import boto3

def lambda_handler(event, context):
    try:
        db = boto3.resource('dynamodb')
        table = db.Table('Items')
        
        item_id = event['pathParameters']['id']
        table.delete_item(Key={'id': item_id})
        
        return {
            'statusCode': 200,
            'body': json.dumps({'deleted': item_id})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }