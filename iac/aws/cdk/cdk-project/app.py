#!/usr/bin/env python3

from aws_cdk import core

from cdk_project.my_network_stack import NetworkStack as mynetworkstack
from cdk_project.my_security_stack import SecurityStack as mysecuritystack
from cdk_project.my_ec2_stack import EC2Stack as myec2stack

app = core.App()
mynetworkstack(app, 'mynetwork')
mysecuritystack(app, 'mysecurity')
myec2stack(app, 'myec2')
app.synth()
