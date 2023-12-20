import boto3

vpc_id = 'VPC ID HERE'

ec2 = boto3.client('ec2')

routeTable = ec2.create_route-table(VpcId=vpc_id)

print(routeTable["RouteTable"]["RouteTableId"])