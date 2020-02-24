from aws_cdk import core
from aws_cdk import aws_ec2

class EIP(core.Construct):

    @property # getter
    def eip(self):
        return self._eip

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        self._id = id

        try: kwargs['tags']
        except: self._tags_wk = None
        else: self._tags_wk = [core.CfnTag(key=kwargs['tags'][i]['key'] ,value=kwargs['tags'][i]['value']) if kwargs['tags'] else None for i in range(len(kwargs['tags']))]

        self._eip = aws_ec2.CfnEIP(self, self._id, tags=self._tags_wk)