import boto3

def empty_bucket(client, bucket):
    response = client.list_objects_v2(Bucket=bucket)
    
s3 = boto3.client('s3')

bucket = "jtyree-boto3-121923"

response = s3.delete_bucket(
    Bucket=bucket)