### Bootstrap ###

import os
import subprocess
import sys
import ensurepip

print("Fetching required modules...")

def install_pip():
    ensurepip.bootstrap()
    subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)

def install_packages():
    result = subprocess.run([sys.executable, '-m', 'pip', 'install', "brotli"], capture_output=True)
    if result.returncode != 0: # if it is not yet installed
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', "brotli"], capture_output=True)
        if result.returncode == 0:
            print(f"Brotli has been installed!")
        else:
            print(f"Failed to install Brotli.")
            sys.exit()

def run_hash_script():
    subprocess.run(os.path.join(os.getcwd(), 'Hash.exe'))

def main():
    try:
        subprocess.run(['pip', '--version'], check=True, stdout=subprocess.PIPE)
    except FileNotFoundError:
        print("pip is not installed. Installing pip...")
        install_pip()
        print("pip has been installed!")

    install_packages()
    
    print("Requirements satisfied! \n")

    run_hash_script()
    
main()
