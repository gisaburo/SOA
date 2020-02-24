from aws_cdk import (
    aws_ec2,
    core,
)

class InternetGateway(core.Construct):

    @property
    def internetgateway(self):
        return self._internetgateway

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        self._id = id
        self._vpc_id = kwargs['vpc_id']
        self._tags = kwargs['tags']

        try: kwargs['tags']
        except: self._tags_wk = None
        else: self._tags_wk = [core.CfnTag(key=kwargs['tags'][i]['key'] ,value=kwargs['tags'][i]['value']) if kwargs['tags'] else None for i in range(len(kwargs['tags']))]

        self._internetgateway = aws_ec2.CfnInternetGateway(self,
                                self._id,
                                tags=self._tags_wk
        )

        aws_ec2.CfnVPCGatewayAttachment(self,
            'VPCGatewayAttachment',
            vpc_id=self._vpc_id.ref,
            internet_gateway_id=self._internetgateway.ref,
            )