import boto3

route_table_id = 'PLACE ROUTE TABLE ID HERE'
subnet_id = 'PLACE SUBNET ID HERE'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table-id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])