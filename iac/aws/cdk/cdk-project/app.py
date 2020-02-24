#!/usr/bin/env python3

from aws_cdk import core

from cdk_project.a01_network_stack import NetworkStack
from cdk_project.b01_network_stack import NetworkStack as networkstack

app = core.App()
NetworkStack(app, "networka")
networkstack(app, "networkb")
app.synth()
