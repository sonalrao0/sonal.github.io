import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TaskTable')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        task_id = body['task_id']
        task_name = body['task_name']
        task_status = body['task_status']

        table.put_item(
            Item={
                'task_id': task_id,
                'task_name': task_name,
                'task_status': task_status
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Task created successfully!')
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {e.response['Error']['Message']}")
        }
