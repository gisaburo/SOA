import json
import boto3

def next(point):
    if type(point) is list:
        ftype = list
    elif type(point) is dict:
        ftype = dict
    else:
        return ftype

def main(event):
    print(type(event))
    print(type(iter(event)))
    print()
    print(event.keys())
    for i in event.keys()
        print(i)
    #print(event.values())

    '''
#   _event = json.loads(event)
    iter_event_l1 = iter(event)
    print(iter_event_l1)
    for i in iter_event_l1:
        if type(event[i]) is list:
            print('this is list A')
            #iter_event_l2 = event[i][0]
            iter_event_l3 = iter(event[i][0])
            for a in iter_event_l3:
                print(event[i][0][a])
                for 
        elif type(event[i]) is dict:
            print('this is dict A')
            iter_event_l2 = iter(event[i])
            for j in iter_event_l2:
                if type(event[i][j]) is list:
                    print('this is list B')
                elif type(event[i][j]) is dict:
                    print('this is dict B')
                    iter_event_l3 = iter(event[i][j])
                    for r in iter_event_l3:
                        if type(event[i][j][r]) is list:
                            print('this is list C')
                        elif type(event[i][j][r]) is dict:
                            print('this is dict C')
                        else:
                            print(i + ' ' + j + ' ' + r + ' : ' + str(event[i][j][r]))        
                else:
                    print(i + ' ' + j + ' : ' + str(event[i][j]))
        else:
            print(i + ' : ' + str(event[i][j]))
    '''
    '''
    print('Groups                : ' + str(event['Reservations'][0]['Groups']))
    print('ImageId               : ' + str(event['Reservations'][0]['Instances'][0]['ImageId']))
    print('InstanceId            : ' + str(event['Reservations'][0]['Instances'][0]['InstanceId']))
    print('InstanceType          : ' + str(event['Reservations'][0]['Instances'][0]['InstanceType']))
    print('KeyName               : ' + str(event['Reservations'][0]['Instances'][0]['KeyName']))
    print('LaunchTime            : ' + str(event['Reservations'][0]['Instances'][0]['LaunchTime']))
    print('Monitoring            : ' + str(event['Reservations'][0]['Instances'][0]['Monitoring']))
    print('AvailabilityZone      : ' + str(event['Reservations'][0]['Instances'][0]['Placement']['AvailabilityZone']))
    print('GroupName             : ' + str(event['Reservations'][0]['Instances'][0]['Placement']['GroupName']))
    print('Tenancy               : ' + str(event['Reservations'][0]['Instances'][0]['Placement']['Tenancy']))
    print('PrivateDnsName        : ' + str(event['Reservations'][0]['Instances'][0]['PrivateDnsName']))
    print('PrivateIpAddress      : ' + str(event['Reservations'][0]['Instances'][0]['PrivateIpAddress']))
    print('ProductCodes          : ' + str(event['Reservations'][0]['Instances'][0]['ProductCodes']))
    print('PublicDnsName         : ' + str(event['Reservations'][0]['Instances'][0]['PublicDnsName']))
    print('PublicIpAddress       : ' + str(event['Reservations'][0]['Instances'][0]['PublicIpAddress']))
    print('State                 : ' + str(event['Reservations'][0]['Instances'][0]['State']))
    print('StateTransitionReason : ' + str(event['Reservations'][0]['Instances'][0]['StateTransitionReason']))
    print('SubnetId              : ' + str(event['Reservations'][0]['Instances'][0]['SubnetId']))
    print('VpcId                 : ' + str(event['Reservations'][0]['Instances'][0]['VpcId']))
    print('Architecture          : ' + str(event['Reservations'][0]['Instances'][0]['Architecture']))
    print('BlockDeviceMappings   : ' + str(event['Reservations'][0]['Instances'][0]['BlockDeviceMappings']))
    print('ClientToken           : ' + str(event['Reservations'][0]['Instances'][0]['ClientToken']))
    print('EbsOptimized          : ' + str(event['Reservations'][0]['Instances'][0]['EbsOptimized']))
    print('EnaSupport            : ' + str(event['Reservations'][0]['Instances'][0]['EnaSupport']))
    print('Hypervisor            : ' + str(event['Reservations'][0]['Instances'][0]['Hypervisor']))
    print('NetworkInterfaces     : ' + str(event['Reservations'][0]['Instances'][0]['NetworkInterfaces']))
    print('OwnerId               : ' + str(event['Reservations'][0]['OwnerId']))
    print('ReservationId         : ' + str(event['Reservations'][0]['ReservationId']))
    '''
session = boto3.Session(profile_name='worker01')
ec2 = session.client('ec2')
response = ec2.describe_instances()
main(response)