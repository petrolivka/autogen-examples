# filename: install_dependencies.py
import sys
import subprocess

def install_packages():
    packages = ['yfinance', 'matplotlib', 'pandas']
    for package in packages:
        subprocess.run([sys.executable, "-m", "pip", "install", package])

install_packages()
print("Dependencies installed successfully.")