import boto3

internet_gatway_id = "ENTER IG HERE"

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)