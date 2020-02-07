import * as cdk from '@aws-cdk/core';
import * as ec2 from '@aws-cdk/aws-ec2'

export class MypjStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    new ec2.CfnVPC(this, 'vpc', {
      cidrBlock: "10.0.0.0/16",
      enableDnsHostnames: true,
      enableDnsSupport: true,
      instanceTenancy: "default",
      tags:[{
        "key":"Name", 
        "value":"vpc"
      }]
    })
  }
}
