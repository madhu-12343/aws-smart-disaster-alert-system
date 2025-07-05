import json
import boto3
import uuid
from datetime import datetime

sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DisasterAlerts')

SNS_TOPIC_ARN = 'arn:aws:sns:eu-north-1:026900513869:DisasteralertTopic'

def lambda_handler(event, context):
    time_str = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    msg = f"🚨 Test Earthquake Alert!\nLocation: TestCity\nMagnitude: 6.5\nTime: {time_str}"

    table.put_item(Item={
        'alertId': str(uuid.uuid4()),
        'type': 'Earthquake',
        'location': "TestCity",
        'message': msg,
        'time': time_str
    })

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=msg,
        Subject="🚨 Test Disaster Alert"
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'test_alert_sent': msg})
    }