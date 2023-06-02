import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Department')

def populate_employee_data():
    departments = [
        {
            'DepartmentID': 'IT',
            'CostCenter': '1234567890',
            'ParentDepartmentID': None
        },
        {
            'DepartmentID': 'Finance',
            'CostCenter': '9876543210',
            'ParentDepartmentID': None
        },
        {
            'DepartmentID': 'Sales',
            'CostCenter': '5555555555',
            'ParentDepartmentID': None
        },
        # Add more departments as needed
    ]

    with table.batch_writer() as batch:
        for department in departments:
            batch.put_item(Item=department)

    print('Data population completed.')

populate_employee_data()
