#!/bin/bash
_sts=`aws sts assume-role --role-arn arn:aws:iam::12345678:role/role-name --role-session-name iam-user-name`
export AWS_REGION=ap-northeast-1
export AWS_ACCESS_KEY_ID=`echo $_sts | jq -r '.Credentials.AccessKeyId'`
export AWS_SECRET_ACCESS_KEY=`echo $_sts | jq -r '.Credentials.SecretAccessKey'`
export AWS_SESSION_TOKEN=`echo $_sts | jq -r '.Credentials.SessionToken'`
echo 'AWS_REGION: ' $AWS_REGION
echo 'AWS_ACCESS_KEY_ID: ' $AWS_ACCESS_KEY_ID
echo 'AWS_SECRET_ACCESS_KEY: ' $AWS_SECRET_ACCESS_KEY
echo 'AWS_SESSION_TOKEN: ' $AWS_SESSION_TOKEN