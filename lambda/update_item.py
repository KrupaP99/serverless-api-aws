
import json
import boto3

def lambda_handler(event, context):
    try:
        db = boto3.resource('dynamodb')
        table = db.Table('Items')
        
        item_id = event['pathParameters']['id']
        body = json.loads(event['body'])
        
        if not body:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Request body cannot be empty'})
            }
        
        update_expression = 'SET ' + ', '.join(f'#k{i} = :v{i}' for i, k in enumerate(body))
        expression_names = {f'#k{i}': k for i, k in enumerate(body)}
        expression_values = {f':v{i}': v for i, (k, v) in enumerate(body.items())}
        
        table.update_item(
            Key={'id': item_id},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_names,
            ExpressionAttributeValues=expression_values
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'updated': item_id, 'fields': body})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }