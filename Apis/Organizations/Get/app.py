import json

import boto3
from boto3.dynamodb.conditions import Key

# client = boto3.client('dynamodb')
TABLE_NAME = "Organization-aou76nv52bapbebq3uxerkfcce-staging"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def get(id):
    response = table.query(KeyConditionExpression=Key("id").eq(id))
    if not response["Items"]:
        return None
    return response["Items"][0]


def lambda_handler(event, context):
    path_parameters = event.get('pathParameters', None)
    uuid = path_parameters.get("id", None)

    data = json.loads(event['body'])
    # data = event['body']
    print("------------------")
    print(data)
    print("------------------")
    response = get(uuid)
    print("--\n----\n----\n----\n----")
    print("---------response---------")
    print(response)
    print("---------response---------")

    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'msg': "sucess"})
    }
