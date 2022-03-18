# CodeCreatorForPyinstaller

## 概要
このコードは、「不必要なパッケージを全てexcludeする、pyinstallerのコンソール文」を自動で作成するコードです。

## 使い方
1. コンソールにおける"pip list"の出力を全てコピーして、"pkg_list.txt"にペースト
2. このコードを実行して、ファイルパスを入力
3. ”pyinstaller C:... --onefile -- noconsole --exclude-module ...”が出力される

