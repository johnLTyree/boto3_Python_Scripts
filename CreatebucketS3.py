import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='jtyree-boto3-121923'
    )

print(response)