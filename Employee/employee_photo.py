#!/bin/bash
import io
from flask import Blueprint,request, send_file
import boto3
from botocore.exceptions import ClientError


s3_client = boto3.client("s3", region_name='us-west-1')

employee_photo = Blueprint("employee_photo", __name__)
bucket_name = "peoplesuite"

@employee_photo.route('/peoplesuite/apis/employees/<EmployeeID>/photo', methods=['POST'])
def upload_employee_photo(EmployeeID):
    photo_data = request.data    
    try:
        # Check if photo already exists for the employee
        s3_client.head_object(Bucket='peoplesuite', Key=f'{EmployeeID}.jpg')
        try:
            with io.BytesIO(photo_data) as file: #BytesIO class from the io module to create a file-like object from the binary data.
                s3_client.upload_fileobj(file, bucket_name, Key=f'{EmployeeID}.jpg')
            return 'Photo updated successfully', 200
        except ClientError as e:
            return 'Failed to update photo', 500
    except ClientError as e:
        try:
            with io.BytesIO(photo_data) as file:
                s3_client.upload_fileobj(file, bucket_name, Key=f'{EmployeeID}.jpg')
            return 'Photo uploaded successfully', 200
        except ClientError as e:
            return 'Failed to upload photo', 500


@employee_photo.route('/peoplesuite/apis/employees/<EmployeeID>/photo', methods=['GET'])
def get_employee_photo(EmployeeID):
    try:
        photo_url = s3_client.generate_presigned_url('get_object', 
                                                     Params={'Bucket': bucket_name, 
                                                             'Key': f'{EmployeeID}.jpg'}, 
                                                     ExpiresIn=3600)
        response = s3_client.get_object(Bucket=bucket_name, Key=f'{EmployeeID}.jpg')
        photo_data = response['Body'].read()
        
        # Create a response with the photo data
        return send_file(io.BytesIO(photo_data), mimetype='image/jpeg')
    
    except ClientError as e:
        return 'Failed to retrieve photo', 500


