import boto3

s3 = boto3.client('s3')

s3.upload_file('test.txt', 'jtyree-boto3-121923', 'test_upload.txt', ExtraArgs={'ContentType' : 'text/plain'})
