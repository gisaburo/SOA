from aws_cdk import (
    aws_ec2,
    core,
)

class VPC(core.Construct):

    # getter
    @property 
    def vpc(self):
        return self._vpc

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        self._id = id

        try: kwargs['cidr_block']
        except: self._cidr_block = None
        else: self._cidr_block   = kwargs['cidr_block']

        try: kwargs['enable_dns_hostnames']
        except: self._enable_dns_hostnames = None
        else: self._enable_dns_hostnames   = kwargs['enable_dns_hostnames']

        try: kwargs['enable_dns_support']
        except: self._enable_dns_support = None
        else: self._enable_dns_support   = kwargs['enable_dns_support']

        try: kwargs['instance_tenancy']
        except: self._instance_tenancy = None
        else: self._instance_tenancy   = kwargs['instance_tenancy']

        try: kwargs['tags']
        except: self._tags_wk = None
        else: self._tags_wk = [core.CfnTag(key=kwargs['tags'][i]['key'] ,value=kwargs['tags'][i]['value']) if kwargs['tags'] else None for i in range(len(kwargs['tags']))]

        self._vpc                   = aws_ec2.CfnVPC(self,
            self._id,
            cidr_block              = self._cidr_block,
            enable_dns_hostnames    = self._enable_dns_hostnames,
            enable_dns_support      = self._enable_dns_support, 
            instance_tenancy        = self._instance_tenancy, 
            tags                    = self._tags_wk
        )