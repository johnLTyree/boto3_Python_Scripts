import boto3

vpc_id = "ENTER VPC ID HERE"

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)
