from flask import Blueprint, Response, request
import boto3
from botocore.exceptions import ClientError


s3_client = boto3.client("s3")
employee_photo = Blueprint("employee_photo", __name__)

@employee_photo.route('/peoplesuite/apis/employees/<employee_id>/photo', methods=['POST'])
def upload_employee_photo(employee_id):
    print("inside the photo upload route")
    photo_data = request.get_json()
    photo = photo_data['photo']
    print("request data ---", photo)
    
    try:
        # Check if photo already exists for the employee
        response = s3_client.head_object(Bucket='peoplesuite', Key=f'{employee_id}.jpg')
        try:
            response = s3_client.upload_file(photo, 'peoplesuite', Key=f'{employee_id}.jpg')
            return 'Photo updated successfully', 200
        except ClientError as e:
            return 'Failed to update photo', 500
    except ClientError as e:
        # Photo does not exist, proceed with upload
        try:
            response = s3_client.upload_file(photo, 'peoplesuite', Key=f'{employee_id}.jpg')
            return 'Photo uploaded successfully', 200
        except ClientError as e:
            return 'Failed to upload photo', 500

@employee_photo.route('/peoplesuite/apis/employees/<employee_id>/photo', methods=['GET'])
def get_employee_photo(employee_id):
    print("inside the photo retrieval route")
    
    try:
        response = s3_client.get_object(Bucket='peoplesuite', Key=f'{employee_id}.jpg')
        photo_data = response['Body'].read()
        return Response(photo_data, mimetype='image/jpeg')
    except ClientError as e:
        return 'Failed to retrieve photo', 500