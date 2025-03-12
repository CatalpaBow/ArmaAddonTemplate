import tomllib
import tomli_w
import os
def excute():
    # ユーザーからの入力を取得
    name = input("Enter the name (e.g. 'Arma Addon Template'): ")
    author = input("Enter the author (e.g. 'FooBar Team'): ")
    prefix = input("Enter the prefix (e.g. 'aam'): ")
    mainprefix = input("Enter the main prefix (e.g. 'z'): ")

    # git_hashは固定値0
    git_hash = 0

    # このファイルのパスから2階層上をプロジェクトルートとする
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, ".hemtt", "project.toml")

    # 辞書形式でデータを作成
    toml_data = {
        "name": name,
        "author": author,
        "prefix": prefix,
        "mainprefix": mainprefix,
        "git_hash": git_hash
    }

    # 書き込み先のディレクトリを作成（存在しない場合）
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # バイナリモード("wb")でファイルに書き込む
    with open(file_path, "wb") as f:
        tomli_w.dump(toml_data, f)

    print(f"TOMLファイルが作成されました: {file_path}")
    
if __name__ == "__main__":
    excute()