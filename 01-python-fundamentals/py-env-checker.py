import sys
import subprocess
import os
import platform

# -----------------------------------------------
# py-env-checker.py
# Checks if your Python environment is properly set up
# -----------------------------------------------

DIVIDER = "-" * 50

def check_python_version():
    print(DIVIDER)
    print("[1] PYTHON VERSION")
    print(DIVIDER)
    version = sys.version
    major = sys.version_info.major
    minor = sys.version_info.minor
    print(f"Version   : {version}")
    print(f"Executable: {sys.executable}")
    if major < 3:
        print("WARNING: You are using Python 2. Please upgrade to Python 3.")
    elif minor < 9:
        print(f"NOTE: Python 3.{minor} detected. Consider upgrading to 3.11+.")
    else:
        print("OK: Python version looks good.")
    print()


def check_pip():
    print(DIVIDER)
    print("[2] PIP STATUS")
    print(DIVIDER)
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True, text=True
        )
        print(result.stdout.strip())
        print("OK: pip is available.")
    except Exception as e:
        print(f"ERROR: pip not found. {e}")
    print()


def check_venv():
    print(DIVIDER)
    print("[3] VIRTUAL ENVIRONMENT")
    print(DIVIDER)
    in_venv = sys.prefix != sys.base_prefix
    if in_venv:
        print(f"Active venv : {sys.prefix}")
        print("OK: You are inside a virtual environment.")
    else:
        print("WARNING: No virtual environment is active.")
        print("TIP: Run  ->  python3 -m venv venv  then  source venv/bin/activate")
    print()


def check_packages(packages):
    print(DIVIDER)
    print("[4] PACKAGE CHECK")
    print(DIVIDER)
    for pkg in packages:
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "show", pkg],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                # grab version from output
                for line in result.stdout.splitlines():
                    if line.startswith("Version"):
                        version = line.split(":")[1].strip()
                        print(f"  FOUND   {pkg} ({version})")
                        break
            else:
                print(f"  MISSING {pkg}  ->  pip install {pkg}")
        except Exception:
            print(f"  ERROR checking {pkg}")
    print()


def check_requirements_file():
    print(DIVIDER)
    print("[5] requirements.txt")
    print(DIVIDER)
    if os.path.exists("requirements.txt"):
        print("Found requirements.txt")
        with open("requirements.txt", "r") as f:
            lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]
        if lines:
            print(f"Listed packages ({len(lines)}):")
            for line in lines:
                print(f"  - {line}")
        else:
            print("File is empty.")
    else:
        print("No requirements.txt found in current directory.")
        print("TIP: Run  ->  pip freeze > requirements.txt")
    print()


def check_os():
    print(DIVIDER)
    print("[6] SYSTEM INFO")
    print(DIVIDER)
    print(f"OS      : {platform.system()} {platform.release()}")
    print(f"Machine : {platform.machine()}")
    print(f"CWD     : {os.getcwd()}")
    print()


def main():
    print()
    print("=" * 50)
    print("   Python Environment Checker")
    print("=" * 50)
    print()

    check_os()
    check_python_version()
    check_pip()
    check_venv()

    # common packages to check — edit this list as needed
    packages_to_check = ["requests", "numpy", "flask", "pandas"]
    check_packages(packages_to_check)

    check_requirements_file()

    print(DIVIDER)
    print("Audit complete.")
    print(DIVIDER)
    print()


if __name__ == "__main__":
    main()