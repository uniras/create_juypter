import sys
import os
import subprocess

# インストールスクリプトが存在するディレクトリ
script_dir = os.path.dirname(os.path.abspath(__file__))

# スクリプトが存在するディレクトリをカレントディレクトリに設定
os.chdir(script_dir)

# 仮想環境のディレクトリ
venv_dir = os.path.join(script_dir, ".venv")

# ステップ1: .venvディレクトリを確認して存在する場合は中止
files = os.listdir(script_dir)

if ".venv" in files:
    print(
        f'"{script_dir}" ディレクトリにはすでに仮想環境ディレクトリがあります。仮想環境の作成を中止します。'
    )
    input("続行するには何かキーを押してください...")
    sys.exit(1)

# ステップ2: 仮想環境を作成
print("仮想環境を作成しています...")
if not os.path.exists(venv_dir):
    subprocess.run([sys.executable, "-m", "venv", venv_dir])
    print(f'仮想環境 "{venv_dir}" を作成しました。')

# ステップ3: プラットフォーム固有の変数を設定
if sys.platform == "win32":
    binname = "Scripts"
else:
    binname = "bin"

# ステップ4: 仮想環境のパスを設定
pip_path = os.path.join(venv_dir, binname, "pip")

# ステップ5: 必要なパッケージのインストール
required_packages = ["jupyter"]

print(f'必要なパッケージを "{venv_dir}" 環境にインストールしています...')
subprocess.run([pip_path, "install"] + required_packages)

# ステップ6: 自身のスクリプトを削除
print("インストールスクリプトを削除しています...")
os.remove(__file__)
print(f'ファイル "{__file__}" を削除しました。')

# 終了メッセージの出力と待機
print("Jupyter環境のインストールが完了しました。")
print('VSCodeでJupyterノートブックを開始するには、VSCodeを起動して、F1を押して、"Jupyter: Create New Blank Notebook"を選択します。')
print('VSCodeのJupyterで仮想環境を有効にするには、"Select Kernel"をクリックし、"Python Environment"を選択した後、作成した".venv"ディレクトリを選択します。')
input("続行するには何かキーを押してください...")
