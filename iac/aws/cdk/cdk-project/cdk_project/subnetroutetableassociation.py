from aws_cdk import core
from aws_cdk import aws_ec2

class SubnetRouteTableAssociation(core.Construct):

    @property # getter
    def subnetroutetableassociation(self):
        return self._subnetroutetableassociation

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        self._id = id
        self._route_table_id = kwargs['route_table_id']
        self._subnet_id = kwargs['subnet_id']

        try: kwargs['tags']
        except: self._tags_wk = None
        else: self._tags_wk = [core.CfnTag(key=kwargs['tags'][i]['key'] ,value=kwargs['tags'][i]['value']) if kwargs['tags'] else None for i in range(len(kwargs['tags']))]

        self._subnetroutetableassociation = aws_ec2.CfnSubnetRouteTableAssociation(self,
            self._id,
            route_table_id=self._route_table_id.ref,
            subnet_id=self._subnet_id.ref
        )