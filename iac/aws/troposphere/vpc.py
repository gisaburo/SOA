#!/usr/bin/python
# -*- coding: utf-8 -*-
# Converted from VPC_With_VPN_Connection.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates

from troposphere import Base64, FindInMap, GetAtt, Join, Output
from troposphere import Parameter, Ref, Tags, Template, Export, Sub
from troposphere.autoscaling import Metadata
from troposphere.ec2 import PortRange, NetworkAcl, Route, \
    VPCGatewayAttachment, SubnetRouteTableAssociation, Subnet, RouteTable, \
    VPC, NetworkInterfaceProperty, NetworkAclEntry, \
    SubnetNetworkAclAssociation, EIP, Instance, InternetGateway, \
    SecurityGroupRule, SecurityGroup, VPCGatewayAttachment, NatGateway
from troposphere.policies import CreationPolicy, ResourceSignal
from troposphere.cloudformation import Init, InitFile, InitFiles, \
    InitConfig, InitService, InitServices

t = Template()

t.add_version('2010-09-09')

t.add_description("""vpc/subnet/natgateway template""")

environmentType_param = t.add_parameter(
    Parameter(
        'EnvironmentType',
        Type='String',
        Description='Environment type',
        Default='prod',
        AllowedValues=[
            'prod','veri',
        ],
        ConstraintDescription='must be a environment type.'))

t.add_mapping(
    'prod', {
        'cidr': {'Vpc': '10.0.0.0/16',
                'Public': '10.0.0.0/24',
                'Private': '10.0.1.0/24'},
        'tags':{'Vpc': 'vpc',
                'Igw':'igw',
                'PublicSubnet':'prod-PublicSubnet',
                'PrivateSubnet':'prod-PrivateSubnet',
                'PublicRouteTable':'prod-PublicRoute',
                'PrivateRouteTable':'prod-PrivateRoute',
                'NatGateway':'prod-NatGateway'},
        'output':{'Vpc':'prod-vpc-id',
                'Igw':'prod-igw-id',
                'PublicSubnet':'prod-PublicSubnet-id',
                'PrivateSubnet':'prod-PrivateSubnet-id',
                'PublicRouteTable':'prod-PublicRoute-id',
                'PrivateRouteTable':'prod-PrivateRoute-id',
                'NatGateway':'prod-NatGateway-id'}})

t.add_mapping(
    'veri', {
        'cidr': {'Vpc': '10.0.0.0/16',
                'Public': '10.0.0.0/24',
                'Private': '10.0.1.0/24'},
        'tags':{'Vpc': 'veri-vpc',
                'Igw':'veri-igw',
                'PublicSubnet':'veri-PublicSubnet',
                'PrivateSubnet':'veri-PrivateSubnet',
                'PublicRouteTable':'veri-PublicRoute',
                'PrivateRouteTable':'veri-PrivateRoute',
                'NatGateway':'veri-NatGateway'},
        'output':{'Vpc':'veri-vpc-id',
                'Igw':'veri-igw-id',
                'PublicSubnet':'veri-PublicSubnet-id',
                'PrivateSubnet':'veri-PrivateSubnet-id',
                'PublicRouteTable':'veri-PublicRoute-id',
                'PrivateRouteTable':'veri-PrivateRoute-id',
                'NatGateway':'veri-NatGateway-id'}})

VPC = t.add_resource(
    VPC(
        'VPC',
        CidrBlock=FindInMap(
            Ref(environmentType_param),
            'cidr',
            'Vpc'),
        Tags=Tags(
            Name=FindInMap(
            Ref(environmentType_param),
            'tags',
            'Vpc'))))

PublicSubnet = t.add_resource(
    Subnet(
        'PublicSubnet',
        CidrBlock=FindInMap(
            Ref(environmentType_param),
            'cidr',
            'Public'),
        VpcId=Ref(VPC),
        Tags=Tags(
            Name=FindInMap(
            Ref(environmentType_param),
            'tags',
            'PublicSubnet'))))

PrivateSubnet = t.add_resource(
    Subnet(
        'PrivateSubnet',
        CidrBlock=FindInMap(
            Ref(environmentType_param),
            'cidr',
            'Private'),
        VpcId=Ref(VPC),
        Tags=Tags(
            Name=FindInMap(
            Ref(environmentType_param),
            'tags',
            'PrivateSubnet'))))

