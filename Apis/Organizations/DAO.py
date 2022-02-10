"""contract/dao_contract.py

DAO para o Contratos.
"""
import base64
import logging
import os
import time
import uuid
from datetime import datetime

from boto3 import resource as boto_resource
from boto3.dynamodb.conditions import Key
from botocore import exceptions as boto_exceptions

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL") or logging.NOTSET

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name
logger.setLevel(LOGGING_LEVEL)

dynamodb = boto_resource("dynamodb")

import boto3

client = boto3.client('dynamodb')

TABLE_NAME = "Organization-aou76nv52bapbebq3uxerkfcce-staging"


def create_id():
    """Cria um id único"""
    return base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("utf-8").replace("=", "")


def logger_warning(exc):
    logger.warning("não foi possivel recuperar o recurso: %s", exc, exc_info=1)


class ContractDao:
    CONTRACT_TABLE_NAME = os.getenv("DB_CONTRACT")

    def __init__(self):
        """Inicialização da classe."""
        self._contract_table = dynamodb.Table(self.CONTRACT_TABLE_NAME)

    def get(self, id):
        """Retorna um contrato"""

        try:
            response = client.query(TABLE_NAME=TABLE_NAME, KeyConditionExpression=Key("id").eq(id))
        except boto_exceptions.ClientError as exc:
            logger_warning(exc)
            return None

        if not response["Items"]:
            return None
        else:
            return response["Items"][0]

    def update(self, cid, update_expression, expression_attribute_values):
        try:
            self._contract_table.update_item(
                Key={"id": cid, },
                UpdateExpression="set " + ", ".join(update_expression),
                ExpressionAttributeValues={**expression_attribute_values},
                ReturnValues="UPDATED_NEW"
            )

        except boto_exceptions.ClientError as exc:
            logger_warning(exc)
            return None

    def create(self, item):
        try:
            ttl = (15 * 24 * 60 * 60) + int(time.time())
            item["id"] = create_id()
            item["createdAt"] = str(datetime.timestamp(datetime.now()))

            resp = client.put_item(TABLE_NAME=TABLE_NAME, Item=item)
            return uuid
        except boto_exceptions.ClientError as exc:
            logger_warning(exc)
    def scan():
        data = client.scan(TableName=TABLE_NAME)
