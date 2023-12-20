import boto3

subnet_id = "ENTER SUBNET ID HERE"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)