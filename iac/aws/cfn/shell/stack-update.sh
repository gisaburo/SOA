#!/usr/bin/bash
# ------------------------------------------------------------#
# stack-vpc
# ------------------------------------------------------------#
#STACKNAME="stack-vpc"
#TEMPLATE=`echo ${HOME}/cfn/template/template-vpc.yml`
#PARAMETER=`echo ${HOME}/cfn/parameter/parameter-vpc.json`
#echo 'start update name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation update-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER}
#echo 'wait update complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-update-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-publicsubnet
# ------------------------------------------------------------#
#STACKNAME="stack-publicsubnet"
#TEMPLATE=`echo ${HOME}/cfn/template/template-publicsubnet.yml`
#PARAMETER=`echo ${HOME}/cfn/parameter/parameter-publicsubnet.json`
#echo 'start update name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation update-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER}
#echo 'wait update complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-update-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-privatesubnet
# ------------------------------------------------------------#
#STACKNAME="stack-privatesubnet"
#TEMPLATE=`echo ${HOME}/cfn/template/template-privatesubnet.yml`
#PARAMETER=`echo ${HOME}/cfn/parameter/parameter-privatesubnet.json`
#echo 'start update name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation update-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER}
#echo 'wait update complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-update-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-securitygroup
# ------------------------------------------------------------#
STACKNAME="stack-securitygroup"
TEMPLATE=`echo ${HOME}/cfn/template/template-securitygroup.yml`
PARAMETER=`echo ${HOME}/cfn/parameter/parameter-securitygroup.json`
echo 'start update name:'${STACKNAME}
aws-vault exec role -- aws cloudformation update-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER} --capabilities CAPABILITY_AUTO_EXPAND
echo 'wait update complate name:'${STACKNAME}
aws-vault exec role -- aws cloudformation wait stack-update-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-rds
# ------------------------------------------------------------#
#STACKNAME="stack-rds"
#TEMPLATE=`echo ${HOME}/cfn/template/template-rds.yml`
#PARAMETER=`echo ${HOME}/cfn/parameter/parameter-rds.json`
#echo 'start update name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation update-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER}
#echo 'wait update complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-update-complete --stack-name ${STACKNAME}