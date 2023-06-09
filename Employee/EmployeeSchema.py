#!/bin/bash
import boto3

dynamodb = boto3.client('dynamodb')

def create_table():
    response = dynamodb.create_table(
        TableName='Employee',
        KeySchema=[
            {'AttributeName': 'EmployeeID', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
        {
            'AttributeName': 'EmployeeID',
            'AttributeType': 'N'
        }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print("Table created successfully:", response['TableDescription']['TableName'])

create_table()
