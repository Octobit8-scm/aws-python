import boto3

client = boto3.client('iam')

response = client.list_roles()
print(response)