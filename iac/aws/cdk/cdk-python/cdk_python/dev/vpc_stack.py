import sys
from aws_cdk import (
    core,
)

sys.path.append('../resources/')
from resources import vpc

class vpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # vpc create -------------------------------
        vpcObj = vpc.create_vpc(self, id, tags='vpc01')
        # internet gateway create ------------------
        vpc.create_internet_gateway(self, vpcObj)