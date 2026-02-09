import subprocess
import sys
import os

def run(cmd):
    subprocess.run(cmd, check=True)

def install_requirements():
    print("Installing dependencies from requirements.txt...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("Failed to install dependencies. Please install manually.")
        

def init_db():
    print("initialisation database")
    try:
        db_type = "{{cookiecutter.db_type}}"
        if os.path.exists("alembic.ini"):
            run([sys.executable, "-m", "alembic", "revision", "--autogenerate", "-m", "init"])
            run([sys.executable, "-m", "alembic", 'upgrade', 'head'])
            print("Database migrated")
    except subprocess.CalledProcessError:
        print("Failed to initialisate database. Please install manually")

def main():
    # Проверяем, что requirements.txt существует в корне сгенерированного проекта
    if os.path.exists("requirements.txt"):
        install_requirements()
        init_db()
    else:
        print("requirements.txt not found. Skipping dependency installation.")

if __name__ == "__main__":
    main()
