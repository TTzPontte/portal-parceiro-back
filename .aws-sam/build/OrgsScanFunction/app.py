import json

import boto3

client = boto3.client('dynamodb')

TABLE_NAME = "Organization-aou76nv52bapbebq3uxerkfcce-staging"


def lambda_handler(event, context):
    data = client.scan(TableName=TABLE_NAME)
    print("----------------------------------")
    print("TABLE_NAME", TABLE_NAME)
    print("----------------------------------")
    response = {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return response
