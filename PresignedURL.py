import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': "jtyree-boto3-121923",
                                                            'Key': "test.txt"}, 
                                                    ExpiresIn=300)
print(response)