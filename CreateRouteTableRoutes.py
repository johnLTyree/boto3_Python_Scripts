import boto3

route_table_id = "ENTER ROUTE TABLE ID HERE"
internet_gateway_id = "ENTER INTERNET GATEWAY ID HERE"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)
