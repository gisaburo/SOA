#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { MypjStack } from '../lib/mypj-stack';

const app = new cdk.App();
new MypjStack(app, 'MypjStack');
