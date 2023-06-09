#!/bin/bash
from flask import Blueprint, jsonify, request
import boto3

employee_profile = Blueprint("employee_profile", __name__)

# Create a DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-west-1')


employee_table = dynamodb.Table('Employee')

# GET operation to view an employee's profile
@employee_profile.route('/peoplesuite/apis/employees/<EmployeeID>/profile', methods=['GET'])
def view_employee_profile(EmployeeID):
    print("employee id", type(EmployeeID))
    response = employee_table.get_item(Key={'EmployeeID': int(EmployeeID)})
    print("response --", response)
    if 'Item' in response:
        print("response --", response)
        profile_data = response['Item']
        return jsonify(profile_data)
    else:
        return jsonify({'message': 'Employee profile not found.'}), 404

# POST operation to create an employee's profile
@employee_profile.route('/peoplesuite/apis/employees/<EmployeeID>/profile', methods=['POST'])
def create_employee_profile(EmployeeID):
    profile_data = request.get_json()
    print("profile data --", profile_data)
    profile_data['EmployeeID'] = int(EmployeeID)
    print("emploee", type(EmployeeID))
    employee_table.put_item(Item=profile_data)
    return jsonify({'message': 'Employee profile created successfully.'}), 201
