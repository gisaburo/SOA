from aws_cdk import core
from aws_cdk import aws_ec2

class SecurityStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # instance role
        # instance profile
        # SecurityGroup
        publicsecuritygroup01 = aws_ec2.CfnSecurityGroup(self, 'publicsecuritygroup01', group_description='publicsecuritygroup', group_name='publicsecuritygroup01', vpc_id=core.Fn.import_value('vpcid01'), tags=[core.CfnTag(key='Name', value='publicsecuritygroup01')])
        privatesecuritygroup01 = aws_ec2.CfnSecurityGroup(self, 'privatesecuritygroup01', group_description='privatesecuritygroup', group_name='privatesecuritygroup01', vpc_id=core.Fn.import_value('vpcid01'), tags=[core.CfnTag(key='Name', value='privatesecuritygroup01')])
        # public Ingress
        aws_ec2.CfnSecurityGroupIngress(self, 'publicsecuritygroupingress01', group_id=publicsecuritygroup01.ref, ip_protocol='tcp', cidr_ip='0.0.0.0/0', description='for bastion', from_port=22, to_port=22)
        # public Egress
        aws_ec2.CfnSecurityGroupEgress(self, 'publicsecuritygroupegress01', group_id=publicsecuritygroup01.ref, ip_protocol='tcp', destination_security_group_id=privatesecuritygroup01.ref, description='for private', from_port=22, to_port=22)
        # private Ingress
        aws_ec2.CfnSecurityGroupIngress(self, 'privatesecuritygroupingress01', group_id=privatesecuritygroup01.ref, ip_protocol='tcp', source_security_group_id=publicsecuritygroup01.ref, description='for bastion', from_port=22, to_port=22)
        # private Egress
        aws_ec2.CfnSecurityGroupEgress(self, 'privatesecuritygroupegress01', group_id=privatesecuritygroup01.ref, ip_protocol='tcp', cidr_ip='0.0.0.0/0', description='for 443', from_port=443, to_port=443)
        aws_ec2.CfnSecurityGroupEgress(self, 'privatesecuritygroupegress02', group_id=privatesecuritygroup01.ref, ip_protocol='tcp', cidr_ip='0.0.0.0/0', description='for 80', from_port=80, to_port=80)
        aws_ec2.CfnSecurityGroupEgress(self, 'privatesecuritygroupegress03', group_id=privatesecuritygroup01.ref, ip_protocol='tcp', cidr_ip='0.0.0.0/0', description='for 22', from_port=22, to_port=22)
