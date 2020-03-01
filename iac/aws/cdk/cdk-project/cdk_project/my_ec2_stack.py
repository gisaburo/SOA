from aws_cdk import core
from aws_cdk import aws_ec2

class EC2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        # ImageId
        # The code that defines your stack goes here
        # image: fedora
        aws_ec2.CfnLaunchTemplate(self, 'template01', launch_template_data=None, launch_template_name='template01')
        # bastion
        # aws_ec2.CfnInstance(self, 'instance01', availability_zone=, block_device_mappings=, key_name=, instance_type=,iam_instance_profile=, security_group_ids=, launch_template= , tags=)
        # ami-0d8e872ddc3206741
        # private