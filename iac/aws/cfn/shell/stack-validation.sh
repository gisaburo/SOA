#!/usr/bin/bash
# ------------------------------------------------------------#
# stack-vpc
# ------------------------------------------------------------#
#TEMPLATE=`echo ${HOME}/cfn/template/template-vpc.yml`
#aws-vault exec role -- aws cloudformation validate-template --template-body file://${TEMPLATE}
# ------------------------------------------------------------#
# stack-publicsubnet
# ------------------------------------------------------------#
#TEMPLATE=`echo ${HOME}/cfn/template/template-publicsubnet.yml`
#aws-vault exec role -- aws cloudformation validate-template --template-body file://${TEMPLATE} 
# ------------------------------------------------------------#
# stack-privatesubnet
# ------------------------------------------------------------#
#TEMPLATE=`echo ${HOME}/cfn/template/template-privatesubnet.yml`
#aws-vault exec role -- aws cloudformation validate-template --template-body file://${TEMPLATE} 
# ------------------------------------------------------------#
# stack-scuritygroup
# ------------------------------------------------------------#
#TEMPLATE=`echo ${HOME}/cfn/template/template-securitygroup.yml`
#aws-vault exec role -- aws cloudformation validate-template --template-body file://${TEMPLATE}
# ------------------------------------------------------------#
# stack-rds
# ------------------------------------------------------------#
#TEMPLATE=`echo ${HOME}/cfn/template/template-rds.yml`
#aws-vault exec role -- aws cloudformation validate-template --template-body file://${TEMPLATE}
# ------------------------------------------------------------#
# stack-ec2
# ------------------------------------------------------------#
TEMPLATE=`echo ${HOME}/cfn/template/template-ec2.yml`
aws-vault exec role -- aws cloudformation validate-template --template-body file://${TEMPLATE}
# ------------------------------------------------------------#
# stack-iam
# ------------------------------------------------------------#
TEMPLATE=`echo ${HOME}/cfn/template/template-iam.yml`
aws-vault exec role -- aws cloudformation validate-template --template-body file://${TEMPLATE}