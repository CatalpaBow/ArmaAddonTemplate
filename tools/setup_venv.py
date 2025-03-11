import os
import sys
import subprocess

# 実行されたスクリプトの親ディレクトリを取得し、さらに一段階上に移動
parent_dir = os.path.dirname(os.path.abspath(__file__))  # 'tools' フォルダのパス
parent_dir = os.path.dirname(parent_dir)  # 'AddonTemplate' フォルダのパス

# .venvという仮想環境のディレクトリを作成するパス
venv_dir = os.path.join(parent_dir, '.venv')

# 仮想環境が既に存在しないか確認
if not os.path.exists(venv_dir):
    # 仮想環境を作成
    print(f"Creating virtual environment at: {venv_dir}")
    subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    print(".venv created successfully!")
else:
    print(".venv already exists.")

# 仮想環境をアクティベートするためのパスを作成
activate_script = os.path.join(venv_dir, 'Scripts', 'activate') if os.name == 'nt' else os.path.join(venv_dir, 'bin', 'activate')

# requirements.txtがあるか確認し、インストールする
requirements_file = os.path.join(parent_dir, 'requirements.txt')
if os.path.exists(requirements_file):
    print(f"Installing packages from {requirements_file}...")
    # 仮想環境内でpipを使ってパッケージをインストール
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
    print("Packages installed successfully!")
else:
    print("requirements.txt not found.")
