import subprocess
import sys
import os

def install_requirements():
    print("Installing dependencies from requirements.txt...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("Failed to install dependencies. Please install manually.")

def main():
    # Проверяем, что requirements.txt существует в корне сгенерированного проекта
    if os.path.exists("requirements.txt"):
        install_requirements()
    else:
        print("requirements.txt not found. Skipping dependency installation.")

if __name__ == "__main__":
    main()
