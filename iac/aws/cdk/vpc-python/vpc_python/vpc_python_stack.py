from aws_cdk import (
    aws_ec2,
    core,
)
class VpcPythonStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = aws_ec2.CfnVPC(
            self,
            id='vpc',
            cidr_block='10.0.0.0/16',
            enable_dns_hostnames=True,
            enable_dns_support=True,
            instance_tenancy='dafault',
            tags=[
                core.CfnTag(key='Name', value='vpc')
            ]
        )
