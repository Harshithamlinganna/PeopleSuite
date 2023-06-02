import boto3

dynamodb = boto3.resource('dynamodb')

def create_department_table():
    table_name = 'Department'
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'DepartmentID',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'DepartmentID',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    table.wait_until_exists()

    print(f"Table '{table_name}' is created with ARN: {table.table_arn}")

create_department_table()
