import boto3

internet_gateway_id = 'ENTER INTERNET GATEWAY ID HERE'
vpc_id = 'ENTER VPC ID HERE'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)