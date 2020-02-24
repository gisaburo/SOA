from aws_cdk import core
from aws_cdk import aws_ec2

class NatGateway(core.Construct):

    @property # getter
    def natgateway(self):
        return self._natgateway

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        self._id = id
        self._eip = kwargs['eip_attr_allocation_id']
        self._subnet_id = kwargs['subnet_id']

        try: kwargs['tags']
        except: self._tags_wk = None
        else: self._tags_wk = [core.CfnTag(key=kwargs['tags'][i]['key'] ,value=kwargs['tags'][i]['value']) if kwargs['tags'] else None for i in range(len(kwargs['tags']))]
    
        self._natgateway = aws_ec2.CfnNatGateway(self,
            self._id,
            allocation_id=self._eip.attr_allocation_id,
            subnet_id=self._subnet_id.ref,
            tags=self._tags_wk
        )