import boto3

def filter_objects_extension(client, extension):
    keys = []
    response = client.list_objcts_v2(Bucket="jtyree-boto3-121923")
    for content in response["Contents"]:
        if(extension in content["Key"][-(len(extension)):]):
            keys.append(content["Key"])
           
    
s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket="jtyree-boto3-121923")

extension = ".txt"

