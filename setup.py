import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    try:
        # Read the requirements file
        with open("requirements.txt") as f:
            requirements = f.readlines()
        
        # Install each package listed in requirements.txt
        for package in requirements:
            install(package.strip())
        
        print("All packages installed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
