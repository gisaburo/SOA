from aws_cdk import core
from aws_cdk import aws_ec2

from vpc import VPC
from internetgateway import InternetGateway
from subnet import Subnet
from routetable import RouteTable
from route import Route
from natgateway import NatGateway
from subnetroutetableassociation import SubnetRouteTableAssociation
from eip import EIP

class NetworkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # vpc network
        vpc = VPC(self, 'vpc', cidr_block='10.0.0.0/16', enable_dns_hostnames=True, enable_dns_support=True, tags=[{'key': 'Name','value':'vpc'}])
        internetgateway = InternetGateway(self, 'internetgateway', vpc_id=vpc.vpc, tags=[{'key': 'Name','value':'internetgateway'}])

        # public network
        publicsubnet01 = Subnet(self, 'publicsubnet01', vpc_id=vpc.vpc, cidr_block='10.0.0.0/24', availability_zone='ap-northeast-1a',tags=[{'key': 'Name','value':'publicsubnet01'}])
        publicsubnet02 = Subnet(self, 'publicsubnet02', vpc_id=vpc.vpc, cidr_block='10.0.1.0/24', availability_zone='ap-northeast-1c',tags=[{'key': 'Name','value':'publicsubnet02'}])
        publicsubnet03 = Subnet(self, 'publicsubnet03', vpc_id=vpc.vpc, cidr_block='10.0.2.0/24', availability_zone='ap-northeast-1d',tags=[{'key': 'Name','value':'publicsubnet03'}])
        publicroutetable01 = RouteTable(self,'publicroutetable01', vpc_id=vpc.vpc, tags=[{'key': 'Name','value':'publicroutetable01'}])
        publicroutetable02 = RouteTable(self,'publicroutetable02', vpc_id=vpc.vpc, tags=[{'key': 'Name','value':'publicroutetable02'}])
        publicroutetable03 = RouteTable(self,'publicroutetable03', vpc_id=vpc.vpc, tags=[{'key': 'Name','value':'publicroutetable03'}])
        Route(self, 'publicroute01', internetgateway_id=internetgateway.internetgateway, routetable_id=publicroutetable01.routetable)
        Route(self, 'publicroute02', internetgateway_id=internetgateway.internetgateway, routetable_id=publicroutetable02.routetable)
        Route(self, 'publicroute03', internetgateway_id=internetgateway.internetgateway, routetable_id=publicroutetable03.routetable)
        SubnetRouteTableAssociation(self, 'publicsubnetroutetableassociation01', route_table_id=publicroutetable01.routetable, subnet_id=publicsubnet01.subnet)
        SubnetRouteTableAssociation(self, 'publicsubnetroutetableassociation02', route_table_id=publicroutetable02.routetable, subnet_id=publicsubnet02.subnet)
        SubnetRouteTableAssociation(self, 'publicsubnetroutetableassociation03', route_table_id=publicroutetable03.routetable, subnet_id=publicsubnet03.subnet)

        # private network
        privatesubnet01 = Subnet(self, 'privatesubnet01', vpc_id=vpc.vpc, cidr_block='10.0.10.0/24', availability_zone='ap-northeast-1a',tags=[{'key': 'Name','value':'privatesubnet01'}])
        privatesubnet02 = Subnet(self, 'privatesubnet02', vpc_id=vpc.vpc, cidr_block='10.0.11.0/24', availability_zone='ap-northeast-1c',tags=[{'key': 'Name','value':'privatesubnet02'}])
        privatesubnet03 = Subnet(self, 'privatesubnet03', vpc_id=vpc.vpc, cidr_block='10.0.12.0/24', availability_zone='ap-northeast-1d',tags=[{'key': 'Name','value':'privatesubnet03'}])
        privateroutetable01 = RouteTable(self,'privateroutetable01', vpc_id=vpc.vpc, tags=[{'key': 'Name','value':'privateroutetable01'}])
        privateroutetable02 = RouteTable(self,'privateroutetable02', vpc_id=vpc.vpc, tags=[{'key': 'Name','value':'privateroutetable02'}])
        privateroutetable03 = RouteTable(self,'privateroutetable03', vpc_id=vpc.vpc, tags=[{'key': 'Name','value':'privateroutetable03'}])
        SubnetRouteTableAssociation(self, 'privatesubnetroutetableassociation01', route_table_id=privateroutetable01.routetable, subnet_id=privatesubnet01.subnet)
        SubnetRouteTableAssociation(self, 'privatesubnetroutetableassociation02', route_table_id=privateroutetable02.routetable, subnet_id=privatesubnet02.subnet)
        SubnetRouteTableAssociation(self, 'privatesubnetroutetableassociation03', route_table_id=privateroutetable03.routetable, subnet_id=privatesubnet03.subnet)
        eip01 = EIP(self, 'eip01', tags=[{'key': 'Name','value': 'eip01'}])
        eip02 = EIP(self, 'eip02', tags=[{'key': 'Name','value': 'eip02'}])
        eip03 = EIP(self, 'eip03', tags=[{'key': 'Name','value': 'eip03'}])
        NatGateway(self, 'natgateway01', eip_attr_allocation_id=eip01.eip, subnet_id=publicsubnet01.subnet, tags=[{'key': 'Name','value':'natgateway01'}])
        NatGateway(self, 'natgateway02', eip_attr_allocation_id=eip02.eip, subnet_id=publicsubnet02.subnet, tags=[{'key': 'Name','value':'natgateway02'}])
        NatGateway(self, 'natgateway03', eip_attr_allocation_id=eip03.eip, subnet_id=publicsubnet03.subnet, tags=[{'key': 'Name','value':'natgateway03'}])

        # isolate network
        Subnet(self, 'isolatesubnet01', vpc_id=vpc.vpc, cidr_block='10.0.20.0/24', availability_zone='ap-northeast-1a',tags=[{'key': 'Name','value':'isolatesubnet01'}])
        Subnet(self, 'isolatesubnet02', vpc_id=vpc.vpc, cidr_block='10.0.21.0/24', availability_zone='ap-northeast-1c',tags=[{'key': 'Name','value':'isolatesubnet02'}])
        Subnet(self, 'isolatesubnet03', vpc_id=vpc.vpc, cidr_block='10.0.22.0/24', availability_zone='ap-northeast-1d',tags=[{'key': 'Name','value':'isolatesubnet03'}])