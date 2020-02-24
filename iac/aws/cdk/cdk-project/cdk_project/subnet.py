from aws_cdk import (
    aws_ec2,
    core,
)

class Subnet(core.Construct):

    @property # getter
    def subnet(self):
        return self._subnet

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        self._id = id
        self._cidr_block = kwargs['cidr_block']
        self._vpc_id = kwargs['vpc_id']
        self._availability_zone = kwargs['availability_zone']

        try: kwargs['tags']
        except: self._tags_wk = None
        else: self._tags_wk = [core.CfnTag(key=kwargs['tags'][i]['key'] ,value=kwargs['tags'][i]['value']) if kwargs['tags'] else None for i in range(len(kwargs['tags']))]

        self._subnet = aws_ec2.CfnSubnet(self,
                self._id,
                cidr_block=self._cidr_block,
                vpc_id=self._vpc_id.ref,
                availability_zone=self._availability_zone,
                tags=self._tags_wk
            )