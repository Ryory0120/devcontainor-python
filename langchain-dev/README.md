# langchain-dev

DevContainor+RyeのLangChain環境

## DevContainor使い方
### 動作確認要件
* Windows11 Pro 23H1
* Rancher Desktop v1.16.0
* rye v0.42.0
* VS Code v1.95.1

### 事前準備

* Rancher Desktopをインストール
* Rancher Desktopにて下記2点を設定
    - Preferences -> Container Engine -> General -> dockerd(moby)を有効
    - Preferences -> WSL -> Integrations -> Ubuntuを有効
* VS CodeにてDevContainor Extentionをインストール

### DevContainor起動
* Ctrl+Shift+P より「DevContainor : ReOpen in Containor」を実行
    - 初回作成時、Containerへryeのインストールを実施。
* /workspaces/devcontainor-python/langchain-dev/.envに環境変数を設定
* rye run python src/main.pyで動作確認
    - 
　

## 疑問メモ
* DockerFileをいい感じにほかの人のものを流用できないか？
* オンライン環境でDockerImageの作成→保存/展開してオンプレで使えるか？

## TODO
* ryeの中でPythonのバージョン管理しているので、Containor側にPython不要。他の適切なImageに置き換えてよい。