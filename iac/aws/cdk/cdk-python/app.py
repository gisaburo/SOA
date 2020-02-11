#!/usr/bin/env python3

from aws_cdk import core

from cdk_python.dev.vpc_stack import vpcStack


app = core.App()
vpcStack(app, "dev-vpc")

app.synth()
