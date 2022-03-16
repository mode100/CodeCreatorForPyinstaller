import subprocess, os, sys, pkgutil

PATH = __file__
FOLDER = os.path.dirname(__file__)

PLIST_FILE = "pkg_list.txt"
PLIST_PATH = FOLDER + "\\" + PLIST_FILE
object_path = __file__

pkg_list = []

# パスを入力します
def input_path():
    _input = input("パスを入力して下さい> ")
    if os.path.exists(_input):
        return _input
    if os.path.exists(FOLDER+"\\"+_input):
        return FOLDER+"\\"+_input
    print("[Error]そのパスは存在しません!")
    return None

#  パッケージの一覧を取得
def get_pkg_list_in_python():
    rl = []
    if os.path.exists(PLIST_PATH):
        with open(PLIST_PATH, "r") as f:
            rl = f.readlines()
    _list = []
    for i in rl:
        _name = i.split()[0]
        _list.append(_name)
    return _list

# ファイルに含まれるパッケージの一覧を取得
def get_pkg_list_in_code(_filepath):
    rl = []
    with open(_filepath, "r", encoding="utf-8") as f:
        rl = f.readlines()
    _list = []
    for i in rl:
        if "import" == i[:6]:
            word_list = i.split(",")
            for j in range(len(word_list)):
                word_list[j] = word_list[j].replace("import", "")
                word_list[j] = word_list[j].replace(" ", "")
                word_list[j] = word_list[j].replace(";", "")
                word_list[j] = word_list[j].replace("\n", "")
            for w in word_list:
                _list.append(w)
        elif "from" == i[:4]:
            _lib = i.split("import")[0]
            _lib = _lib.split(".")[0]
            _lib = _lib.replace("from", "")
            _lib = _lib.replace(" ", "")
            _list.append(_lib)
    # 重複を消す
    _list = list(set(_list))
    return _list

def get_sentence_for_pyinstaller(_path):
    snt = "pyinstaller " + _path + " --onefile --noconsole"
    _pkgs_exclude = get_pkg_list_in_python()
    _pkgs_in_code = get_pkg_list_in_code(_path)
    for i in _pkgs_in_code:
        if i in _pkgs_exclude:
            _pkgs_exclude.remove(i)
    for i in _pkgs_exclude:
        snt += " --exclude-module " + i
    return snt


def main():
    while True:
        object_path = input_path()
        if object_path != None:
            break
    print(get_sentence_for_pyinstaller(object_path))

if __name__ == "__main__":
    main()

    


# python C:\Users\yuito\Documents\Works\Code\Python\ツール\excludeを作成.py
    
    