InternetGateway = t.add_resource(
    InternetGateway(
        'InternetGateway',
        Tags=Tags(
            Name=FindInMap(
            Ref(environmentType_param),
            'tags',
            'Igw'))))

GatewayAttachment = t.add_resource(
    VPCGatewayAttachment(
        'AttachGateway',
        VpcId=Ref(VPC),
        InternetGatewayId=Ref(InternetGateway)))

NatEip = t.add_resource(
    EIP(
        'NatEip',
        Domain="vpc"))

NatGateway = t.add_resource(
    NatGateway(
        'NatGateway',
        DependsOn='AttachGateway',
        AllocationId=GetAtt(NatEip, 'AllocationId'),
        SubnetId=Ref(PublicSubnet),
        Tags=Tags(
            Name=FindInMap(
            Ref(environmentType_param),
            'tags',
            'NatGateway'))))

PublicRouteTable = t.add_resource(
    RouteTable(
        'PublicRouteTable',
        VpcId=Ref(VPC),
        Tags=Tags(
            Name=FindInMap(
            Ref(environmentType_param),
            'tags',
            'PublicRouteTable'))))

PublicRoute = t.add_resource(
    Route(
        'PublicRoute',
        DependsOn='AttachGateway',
        GatewayId=Ref(InternetGateway),
        DestinationCidrBlock='0.0.0.0/0',
        RouteTableId=Ref(PublicRouteTable)))

PublicSubnetRouteTableAssociation = t.add_resource(
    SubnetRouteTableAssociation(
        'PublicSubnetRouteTableAssociation',
        SubnetId=Ref(PublicSubnet),
        RouteTableId=Ref(PublicRouteTable)))

PrivateRouteTable = t.add_resource(
    RouteTable(
        'PrivateRouteTable',
        VpcId=Ref(VPC),
        Tags=Tags(
            Name=FindInMap(
            Ref(environmentType_param),
            'tags',
            'PrivateRouteTable'))))

PrivateSubnetRouteTableAssociation = t.add_resource(
    SubnetRouteTableAssociation(
        'PrivateSubnetRouteTableAssociation',
        SubnetId=Ref(PrivateSubnet),
        RouteTableId=Ref(PrivateRouteTable)))

PrivateRoute = t.add_resource(
    Route(
    'PrivateRoute',
    RouteTableId=Ref(PrivateRouteTable),
    DestinationCidrBlock='0.0.0.0/0',
        NatGatewayId=Ref(NatGateway)))

t.add_output(
    Output(
        'VpcId', 
        Value=Ref(VPC), 
        Export=Export(
                FindInMap(
                    Ref(environmentType_param),
                    'output',
                    'Vpc'))))

t.add_output(
    Output(
        'InternetGatewayId',
        Value=Ref(InternetGateway), 
        Export=Export(
                FindInMap(
                    Ref(environmentType_param),
                    'output',
                    'Igw'))))

t.add_output(
    Output(
        'PublicSubnetId',
        Value=Ref(PublicSubnet), 
        Export=Export(
                FindInMap(
                    Ref(environmentType_param),
                    'output',
                    'PublicSubnet'))))

t.add_output(
    Output(
        'PrivateSubnetId',
        Value=Ref(PrivateSubnet), 
        Export=Export(
                FindInMap(
                    Ref(environmentType_param),
                    'output',
                    'PrivateSubnet'))))

t.add_output(
    Output(
        'PublicRouteTableId',
        Value=Ref(PublicRouteTable), 
        Export=Export(
                FindInMap(
                    Ref(environmentType_param),
                    'output',
                    'PublicRouteTable'))))

t.add_output(
    Output(
        'PrivateRouteTableId',
        Value=Ref(PrivateRouteTable), 
        Export=Export(
                FindInMap(
                    Ref(environmentType_param),
                    'output',
                    'PrivateRouteTable'))))

t.add_output(
    Output(
        'NatGatewayId',
        Value=Ref(NatGateway), 
        Export=Export(
                FindInMap(
                    Ref(environmentType_param),
                    'output',
                    'NatGateway'))))

print(t.to_json())

fh = open("vpc-template", "a")
fh.writelines(t.to_json())
fh.close()
