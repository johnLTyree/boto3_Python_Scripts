import boto3

route_table_id = "ENTER ROUTE TABLE ID HERE"

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)
