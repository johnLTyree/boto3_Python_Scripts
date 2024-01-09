import boto3

def stop_all_ec2_instances():
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Retrieve all running instances
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    # Extract instance IDs
    instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

    # Stop all running instances
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped instances: {', '.join(instance_ids)}")
    else:
        print("No running instances to stop.")

if __name__ == "__main__":
    stop_all_ec2_instances()