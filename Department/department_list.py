from flask import Blueprint, jsonify, request
import boto3

department_list = Blueprint("department_list", __name__)

db_client = boto3.resource('dynamodb')


@department_list.route('/peoplesuite/apis/departments', methods=['GET'])
def get_departments():
    try:
        response = db_client.scan(TableName='Department')
        departments = response['Items']
        return jsonify(departments), 200
    except Exception as e:
        return 'Failed to fetch departments', 500
    
@department_list.route('/peoplesuite/apis/departments/<department_id>/employees', methods=['GET'])
def get_department_employees(department_id):
    print("inside", department_id)
    try:
        response = db_client.query(
                TableName="Employee",
                KeyConditionExpression='DepartmentID = :department_id',
            ExpressionAttributeValues={
                ':department_id': {'S': DepartmentID}
            }
        )

        print("response,---------", response)
        department = response['Item']
        
        
        return jsonify(department), 200
    except Exception as e:
        return 'Failed to fetch department employees', 500

