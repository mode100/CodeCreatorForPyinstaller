# CodeCreatorForPyinstaller

このコードは、「不必要なパッケージを全てexcludeする、pyinstallerのコンソール文」を自動で作成するコードです。

[使い方]
1. "pip list"の出力を"pkg_list.txt"にコピー&ペースト
2. 実行ファイルにする予定のファイルのパスを入力
3. ”pyinstaller C:... --onefile -- noconsole --exclude-module ...”が出力される

