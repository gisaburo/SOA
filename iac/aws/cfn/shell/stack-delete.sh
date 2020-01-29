#!/usr/bin/bash
# ------------------------------------------------------------#
# stack-ec2
# ------------------------------------------------------------#
STACKNAME="stack-ec2"
echo 'start delete name:'${STACKNAME}
aws-vault exec role -- aws cloudformation delete-stack --stack-name ${STACKNAME}
echo 'wait delete complate name:'${STACKNAME}
aws-vault exec role -- aws cloudformation wait stack-delete-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-iam
# ------------------------------------------------------------#
#STACKNAME="stack-iam"
#echo 'start delete name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation delete-stack --stack-name ${STACKNAME}
#echo 'wait delete complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-delete-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-rds
# ------------------------------------------------------------#
#STACKNAME="stack-rds"
#echo 'start delete name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation delete-stack --stack-name ${STACKNAME}
#echo 'wait delete complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-delete-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-securitygroup
# ------------------------------------------------------------#
#STACKNAME="stack-securitygroup"
#echo 'start delete name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation delete-stack --stack-name ${STACKNAME}
#echo 'wait delete complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-delete-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-privatesubnet
# ------------------------------------------------------------#
#STACKNAME="stack-privatesubnet"
#echo 'start delete name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation delete-stack --stack-name ${STACKNAME}
#echo 'wait delete complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-delete-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-publicsubnet
# ------------------------------------------------------------#
#STACKNAME="stack-publicsubnet"
#echo 'start delete name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation delete-stack --stack-name ${STACKNAME}
#echo 'wait delete complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-delete-complete --stack-name ${STACKNAME}
# ------------------------------------------------------------#
# stack-vpc
# ------------------------------------------------------------#
#STACKNAME="stack-vpc"
#echo 'start delete name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation delete-stack --stack-name ${STACKNAME}
#echo 'wait delete complate name:'${STACKNAME}
#aws-vault exec role -- aws cloudformation wait stack-delete-complete --stack-name ${STACKNAME}
# ----------------
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-privatesubnet
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-natgateway
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-loadbalancer
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-s3endpoint
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-rds
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-ssm-parmstore
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-vpcflowlog
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-cloudwatch-alarm
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-cloudwatch-filter
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-cloudtrail
#aws-vault exec role -- aws cloudformation delete-stack --stack-name vpc01-stack-s3
