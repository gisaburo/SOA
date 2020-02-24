from aws_cdk import core
from aws_cdk import aws_ec2

class Output(core.Construct):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        self._id = id
        self._value = kwargs['value']
        self._discription = kwargs['discription']
        self._export_name = kwargs['export_name']        

        core.CfnOutput(self,
            self._id,
            value=self._value.ref,
            description=self._discription,
            export_name=self._export_name
        )