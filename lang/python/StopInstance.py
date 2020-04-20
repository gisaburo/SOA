#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import boto3
import pprint
import json
import time

def my_handler(event, context):

    print("Log stream name:", context.log_stream_name)
    print("Log group name:",  context.log_group_name)
    print("Request ID:",context.aws_request_id)
    print("Mem. limits(MB):", context.memory_limit_in_mb)

    _InstanceId = event['InstanceId']
    cloudwatch = boto3.client('cloudwatch')

# ========== アラート抑止 ==========
    _describe_alarms = cloudwatch.describe_alarms(
    )
    for i in range(len(_describe_alarms['MetricAlarms'])):
        if _describe_alarms['MetricAlarms'][i]['Dimensions'][0]['Name'] == 'InstanceId':
            if _describe_alarms['MetricAlarms'][i]['Dimensions'][0]['Value'] == _InstanceId:
                _disable_alarm_actions = cloudwatch.disable_alarm_actions(
                    AlarmNames=[
                        _describe_alarms['MetricAlarms'][i]['AlarmName'],
                    ]
                )

# ========== アラート抑止確認（失敗しても続行） ==========
    _describe_alarms = cloudwatch.describe_alarms(
    )
    store_disable_alarms = []
    for i in range(len(_describe_alarms['MetricAlarms'])):
        if _describe_alarms['MetricAlarms'][i]['Dimensions'][0]['Name'] == 'InstanceId':
            if _describe_alarms['MetricAlarms'][i]['Dimensions'][0]['Value'] == _InstanceId:
                store_disable_alarms.append( { 'Dimensions':_describe_alarms['MetricAlarms'][i]['Dimensions'][0]['Value'],'AlarmName':_describe_alarms['MetricAlarms'][i]['AlarmName'],'StateValue':_describe_alarms['MetricAlarms'][i]['StateValue'],'ActionsEnabled':_describe_alarms['MetricAlarms'][i]['ActionsEnabled'] } )

# ========== インスタンス停止 ==========
    ec2 = boto3.client('ec2')
    ec2.stop_instances(
        InstanceIds=[
            _InstanceId
        ]
    )

# ========== インスタンスstatus確認 ==========
    _instance_status = ec2.describe_instances(
        InstanceIds=[
            _InstanceId
        ]
    )
    store_instance = []
    store_instance.append( { 'Tags':_instance_status['Reservations'][0]['Instances'][0]['Tags'][0]['Value'],'State':_instance_status['Reservations'][0]['Instances'][0]['State']['Name'] } )

# ========== 情報出力 ==========
    print('---alarm_disable_status')
    pprint.pprint(store_disable_alarms)
    print('---instance status')
    pprint.pprint(store_instance)

# ========== チェック用lambda呼び出し ==========

# ========== 5分間 wait ==========
    time.sleep(300)

# ========== インスタンスstatus確認 ==========
    _instance_status = ec2.describe_instances(
        InstanceIds=[
            _InstanceId
        ]
    )
    store_instance = []
    store_instance.append( { 'Tags':_instance_status['Reservations'][0]['Instances'][0]['Tags'][0]['Value'],'State':_instance_status['Reservations'][0]['Instances'][0]['State']['Name'] } )

    if _instance_status['Reservations'][0]['Instances'][0]['State']['Name'] != 'stopped':
        pass
    else:
# ========== チェック用lambda呼び出し ==========
        return

# ========== アラーム抑止解除 ==========
    _describe_alarms = cloudwatch.describe_alarms(
    )
    for i in range(len(_describe_alarms['MetricAlarms'])):
        if _describe_alarms['MetricAlarms'][i]['Dimensions'][0]['Name'] == 'InstanceId':
            if _describe_alarms['MetricAlarms'][i]['Dimensions'][0]['Value'] == _InstanceId:
                if _describe_alarms['MetricAlarms'][i]['StateValue'] != 'OK':
                    _enable_alarm_actions = cloudwatch.enable_alarm_actions(
                        AlarmNames=[
                            _describe_alarms['MetricAlarms'][i]['AlarmName'],
                        ]
                    )
                else:
# ========== チェック用lambda呼び出し ==========
                    return
# ========== アラーム状態確認 ==========
    _describe_alarms = cloudwatch.describe_alarms(
    )
    store_enable_alarms = []
    for i in range(len(_describe_alarms['MetricAlarms'])):
        if _describe_alarms['MetricAlarms'][i]['Dimensions'][0]['Name'] == 'InstanceId':
            if _describe_alarms['MetricAlarms'][i]['Dimensions'][0]['Value'] == _InstanceId:
                store_enable_alarms.append( { 'AlarmName':_describe_alarms['MetricAlarms'][i]['AlarmName'],'StateValue':_describe_alarms['MetricAlarms'][i]['StateValue'],'ActionsEnabled':_describe_alarms['MetricAlarms'][i]['ActionsEnabled'] } )

    print('---alarm_enable_status')
    pprint.pprint(store_enable_alarms)

# ========== 完了メッセージ通知 ==========
    TOPIC_ARN = _TOPIC_ARN
    msg = 'インスタンス%sを停止しました。\n\n○インスタンスステータス\n  %s\n\n○アラームステータス\n  %s' %(_InstanceId,store_instance,store_enable_alarms)
    subject = u'インスタンス停止情報'
    sns = boto3.client('sns')

    request = {
        'TopicArn': TOPIC_ARN,
        'Message': msg,
        'Subject': subject
    }
    response = sns.publish(**request)
    pprint.pprint(response)

    return {
        'message' : None
    }