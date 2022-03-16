# CodeCreatorForPyinstaller

Pyinstallerでpyファイルを実行ファイルに直す際、Pythonの環境に入っている全てのパッケージが封入されてしまい、実行ファイルのサイズが大きくなってしまいます。そして、不必要なパっケージを取り除くには、コンソールで「--exclude-module numpy --exclude-module pip ...」などと書き連ねなければなりません。

このコードは、いらないパッケージを全てexcludeするコンソール文を自動で作成するコードです。
