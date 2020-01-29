#!/usr/bin/bash
# ------------------------------------------------------------#
# stack-vpc
# ------------------------------------------------------------#
STACKNAME="stack-vpc"
TEMPLATE=`echo ${HOME}/cfn/template/template-vpc.yml`
PARAMETER=`echo ${HOME}/cfn/parameter/parameter-vpc.json`
echo 'start create name:'${STACKNAME}
aws-vault exec role -- aws cloudformation create-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER}
echo 'wait create complate name:'${STACKNAME}
aws-vault exec role -- aws cloudformation wait stack-create-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-publicsubnet
# ------------------------------------------------------------#
#STACKNAME="stack-publicsubnet"
#TEMPLATE=`echo ${HOME}/cfn/template/template-publicsubnet.yml`
#PARAMETER=`echo ${HOME}/cfn/parameter/parameter-publicsubnet.json`
#echo 'start create name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation create-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER}
#echo 'wait create complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-create-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-privatesubnet
# ------------------------------------------------------------#
#STACKNAME="stack-privatesubnet"
#TEMPLATE=`echo ${HOME}/cfn/template/template-privatesubnet.yml`
#PARAMETER=`echo ${HOME}/cfn/parameter/parameter-privatesubnet.json`
#echo 'start create name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation create-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER}
#echo 'wait create complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-create-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-securitygroup
# ------------------------------------------------------------#
#STACKNAME="stack-securitygroup"
#TEMPLATE=`echo ${HOME}/cfn/template/template-securitygroup.yml`
#PARAMETER=`echo ${HOME}/cfn/parameter/parameter-securitygroup.json`
#echo 'start create name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation create-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER} --capabilities CAPABILITY_AUTO_EXPAND
#echo 'wait create complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-create-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-securitygroup
# ------------------------------------------------------------#
#STACKNAME="stack-rds"
#TEMPLATE=`echo ${HOME}/cfn/template/template-rds.yml`
#PARAMETER=`echo ${HOME}/cfn/parameter/parameter-rds.json`
#echo 'start create name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation create-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER} --capabilities CAPABILITY_AUTO_EXPAND
#echo 'wait create complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-create-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-iam
# ------------------------------------------------------------#
#STACKNAME="stack-iam"
#TEMPLATE=`echo ${HOME}/cfn/template/template-iam.yml`
#PARAMETER=`echo ${HOME}/cfn/parameter/parameter-iam.json`
#echo 'start create name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation create-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE}  --capabilities CAPABILITY_NAMED_IAM
#echo 'wait create complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-create-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-ec2
# ------------------------------------------------------------#
#STACKNAME="stack-ec2"
#TEMPLATE=`echo ${HOME}/cfn/template/template-ec2.yml`
#PARAMETER=`echo ${HOME}/cfn/parameter/parameter-ec2.json`
#echo 'start create name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation create-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER} --capabilities CAPABILITY_AUTO_EXPAND
#echo 'wait create complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-create-complete --stack-name ${STACKNAME}
