#!/usr/bin/bash
if [ $# -ne 1 ]; then
  echo "指定された引数は$#個です。" 1>&2
  echo "実行するには1個の引数が必要です。" 1>&2
  exit 1
fi

cat  $1 | while read line || [ -n "${line}" ]; do
        if [ `echo ${line} | cut -c 1` != '#' ]; then

            var1=`echo ${line} | cut -d , -f 1`
            var2=`echo ${line} | cut -d , -f 2`
            var3=`echo ${line} | cut -d , -f 3`

            STACKNAME="${var1}"
            TEMPLATE="${HOME}/cfn/template/${var2}"
            PARAMETER="${HOME}/cfn/parameter/${var3}"

            echo 'start create name:'${STACKNAME}
            aws cloudformation create-stack --profile role --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER}
            echo 'wait create complate name:'${STACKNAME}
            aws cloudformation wait stack-create-complete --profile role --stack-name ${STACKNAME}
            echo 'describe-stacks'
            aws cloudformation describe-stacks --profile role --stack-name ${STACKNAME} --output text
        fi
    done 
#for var in ${list[@]}
#  do
#    STACKNAME="${var}"
#    TEMPLATE=`echo ${HOME}/cfn/template/${var}`
#    PARAMETER=`echo ${HOME}/cfn/parameter/${var}`

#    echo $STACKNAME
#    echo $TEMPLATE
#    echo $PARAMETER

#    echo 'start create name:'${STACKNAME}
#    aws-vault exec role -- aws cloudformation create-stack --stack-name ${STACKNAME} --template-body file://${TEMPLATE} --parameters file://${PARAMETER}
#    echo 'wait create complate name:'${STACKNAME}
#    aws-vault exec role -- aws cloudformation wait stack-create-complete --stack-name ${STACKNAME}
#    echo 'describe-stacks'
#    aws-vault exec role -- aws cloudformation describe-stacks --stack-name ${STACKNAME} --output text
#  done
