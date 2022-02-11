import json

import boto3

# client = boto3.client('dynamodb')
TABLE_NAME = "Organization-aou76nv52bapbebq3uxerkfcce-staging"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    data = json.loads(event['body'])
    # data = event['body']
    print("------------------")
    print(data)
    print("------------------")
    response = table.put_item(Item=data)

    print("--\n----\n----\n----\n----")
    print("---------response---------")
    print(response)
    print("---------response---------")

    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'msg': "sucess"})
    }
