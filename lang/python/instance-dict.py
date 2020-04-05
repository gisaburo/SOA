import json
import boto3

def main():
    ####################
    # session
    ####################
    session = boto3.Session(profile_name='worker01')
    ####################
    # get status
    ####################
    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    ####################
    # Judgment status
    ####################
    for i in range(len(response['Reservations'])):
        for j in range(len(response['Reservations'][i]['Instances'])):
            InstanceId = response['Reservations'][i]['Instances'][j]['InstanceId']
            if response['Reservations'][i]['Instances'][j]['State']['Name'] != 'running':
                Status = 0
            else:
                Status = 1
            ####################
            # put metrics
            ####################
            session.client('cloudwatch').put_metric_data(
                Namespace='COST_MONITOR', 
                MetricData=[
                    {
                        'MetricName': 'InstanceState',
                        'Dimensions': [
                            {
                                'Name': 'InstanceId',
                                'Value': InstanceId
                            },
                        ],
                        'Values': [
                            Status,
                        ],
                    },
                ]
            )


main()
#main(open('instance.json', 'r', encoding='utf-8'))