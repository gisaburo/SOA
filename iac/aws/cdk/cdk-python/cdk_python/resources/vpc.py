from aws_cdk import (
    core,
    aws_ec2
)

def create_vpc(scope: core.Construct, id: str, *,
        cidr_block='10.0.0.0/16',
        enable_dns_hostnames=True,
        enable_dns_support=True,
        instance_tenancy='default',
        tags='vpc01') -> aws_ec2.CfnVPC:

    vpc = aws_ec2.CfnVPC(scope, 'vpc',
        cidr_block=cidr_block,
        enable_dns_hostnames=enable_dns_hostnames,
        enable_dns_support=enable_dns_support,
        tags=[core.CfnTag(
            key='Name',
            value=tags,
        )]
    )
 
    return vpc

def create_internet_gateway(scope: core.Construct, vpc: aws_ec2.CfnVPC) -> aws_ec2.CfnInternetGateway:

    internet_gateway = aws_ec2.CfnInternetGateway(scope, 'InternetGateway',
        tags=[core.CfnTag(
            key='Name',
            value='InternetGateway',
        )]
    )
    
    aws_ec2.CfnVPCGatewayAttachment(scope, 'VPCGatewayAttachment',
        vpc_id=vpc.ref,
        internet_gateway_id=internet_gateway.ref,
    )
    
    return internet_gateway