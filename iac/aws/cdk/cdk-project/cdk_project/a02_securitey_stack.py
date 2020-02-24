from aws_cdk import core
from aws_cdk import aws_ec2

from vpc import VPC
from subnet import Subnet
from routetable import RouteTable

class NetworkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        vpc01 = VPC(self, 'vpc01', cidr_block='10.0.0.0/16', enable_dns_hostnames=True, enable_dns_support=True, instance_tenancy='default',
                    tags =  {'vpc': [{'key': 'AAAA','value':'test'}],'internetgateway': [{'key': 'FFFF','value':'test'}],}
                )
        Subnet(self, 'subnet01', vpc_id=vpc01.vpc, cidr_block='10.0.0.0/24', availability_zone='ap-northeast-1a')
        RouteTable(self,'routetable01', vpc_id=vpc01.vpc, internetgateway_id=vpc01.internetgateway)