## 
### 環境構築
```
$ sudo npm install -g aws-cdk
```

### cfnの取り出し
```
$ cdk synth MypjStack ---path-metadata false --version-reporting false > stacks/template.yaml
```