from aws_cdk import (
    core,
    aws_ec2
)

class networkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        CfnVPC=aws_ec2.CfnVPC(self,
            'CfnVPC',
            cidr_block='10.0.0.0/16',
            enable_dns_hostnames=True,
            enable_dns_support=True,
            instance_tenancy='default',
            tags=[core.CfnTag(key='Name',value='vpc')]
        )
        core.CfnOutput(self, 'CfnVPCid', value=CfnVPC.ref, export_name='CfnVPCid')

        

        CfnSubnet=aws_ec2.CfnSubnet(self,
            'CfnSubnet',
            cidr_block='10.0.0.0/24', 
            vpc_id=CfnVPC.ref,
            availability_zone='ap-northeast-1a',
            tags=[core.CfnTag(key='Name',value='CfnSubnet')]
        )
        core.CfnOutput(self, 'CfnSubnetid', value=CfnSubnet.ref, export_name='CfnSubnetid')

        