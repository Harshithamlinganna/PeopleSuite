from flask import Blueprint, jsonify, request
from boto3.dynamodb.conditions import Key
import boto3

department_list = Blueprint("department_list", __name__)

db_client = boto3.resource('dynamodb', region_name='us-west-1')


@department_list.route('/peoplesuite/apis/departments', methods=['GET'])
def get_departments():
    try:
        department_table = db_client.Table('Department')
        response = department_table.scan( )
        print("responses---", response)
        departments = response['Items']
        print("departments", type(departments))
        return jsonify(departments), 200
    except Exception as e:
        return 'Failed to fetch departments', e, 500
    
@department_list.route('/peoplesuite/apis/departments/<departmentId>/employees', methods=['GET'])
def get_department_employees(departmentId):
    try:
        employee_table = db_client.Table('Employee')
        # Query the Employee table based on departmentId
        response = employee_table.scan(
            FilterExpression=Key('DepartmentID').eq(departmentId)
        )
        employees = response['Items']
        # Extract relevant employee information (Employee ID, Employee Name, Employee Profile URL)
        employee_data = [
        {
            'EmployeeID': employee['EmployeeID'],
            'EmployeeName': f"{employee['FirstName']} {employee['LastName']}",
            'ProfileURL': f"/peoplesuite/apis/employees/{employee['EmployeeID']}/profile",
        }
             for employee in employees
        ]


        return jsonify(employee_data), 200
    except Exception as e:
        return 'Failed to fetch department employees', 500


