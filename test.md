# githubとの連携テスト

## 2020/08/20 22:33

上手く連携できたようだ。これからPythonの勉強を始め、その内容をここにアップロードして行けたらと思っている。

## 2020/08/20 22:36

まずは python のインストール。VS codeのコマンドラインから python と打ち込んだら、Windowsのアプリストアが開きPythonのダウンロード画面になった。

そのままインストールを実施。無事にインストールに成功した。

```sh
>python
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## 2020/08/23 21:56

完全な思いつきだが、Ingress の [IntelMap](https://intel.ingress.com/intel) からデータを取得して解析するようなプログラムを作ってみたい。
取りあえずは特定地点のPortallistを取得して整形して表示かな。
ログインが必要なのがハードル高そうだけどやってみよう。

## 2020/08/28 22:22

Pythonの静的解析、少し調べて [Flake8](https://flake8.pycqa.org/en/latest/) と言うのを使ってみた。
pipで入れてVS Codeの連携オプションを有効にするとエディタのバッググラウンドで自動で解析してくれて便利。
やはりメインストリームの言語だと道がととのっていて便利なことが多い。
