from aws_cdk import core
from aws_cdk import aws_ec2

class EC2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        # launchtemplate
        # https://aws.amazon.com/marketplace/pp/B00O7WM7QW ami-06a46da680048c8ae
        template01=aws_ec2.CfnLaunchTemplate(self, 'template01',
            launch_template_data={'imageId':'ami-06a46da680048c8ae', 
                                'blockDeviceMappings':[{'deviceName':'/dev/sda1','ebs':{'deleteOnTermination':True, 'volumeSize':20, 'volumeType':'gp2'}}],
                                'securityGroupIds':[core.Fn.import_value('publicsecuritygroup01')],
                                'instanceType':'t3.micro'},
            launch_template_name='public01')
        template02=aws_ec2.CfnLaunchTemplate(self, 'template02',
            launch_template_data={'imageId':'ami-06a46da680048c8ae',
                                'blockDeviceMappings':[{'deviceName':'/dev/sda1','ebs':{'deleteOnTermination':True, 'volumeSize':20, 'volumeType':'gp2'}}],
                                'securityGroupIds':[core.Fn.import_value('privatesecuritygroup01')],
                                'instanceType':'t3.micro'},
            launch_template_name='private01')
        # public instance
        instance01=aws_ec2.CfnInstance(self, 'instance01',
            launch_template={'launchTemplateId': template01.ref, 'version': template01.attr_latest_version_number},
            key_name='aws-example-key',
            subnet_id=core.Fn.import_value('publicsubnet01'))
        aws_ec2.CfnEIP(self, 'eip',
            domain='vpc',
            instance_id=instance01.ref,
            tags=[core.CfnTag(key='Name', value='eip01')])
        # private instance
        aws_ec2.CfnInstance(self, 'instance02',
            launch_template={'launchTemplateId': template02.ref, 'version': template01.attr_latest_version_number},
            key_name='aws-example-key',
            subnet_id=core.Fn.import_value('publicsubnet02'))