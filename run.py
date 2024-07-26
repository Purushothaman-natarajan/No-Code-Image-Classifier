import subprocess
import sys
import os

def install_requirements():
    try:
        # Check if requirements.txt exists
        if os.path.exists('requirements.txt'):
            # Install dependencies from requirements.txt
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        else:
            print("requirements.txt not found.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)

def run_interface():
    try:
        # Run the interface script
        subprocess.check_call([sys.executable, 'interface.py'])
    except subprocess.CalledProcessError as e:
        print(f"Failed to run the interface script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
    run_interface()
