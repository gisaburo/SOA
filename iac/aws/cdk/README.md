# AWS Cloud Development Kit
- コードでcfnスタックを作成できるフレームワーク。terraformとTroposphereをかけ合わせた性質をもつ。terraformはスタックが作成できない。Troposphereはstateが管理できない。といった部分を埋めた印象。
## 環境構築
- ローカルで使ってもいいけど、cloud9とcodecommit使うほうが運用しやすいかも。
- Linuxでやる。windowsはgit bash & vs code で構築してみたけど、pythonのaliasつけたりbash.exe設定したり、cmd.exeでdeactivate.batうったらプロンプト戻らなかったりでもう大変。
### cdkのインストール
- グローバルインストールじゃないと動かないみたい。
    ```
    $ sudo npm install -g aws-cdk
    ```
### プロジェクトの作成
- 作業スペースとなるディレクトリ名は任意、リソースや環境ごとに分割したりすることを考えるとリソース単位にするよりも`mypj`とか広めの名前がいいかも。
    ```
    $ mkdir <working dir>
    $ cd <working dir>
    ```
- 言語はtypescriptかpythonで迷ったけど、bot3使えたほうが助かるのでpythonを選択。
    ```
    $ cdk init --language python
    # ライブラリ構成
    $ tree
    .
    ├── README.md                   <- 親切な説明
    ├── app.py                      <- プログラムメイン（Appにサブプログラムを指定する)
    ├── cdk.json                    <- cdkのパッケージ管理
    ├── cdk_python                  <- サブプログラム用のディレクトリ
    │   ├── __init__.py             <- お決まりのやつ
    │   └── cdk_python_stack.py     <- サブプログラムメイン
    ├── requirements.txt            <- pipのパッケージ管理
    ├── setup.py                    <- いろいろ設定する
    └── source.bat                  <- windows用venv
    ```
- pythonはvenvなバーチャル環境で作業する。
    ```
    $ source .env/bin/activate
    (.env) [user@host <working dir>]$ 
    ```
- requirementsを流す。
    ```
    $ pip install -r requirements.txt
    ....
    # だいたいこんなのがでるのでアップデートする。
    WARNING: You are using pip version <current ver>, however version <new ver> is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.
    
    $ pip install --upgrade pip
    # でこうなる
    Successfully uninstalled pip-<current ver>
    Successfully installed pip-<new ver>

    # ついでにやる
    $ pip install --upgrade aws_cdk.core
    ```
## 眺める
### サブプログラムを見てみる 
- ファイル名は`<working dir>_stack.py`になるみたい。
- 一番下に`# The code that defines your stack goes here`とでているので、この辺にリソース定義を書けばいいのかな。
    ```
    from aws_cdk import core


    class CdkPythonStack(core.Stack):

        def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
            super().__init__(scope, id, **kwargs)

            # The code that defines your stack goes here
    ```
### メインプログラム見てみる
- サブプログラムのclassがインポートされている。
- appの中で呼んでるインスタンス単位にスタックになる模様。
    ```
    #!/usr/bin/env python3

    from aws_cdk import core

    from cdk_python.cdk_python_stack import CdkPythonStack


    app = core.App()
    CdkPythonStack(app, "cdk-python")

    app.synth()
    ```
### スタック名って
- `cdk ls`でスタック名を確認できる。つまり、appで指定した`cdk-python`がスタック名なる様子。`dev-vpc` or `prod-vpc`とかで切り換える感じかな。
    ```
    $ cdk ls
    cdk-python
    ```
### 取り敢えずvpc作ってみる
- まずはパッケージをインストール
    ```
    $ pip install aws_cdk.aws_ec2
    ```
- サブプログラムに直接書いてみる。変更カ所はインライン
    ```
    from aws_cdk import core
    # --- 追加 vpcパッケージのインポート ----
    from aws_cdk import aws_ec2

    class CdkPythonStack(core.Stack):

        def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
            super().__init__(scope, id, **kwargs)

            # The code that defines your stack goes here
            # --- 追加 vpcのリソース定義 ---
            aws_ec2.CfnVPC(
            self, "vpc",
            cidr_block="10.0.0.0/16",
            enable_dns_hostnames=True,
            enable_dns_support=True,
            tags=[core.CfnTag(
                key="Name", 
                value="vpc")
            ])
    ```
- 結果確認
    ```
    $ cdk synth ---path-metadata false --version-reporting false
    Resources:
    vpc:
        Type: AWS::EC2::VPC
        Properties:
        CidrBlock: 192.168.0.0/16
        EnableDnsHostnames: true
        EnableDnsSupport: true
        Tags:
            - Key: Name
              Value: vpc
    ```
