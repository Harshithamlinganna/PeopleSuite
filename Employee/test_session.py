import boto3

# Create a session
session = boto3.Session()

# Get the frozen credentials
credentials = session.get_credentials().get_frozen_credentials()

# Print the credentials
print("Access Key:", credentials.access_key)
print("Secret Key:", credentials.secret_key)
print("Session Token:", credentials.token if credentials.token is not None else "No session token available")
