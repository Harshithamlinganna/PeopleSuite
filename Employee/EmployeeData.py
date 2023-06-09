#!/bin/bash
import boto3
import random

dynamodb = boto3.resource('dynamodb')
employee_table = dynamodb.Table('Employee')

def generate_employee_id():
    return random.randint(1000000, 9999999)

def populate_employee_data():
    employees = [
        {
            'EmployeeID': generate_employee_id(),
            'FirstName': 'Harshitha',
            'LastName': 'Madhugiri Linganna',
            'StartDate': '2022-01-01',
            'Country': 'US',
            'DepartmentID': 'CS',
            'Title': 'Software Engineer',
            'ManagerID': None,
            'ManagerName': None
        },
        {
            'EmployeeID': generate_employee_id(),
            'FirstName': 'Chavan',
            'LastName': 'Maharshi',
            'StartDate': '2022-02-01',
            'Country': 'CA',
            'DepartmentID': 'CS',
            'Title': 'Software development Manager',
            'ManagerID': generate_employee_id(),
            'ManagerName': 'John Doe'
        },
        # Add more employee data as needed
    ]

    with employee_table.batch_writer() as batch:
        for employee in employees:
            batch.put_item(Item=employee)

    print("Employee data populated successfully.")

populate_employee_data()
