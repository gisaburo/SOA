from aws_cdk import core
from aws_cdk import aws_ec2

class RouteTable(core.Construct):

    @property # getter
    def routetable(self):
        return self._routetable

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        self._id = id
        self._vpc_id = kwargs['vpc_id']

        try: kwargs['tags']
        except: self._tags_wk = None
        else: self._tags_wk = [core.CfnTag(key=kwargs['tags'][i]['key'] ,value=kwargs['tags'][i]['value']) if kwargs['tags'] else None for i in range(len(kwargs['tags']))]

        self._routetable = aws_ec2.CfnRouteTable(self,
                    self._id,
                    vpc_id=self._vpc_id.ref,
                    tags=self._tags_wk
                )