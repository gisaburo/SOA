from aws_cdk import core
from aws_cdk import aws_ec2

class NetworkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # vpc network
        vpc = aws_ec2.CfnVPC(self, 'vpc', cidr_block='10.0.0.0/16', enable_dns_hostnames=True, enable_dns_support=True, instance_tenancy='default', tags=[core.CfnTag(key='Name',value='vpc')])
        internetgateway = aws_ec2.CfnInternetGateway(self, 'internetgateway', tags=[core.CfnTag(key='Name',value='internetgateway')])
        aws_ec2.CfnVPCGatewayAttachment(self, 'VPCGatewayAttachment', vpc_id=vpc.ref, internet_gateway_id=internetgateway.ref)

        # public network
        publicsubnet01 = aws_ec2.CfnSubnet(self, 'publicsubnet01', cidr_block='10.0.0.0/24', vpc_id=vpc.ref, availability_zone='ap-northeast-1a', tags=[core.CfnTag(key='Name',value='publicsubnet01')])
        publicsubnet02 = aws_ec2.CfnSubnet(self, 'publicsubnet02', cidr_block='10.0.1.0/24', vpc_id=vpc.ref, availability_zone='ap-northeast-1c', tags=[core.CfnTag(key='Name',value='publicsubnet02')])
        publicsubnet03 = aws_ec2.CfnSubnet(self, 'publicsubnet03', cidr_block='10.0.2.0/24', vpc_id=vpc.ref, availability_zone='ap-northeast-1d', tags=[core.CfnTag(key='Name',value='publicsubnet03')])
        publicroutetable01 = aws_ec2.CfnRouteTable(self, 'publicroutetable01', vpc_id=vpc.ref, tags=[core.CfnTag(key='Name',value='publicroutetable01')])
        publicroutetable02 = aws_ec2.CfnRouteTable(self, 'publicroutetable02', vpc_id=vpc.ref, tags=[core.CfnTag(key='Name',value='publicroutetable02')])
        publicroutetable03 = aws_ec2.CfnRouteTable(self, 'publicroutetable03', vpc_id=vpc.ref, tags=[core.CfnTag(key='Name',value='publicroutetable03')])
        aws_ec2.CfnRoute(self, 'publicroute01', destination_cidr_block='0.0.0.0/0', gateway_id=internetgateway.ref, route_table_id=publicroutetable01.ref,)
        aws_ec2.CfnRoute(self, 'publicroute02', destination_cidr_block='0.0.0.0/0', gateway_id=internetgateway.ref, route_table_id=publicroutetable02.ref)
        aws_ec2.CfnRoute(self, 'publicroute03', destination_cidr_block='0.0.0.0/0', gateway_id=internetgateway.ref, route_table_id=publicroutetable03.ref)
        aws_ec2.CfnSubnetRouteTableAssociation(self, 'publicsubnetroutetableassociation01', route_table_id=publicroutetable01.ref, subnet_id=publicsubnet01.ref)
        aws_ec2.CfnSubnetRouteTableAssociation(self, 'publicsubnetroutetableassociation02', route_table_id=publicroutetable02.ref, subnet_id=publicsubnet02.ref)
        aws_ec2.CfnSubnetRouteTableAssociation(self, 'publicsubnetroutetableassociation03', route_table_id=publicroutetable03.ref, subnet_id=publicsubnet03.ref)

        # private network
        privatesubnet01 = aws_ec2.CfnSubnet(self, 'privatesubnet01', cidr_block='10.0.11.0/24', vpc_id=vpc.ref, availability_zone='ap-northeast-1a', tags=[core.CfnTag(key='Name',value='privatesubnet01')])
        privatesubnet02 = aws_ec2.CfnSubnet(self, 'privatesubnet02', cidr_block='10.0.12.0/24', vpc_id=vpc.ref, availability_zone='ap-northeast-1c', tags=[core.CfnTag(key='Name',value='privatesubnet02')])
        privatesubnet03 = aws_ec2.CfnSubnet(self, 'privatesubnet03', cidr_block='10.0.13.0/24', vpc_id=vpc.ref, availability_zone='ap-northeast-1d', tags=[core.CfnTag(key='Name',value='privatesubnet03')])
        privateroutetable01 = aws_ec2.CfnRouteTable(self, 'privateroutetable01', vpc_id=vpc.ref, tags=[core.CfnTag(key='Name',value='privateroutetable01')])
        privateroutetable02 = aws_ec2.CfnRouteTable(self, 'privateroutetable02', vpc_id=vpc.ref, tags=[core.CfnTag(key='Name',value='privateroutetable02')])
        privateroutetable03 = aws_ec2.CfnRouteTable(self, 'privateroutetable03', vpc_id=vpc.ref, tags=[core.CfnTag(key='Name',value='privateroutetable03')])
        aws_ec2.CfnSubnetRouteTableAssociation(self, 'privatesubnetroutetableassociation01', route_table_id=privateroutetable01.ref, subnet_id=privatesubnet01.ref)
        aws_ec2.CfnSubnetRouteTableAssociation(self, 'privatesubnetroutetableassociation02', route_table_id=privateroutetable02.ref, subnet_id=privatesubnet02.ref)
        aws_ec2.CfnSubnetRouteTableAssociation(self, 'privatesubnetroutetableassociation03', route_table_id=privateroutetable03.ref, subnet_id=privatesubnet03.ref)
        eip01 = aws_ec2.CfnEIP(self, 'eip01', tags=[core.CfnTag(key='Name',value='eip01')])
        eip02 = aws_ec2.CfnEIP(self, 'eip02', tags=[core.CfnTag(key='Name',value='eip02')])
        eip03 = aws_ec2.CfnEIP(self, 'eip03', tags=[core.CfnTag(key='Name',value='eip03')])
        natgateway01 = aws_ec2.CfnNatGateway(self, 'natgateway01', allocation_id=eip01.attr_allocation_id, subnet_id=publicsubnet01.ref, tags=[core.CfnTag(key='Name',value='natgateway01')])
        natgateway02 = aws_ec2.CfnNatGateway(self, 'natgateway02', allocation_id=eip02.attr_allocation_id, subnet_id=publicsubnet02.ref, tags=[core.CfnTag(key='Name',value='natgateway02')])
        natgateway03 = aws_ec2.CfnNatGateway(self, 'natgateway03', allocation_id=eip03.attr_allocation_id, subnet_id=publicsubnet03.ref, tags=[core.CfnTag(key='Name',value='natgateway03')])
        aws_ec2.CfnRoute(self, 'privateroute01', destination_cidr_block='0.0.0.0/0' ,nat_gateway_id=natgateway01.ref, route_table_id=privateroutetable01.ref) 
        aws_ec2.CfnRoute(self, 'privateroute02', destination_cidr_block='0.0.0.0/0' ,nat_gateway_id=natgateway02.ref, route_table_id=privateroutetable02.ref)
        aws_ec2.CfnRoute(self, 'privateroute03', destination_cidr_block='0.0.0.0/0' ,nat_gateway_id=natgateway03.ref, route_table_id=privateroutetable03.ref)

        # isolate network
        isolatesubnet01 = aws_ec2.CfnSubnet(self, 'isolatesubnet01', cidr_block='10.0.21.0/24', vpc_id=vpc.ref, availability_zone='ap-northeast-1a', tags=[core.CfnTag(key='Name',value='isolatesubnet01')])
        isolatesubnet02 = aws_ec2.CfnSubnet(self, 'isolatesubnet02', cidr_block='10.0.22.0/24', vpc_id=vpc.ref, availability_zone='ap-northeast-1c', tags=[core.CfnTag(key='Name',value='isolatesubnet02')])
        isolatesubnet03 = aws_ec2.CfnSubnet(self, 'isolatesubnet03', cidr_block='10.0.23.0/24', vpc_id=vpc.ref, availability_zone='ap-northeast-1d', tags=[core.CfnTag(key='Name',value='isolatesubnet03')])
        isolateroutetable01 = aws_ec2.CfnRouteTable(self, 'isolateroutetable01', vpc_id=vpc.ref, tags=[core.CfnTag(key='Name',value='isolateroutetable01')])
        isolateroutetable02 = aws_ec2.CfnRouteTable(self, 'isolateroutetable02', vpc_id=vpc.ref, tags=[core.CfnTag(key='Name',value='isolateroutetable02')])
        isolateroutetable03 = aws_ec2.CfnRouteTable(self, 'isolateroutetable03', vpc_id=vpc.ref, tags=[core.CfnTag(key='Name',value='isolateroutetable03')])
        aws_ec2.CfnSubnetRouteTableAssociation(self, 'isolatesubnetroutetableassociation01', route_table_id=isolateroutetable01.ref, subnet_id=isolatesubnet01.ref)
        aws_ec2.CfnSubnetRouteTableAssociation(self, 'isolatesubnetroutetableassociation02', route_table_id=isolateroutetable02.ref, subnet_id=isolatesubnet02.ref)
        aws_ec2.CfnSubnetRouteTableAssociation(self, 'isolatesubnetroutetableassociation03', route_table_id=isolateroutetable03.ref, subnet_id=isolatesubnet03.ref)