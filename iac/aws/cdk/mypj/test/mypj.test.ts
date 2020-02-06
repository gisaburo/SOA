import { expect as expectCDK, matchTemplate, MatchStyle } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import Mypj = require('../lib/mypj-stack');

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new Mypj.MypjStack(app, 'MyTestStack');
    // THEN
    expectCDK(stack).to(matchTemplate({
      "Resources": {}
    }, MatchStyle.EXACT))
});
