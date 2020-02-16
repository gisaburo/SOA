from aws_cdk import (
    core,
    aws_ec2
)
from .value import variable

class vpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        v = variable('test/input.yaml')

        for i in range(len(v.yml['VPC'])):
            tags = []
            if 'tags' in v.yml['VPC'][i]:
                for j in range(len(v.yml['VPC'][i]['tags'])):
                    tags.append(core.CfnTag(key=v.yml['VPC'][i]['tags'][j]['key'] ,value=v.yml['VPC'][i]['tags'][j]['value']))
            else:
                tags = None

            CfnVPC= aws_ec2.CfnVPC(self,
                        'vpc' + str(i + 1).zfill(2), 
                        cidr_block=v.yml['VPC'][i]['cidr_block'],
                        enable_dns_hostnames=v.yml['VPC'][i]['enable_dns_hostnames'],
                        enable_dns_support=v.yml['VPC'][i]['enable_dns_support'], 
                        instance_tenancy=v.yml['VPC'][i]['instance_tenancy'], 
                        tags=tags
                    )

            if 'export' in v.yml['VPC'][i]:
                for j in range(len(v.yml['VPC'][i]['export'])):
                
                    if 'description' in v.yml['VPC'][i]['export'][j]:
                        description = v.yml['VPC'][i]['export'][j]['description']
                    else:
                        description = None

                    if v.yml['VPC'][i]['export'][j]['value'] == 'ref':
                        CfnVPC_attr = CfnVPC.ref

                    core.CfnOutput(self,
                        'ovpc' + str(i) + str(j + 1),
                        value=CfnVPC_attr,
                        description=description, 
                        export_name=v.yml['VPC'][i]['export'][j]['export_name']
                    )

            if 'InternetGateway' in v.yml['VPC'][i]:
                tags = []
                for j in range(len(v.yml['VPC'][i]['InternetGateway'])):
                    tags.append(core.CfnTag(key=v.yml['VPC'][i]['InternetGateway'][i]['key'] ,value=v.yml['VPC'][i]['InternetGateway'][i]['value']))

                CfnInternetGateway= aws_ec2.CfnInternetGateway(self,
                                        'InternetGateway' + str(i + 1).zfill(2),
                                        tags=tags
                                    )


                aws_ec2.CfnVPCGatewayAttachment(self,
                    'VPCGatewayAttachment' + str(i + 1).zfill(2),
                    vpc_id=CfnVPC_attr,
                    internet_gateway_id=CfnInternetGateway.ref,
                    )

            print(v.yml['VPC'][i]['InternetGateway'])
            if 'export' in v.yml['VPC'][i]['InternetGateway']:
                for j in range(len(v.yml['InternetGateway'][i]['export'])):
                
                    if 'description' in v.yml['VPC'][i]['InternetGateway'][i]['export'][j]:
                        description = v.yml['InternetGateway'][i]['export'][j]['description']
                    else:
                        description = None

                    core.CfnOutput(self,
                        'oInternetGateway' + str(i) + str(j + 1),
                        value=CfnInternetGateway.ref,
                        description=description, 
                        export_name=v.yml['InternetGateway'][i]['export'][j]['export_name']
                    )