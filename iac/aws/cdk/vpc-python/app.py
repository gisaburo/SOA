#!/usr/bin/env python3

from aws_cdk import core

from vpc_python.vpc_python_stack import VpcPythonStack


app = core.App()
VpcPythonStack(app, "vpc-python")

app.synth()
