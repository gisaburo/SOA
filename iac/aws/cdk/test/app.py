#!/usr/bin/env python3

from aws_cdk import core
from test.vpc_stack import vpcStack


app = core.App()
vpcStack(app, "vpc")

app.synth()
