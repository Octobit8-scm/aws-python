import boto3
import os
from botocore.config import Config

#configure using config object

aws_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts' : 10,
        'mode' : 'standard'
    }
)

