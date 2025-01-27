# filename: install_pip.py
import sys
import subprocess

def install_pip():
    subprocess.run([sys.executable, "-m", "ensurepip"])

install_pip()
print("pip installed successfully.")