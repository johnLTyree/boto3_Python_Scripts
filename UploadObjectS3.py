import boto3

s3 = boto3.client('s3')

#with open("test.txt", 'rb') as f:
    #s3.put_object(Bucket="jtyree-boto3-121923", Key="test.txt", Body=f, ContentType="text/plain")
    
s3.upload_file('test.txt', 'jtyree-boto3-121923', 'test_upload.txt', ExtraArgs={'ContentType' : 'text/plain'})