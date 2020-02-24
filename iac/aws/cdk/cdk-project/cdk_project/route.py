from aws_cdk import core
from aws_cdk import aws_ec2

class Route(core.Construct):

    @property # getter
    def route(self):
        return self._route

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        self._id = id
        self._routetable_id = kwargs['routetable_id']
        self._internetgateway_id = kwargs['internetgateway_id']

        try: kwargs['tags']
        except: self._tags_wk = None
        else: self._tags_wk = [core.CfnTag(key=kwargs['tags'][i]['key'] ,value=kwargs['tags'][i]['value']) if kwargs['tags'] else None for i in range(len(kwargs['tags']))]

        self._internetgateway_id = kwargs['internetgateway_id']
        self._route = aws_ec2.CfnRoute(self,
            self._id,
            gateway_id=self._internetgateway_id.ref,
            destination_cidr_block='0.0.0.0/0',
            route_table_id=self._routetable_id.ref
        )