### 分割する
- 構成
    ```
    tree
    .
    ├── README.md
    ├── app.py
    ├── cdk.context.json
    ├── cdk.json
    ├── cdk.out
    │   ├── cdk-python.template.json
    │   ├── cdk.out
    │   ├── manifest.json
    │   └── tree.json
    ├── cdk_python
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   └── cdk_python_stack.cpython-37.pyc
    │   ├── cdk_python.egg-info
    │   │   ├── PKG-INFO
    │   │   ├── SOURCES.txt
    │   │   ├── dependency_links.txt
    │   │   ├── requires.txt
    │   │   └── top_level.txt
    │   ├── cdk_python_stack.py
    │   └── resources                           <- 追加
    │       ├── __init__.py                     <- 追加（空でok）
    │       ├── __pycache__                     <- 自動生成
    │       │   ├── __init__.cpython-37.pyc     <- 自動生成
    │       │   └── vpc.cpython-37.pyc          <- 自動生成
    │       └── vpc.py                          <- 追加（後で編集）
    ├── requirements.txt
    ├── setup.py
    └── source.bat
    ```
- vpc.py編集
    ```
    from aws_cdk import (
        core,
        aws_ec2,
    )
    
    
    def create_vpc(scope: core.Construct) -> None:
        vpc = aws_ec2.CfnVPC(scope, 
            id='vpc01',
            cidr_block='10.0.0.0/16',
            enable_dns_hostnames=True,
            enable_dns_support=True,
            tags=[core.CfnTag(
                key='Name',
                value='vpc01',
            )]
        )
    
        return vpc
    ```
- cdk_python_stack.py編集
    ```
    from aws_cdk import core
    # --- 追加 vpcリソースのインポート ----
    from resources import vpc

    class CdkPythonStack(core.Stack):

        def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
            super().__init__(scope, id, **kwargs)

            # The code that defines your stack goes here
            # --- 追加 vpcリソースのインスタンス生成 ----
            vpc.create_vpc(self)
    ```
- 確認
    ```
    cdk synth --path-metadata false --version-reporting false
    Resources:
    vpc01:
        Type: AWS::EC2::VPC
        Properties:
        CidrBlock: 10.0.0.0/16
        EnableDnsHostnames: true
        EnableDnsSupport: true
        Tags:
            - Key: Name
            Value: vpc01
    ```
### ライブラリ構成について
- 本番、開発で値を変えて管理することを考えるとこんな感じかな
    ```
    tree
    .
    ├── README.md
    ├── app.py                                      <- ここでライブラリを切り換える
    ├── cdk.context.json
    ├── cdk.json
    ├── cdk.out
    │   ├── cdk-python.template.json
    │   ├── cdk.out
    │   ├── dev-vpc.template.json
    │   ├── manifest.json
    │   └── tree.json
    ├── cdk_python
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   └── cdk_python_stack.cpython-37.pyc
    │   ├── cdk_python.egg-info
    │   │   ├── PKG-INFO
    │   │   ├── SOURCES.txt
    │   │   ├── dependency_links.txt
    │   │   ├── requires.txt
    │   │   └── top_level.txt
    │   ├── dev                                     <- 開発系のライブラリ
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-37.pyc
    │   │   │   └── vpc_stack.cpython-37.pyc
    │   │   └── vpc_stack.py
    │   └── resources                               <- テンプレート
    │       ├── __init__.py
    │       ├── __pycache__
    │       │   ├── __init__.cpython-37.pyc
    │       │   └── vpc.cpython-37.pyc
    │       └── vpc.py
    ├── requirements.txt
    ├── setup.py
    └── source.bat
    ```
## 付録
- マメにやっておくこと。バージョンはすぐに上がってしまう。
    ```
    $ suod pip install --upgrade pip
    $ pip install --upgrade aws-cdk.core
    ```
- synthでcfnを出力 `-j false`入れてもouputがjsonになっちゃうのでもう標準出力をそのまま使うことにした。`--path-metadata false`と`--version-reporting false`を入れておくとメタデータは除外される。
    ```
    $ cdk synth MypjStack --path-metadata false --version-reporting false > stacks/template.yaml
    ```
- Constructは3種類存在する。
    1. High Level Construct
        - AWS CDKがCloudFormationの各リソースを抽象化してくれているライブラリ。例えば‘`aws_ec2.Vpc`リソース内でsubnetの生成までcdkが自動で生成する。特にパラメータに制限がなければこちらを選択する。
    2. Low Level Construct
        - cfnと同等。パラメータを細かく設定する場合をこちらを選択する。普通にcfnを作成する場合と比較して、ループなどでリソースを生成できることが利点といえる。
    3. Patterns
        - デザインパターンがそのまま実行できるライブラリ。設計が合致すれば使える。
## 参考
- [【AWS CDK】CDK標準の3種類のConstructを使って、AWSリソースをデプロイしてみた](https://dev.classmethod.jp/cloud/aws/aws-cdk-construct-explanation/)
- [AWS CDKを導入して脱YAMLテンプレートを試みる](https://www.techscore.com/blog/2019/12/18/aws-cdk/)