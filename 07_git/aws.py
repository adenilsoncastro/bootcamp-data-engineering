# %%
import boto3
from botocore import exceptions
import botocore
from botocore.exceptions import ClientError
import logging
from botocore.retries import bucket
from dotenv import load_dotenv
from os import getenv


# %%
load_dotenv('.env')

# %%
# getenv('AWS_ID')
getenv('AWS_KEY')

# %%
# s3_client = boto3.client(
#     's3',
#     aws_access_key_id=getenv('AWS_ID'),
#     aws_secret_access_key=getenv('AWS_ID'),
#     region_name='us-west-2')

s3_client = boto3.client('s3')


# %%

def create_bucket(name: str):
    try:
        s3_client.create_bucket(Bucket=name, CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2'})
    except ClientError as e:
        logging.error(e)
        return False

    return True


# %%
create_bucket(name='afc-s3-test2')
