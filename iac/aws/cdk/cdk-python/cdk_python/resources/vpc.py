from aws_cdk import (
    core,
    aws_ec2,
)
 
 
def create_vpc(scope: core.Construct) -> None:
    vpc = aws_ec2.CfnVPC(scope, 
        id='vpc01',
        cidr_block='10.0.0.0/16',
        enable_dns_hostnames=True,
        enable_dns_support=True,
        tags=[core.CfnTag(
            key='Name',
            value='vpc01',
        )]
    )
 
    return vpc