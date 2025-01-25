import boto3

client = boto3.client('apigateway')

response = client.create_rest_api(
    name='testing-rest-api',
    description='Testing API',
    version='1.0',
    apiKeySource='HEADER',  # Options: HEADER | AUTHORIZER
    endpointConfiguration={
        'types': ['REGIONAL'],  # Options: EDGE | REGIONAL | PRIVATE
    },
    tags={
        'Environment': 'Testing',
        'Project': 'Demo'
    },
    disableExecuteApiEndpoint=True  # Disables the default endpoint
)

print("REST API created:", response)

response = client.create_resource(
    restApiId='i8jct462cl',
    parentId='9emxlodrf0',
    pathPart='{proxy+}'
)